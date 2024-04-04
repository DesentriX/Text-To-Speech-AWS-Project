# Text-To-Speech-Project
This is a simple text to speech converter using python, Html, CSS, Javascript and AWS cloud services

# Programming Languages and technlogies used
- HTML
- CSS
- Javascript
- Python
- Backend: Amazon Web services: Lambda, Polly, API Gateway


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

# What I learned:
- Gained familiarity with AWS services like Lambda, Polly, and S3.
- Learned about CORS and how to configure it for cross-origin requests.
- Improved debugging skills for frontend-backend communication.
- Learned about API requests
- learned how to implement front end and backend communication
- Improved research skills
- Improved cloud familiarity


# Improvements:

- Implemented better error handling and logging in both frontend and backend.
- Enhanced user interface with more voice options or customization features.
- Optimized performance, such as reducing the wait time after uploading to S3.


  # Running the Project:
- To run the project, clone the repository and ensure you have AWS credentials set up.
- Install any required dependencies and deploy the Lambda function.
- Update the frontend code with the endpoint URL of the deployed Lambda function.
- Open the HTML file in a web browser to access the application.



# Demo Video
- To showcase the program
- https://streamable.com/o6q5am
