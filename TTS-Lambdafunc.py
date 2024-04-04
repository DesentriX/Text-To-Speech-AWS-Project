import boto3
import io
import json
import time  # Import the time module

def lambda_handler(event, context):
    try:
        # Retrieves users input (text and voice options)
        text = event['text']
        voice_id = event['voice']

        # Initialize Polly client
        polly = boto3.client('polly')

        # Synthesize speech
        response = polly.synthesize_speech(Text=text, OutputFormat='mp3', VoiceId=voice_id)

        # Upload  the audio data to S3 bucket
        s3 = boto3.client('s3')
        bucket_name = 'audios-21' 
        file_name = f"{context.aws_request_id}.mp3"  # Uses request ID as the file name
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=response['AudioStream'].read())

        # Construct S3 URL of the uploaded audio file
        s3_url = f"https://{bucket_name}.s3.amazonaws.com/{file_name}"
        
        # Wait for a short period to ensure the file is available in S3
        time.sleep(2)

        # Get the origin from the request headers
        origin = event.get('headers', {}).get('Origin', 'http://127.0.0.1:5500')

        # Set headers for CORS(Cross-origin resource sharing)
        headers = {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': origin,  # Sets the Access-Control-Allow-Origin header to the request origin
            'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token,Access-Control-Allow-Origin',
            'Access-Control-Allow-Methods': 'OPTIONS,POST'
        }
        
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({'audioUrl': s3_url})
        }
    except KeyError as e:
        # Handle missing 'voice' key in the event object
        error_message = f"Missing 'voice' key in the request: {str(e)}"
        return {
            'statusCode': 400,  # Bad request
            'body': error_message
        }
    except Exception as e:
        # Handle other exceptions
        error_message = str(e)
        return {
            'statusCode': 500,
            'body': error_message
        }
