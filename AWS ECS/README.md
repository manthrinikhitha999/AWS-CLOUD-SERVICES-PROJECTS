##Login to the AWS ECR:
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 688567268641.dkr.ecr.us-east-1.amazonaws.com

##Docker Build:
docker build -t 688567268641.dkr.ecr.us-east-1.amazonaws.com/demo-ecrr:latest .

##Docker Push:
docker push .dkr.ecr..amazonaws.com/:latest



# Creating an ECS Cluster
<img width="1920" height="1020" alt="Screenshot 2025-09-11 151213" src="https://github.com/user-attachments/assets/a35bbe57-2b85-4568-b95e-bcb9b7d2ef12" />

<img width="1920" height="1020" alt="Screenshot 2025-09-11 151244" src="https://github.com/user-attachments/assets/1e1693c9-c694-4b94-963a-6e362e53f128" />

<img width="1920" height="1020" alt="Screenshot 2025-09-11 151307" src="https://github.com/user-attachments/assets/f93487d0-335c-41f2-85ee-b0568e31adf8" />

# Creating an ECR Repository
<img width="1920" height="1020" alt="Screenshot 2025-09-11 151424" src="https://github.com/user-attachments/assets/f024ed8f-67d0-4d6c-9fd6-88701867d3b3" />

<img width="1920" height="1020" alt="Screenshot 2025-09-11 151434" src="https://github.com/user-attachments/assets/a99e2efc-227f-49d4-a8ea-8c2525c8564a" />

<img width="1920" height="1020" alt="Screenshot 2025-09-11 151448" src="https://github.com/user-attachments/assets/4b06ff14-57a8-4854-8738-241c2d67ce90" />

# Using WSL to run aws configure & Push commands

<img width="1920" height="1020" alt="Screenshot 2025-09-11 152013" src="https://github.com/user-attachments/assets/b633624a-a48c-419e-a9a3-38c2029f2b7c" />

# Pushing Docker Image to ECR from WSL
<img width="1920" height="1020" alt="Screenshot 2025-09-11 152027" src="https://github.com/user-attachments/assets/b20c7c17-e93f-4709-ab20-d78bdf3cab4d" />

# Using the image from ECR to deploy on ECS by creating a Task Definition (required for deployment)

<img width="1920" height="1020" alt="Screenshot 2025-09-11 152153" src="https://github.com/user-attachments/assets/9375fe38-4868-4a41-b25d-e12d65cd9bbc" />
<img width="1920" height="1020" alt="Screenshot 2025-09-11 152225" src="https://github.com/user-attachments/assets/ce4315f0-9630-42d7-908b-f83bc175f269" />

# Running a Task from Task Definition


<img width="1920" height="1020" alt="Screenshot 2025-09-11 152248" src="https://github.com/user-attachments/assets/9734b272-7063-419e-bced-8f5bc5336ea6" />

# Deploying & Running Your First Container in ECS

<img width="1920" height="1020" alt="Screenshot 2025-09-11 152355" src="https://github.com/user-attachments/assets/b8f88765-68dc-4650-99a9-6dd7dff7650f" />

<img width="1920" height="1020" alt="Screenshot 2025-09-11 152414" src="https://github.com/user-attachments/assets/0bc162e4-9437-4614-a384-2ff20699798f" />

<img width="1920" height="1020" alt="Screenshot 2025-09-11 152440" src="https://github.com/user-attachments/assets/20140113-7117-40f4-9bf9-5e69cd3c78ee" />




