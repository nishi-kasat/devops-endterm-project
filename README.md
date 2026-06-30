# DevOps End Term Project

## Project Title
Automated CI/CD Deployment Pipeline using GitHub, Jenkins, and AWS Cloud Services

## Technologies Used
- Python
- Flask
- Pandas
- Matplotlib
- AWS S3
- AWS EC2
- AWS VPC
- Jenkins
- GitHub

## Features
- Reads MovieLens user dataset
- Displays total users
- Shows average age
- Age distribution analysis
- Occupation distribution analysis
- Sample user records
- CI/CD deployment pipeline

## Project Workflow

1. Source code is maintained using GitHub.
2. Jenkins automatically fetches the latest code after every push.
3. The application is built and tested through the Jenkins pipeline.
4. The application is deployed on an AWS EC2 instance.
5. The dataset is stored in AWS S3 and accessed by the deployed application.

## Repository Structure

```
.
├── app.py
├── Jenkinsfile
├── requirements.txt
├── dataset/
├── templates/
├── static/
└── README.md
```
