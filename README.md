# Text-To-Speech-AWS-Project
This is a simple text to speech converter using python, Html, CSS, Javascript and AWS cloud services

# Programming Languages and technlogies used
- HTML
- CSS
- Javascript
- Python
- Amazon Web services: Lambda, Polly, API Gateway


# Features
- Users can enter text in a text input field.
- Users can select from different voice options.
- The application sends the text input and voice selection to the backend Lambda function.
- The Lambda function synthesizes speech using Amazon Polly.
- The synthesized audio is uploaded to an S3 bucket.
- The S3 URL of the uploaded audio file is returned to the frontend.
- Users can download the generated audio file from the s3 bucket

# Process
The project started with creating an architecture using excalidraw for the diagram. planning the frontend layout and functionality. Setting up the AWS services (Lambda, Polly, S3) was straightforward but required learning about their configurations and permissions. Then creating the frontend web application using HTML, CSS, AND JAVASCRIPT. Implementing the frontend and backend communication posed several challenges  particularly handling CORS issues and ensuring the correct parsing of responses. Through debugging and several test runs these challenges were overcome, leading to a functional application. 
