Click to watch on YouTube :
# AWS Elastic Container Registry (ECR) | Using WSL | Push Your Image to ECR
https://youtu.be/HOx-TZgzvS8?si=PZbI5F8Dj3XHEhTh

I explored Amazon ECR (Elastic Container Registry) – a fully managed container image registry service on AWS.
# What is ECR? #
 Amazon Elastic Container Registry (ECR) is a fully managed container image registry provided by AWS. In simple terms, it’s a secure place to store, manage, and deploy Docker container images in the cloud.
🔹 Steps I followed in my hands-on session:
 1️⃣ Created an ECR Repository (nikman-demo-repo-app).
 2️⃣ Since I’m using a Windows machine, I went with WSL (Ubuntu) for a Linux-like environment.
👉 Install prerequisites: AWS CLI and Docker(since they were not installed by default):
 Updated Ubuntu: sudo apt update && sudo apt upgrade -y
👉 Password reset tip for WSL: If you forget your WSL user password:
Open PowerShell (Admin)
Step1:wsl -u root
Step2:passwd nikhitha (set new password)
Step3:exit and reopen Ubuntu(WSL)
 Now you can log back in and use sudo with your new password.
3️⃣ Install AWS CLI:
Step1: curl "https://lnkd.in/gB8mDghF" -o "awscliv2.zip"
Step2:unzip awscliv2.zip
Step3:sudo ./aws/install
Step4:aws --version
4️⃣ Install Docker:
Step1: sudo apt install docker.io -y
Step2:sudo service docker start
Step3:sudo usermod -aG docker $USER
Step4:exit
Step5:docker --version
5️⃣ Configure AWS CLI using aws configure:
Step1: aws configure
Enter Access Key ID, Secret Access Key, default region (us-east-1), and output format (json).
💠 Now We are ready to fire the "push commands" on WSL.
--Logged into ECR repository
--Built and tagged Docker image
--Pushed the image to the created repo (nikman-demo-repo-app)
💠 Verified Image & Scan:
 While creating the repo, I enabled image scanning. After pushing the image, ECR automatically scanned it and provided the scan status. ✅
====================================================================================================================================================================

 <img width="1920" height="1020" alt="Screenshot 2025-09-01 222219" src="https://github.com/user-attachments/assets/e110e348-5fc2-4b9d-8f7b-b0a218e0580d" />

 <img width="1920" height="1020" alt="Screenshot 2025-09-01 222304" src="https://github.com/user-attachments/assets/d24d9e36-acff-47d4-8af6-96816b5d331f" />

<img width="1920" height="1020" alt="Screenshot 2025-09-01 222318" src="https://github.com/user-attachments/assets/a5ca2a93-96c2-4620-b732-c24f9dc9f2ab" />

<img width="1920" height="1020" alt="Screenshot 2025-09-01 222333" src="https://github.com/user-attachments/assets/d5db27f4-281b-458e-8067-a9865f7baaed" />

<img width="1920" height="1020" alt="Screenshot 2025-09-01 222237" src="https://github.com/user-attachments/assets/b9a6f71f-1f3c-483c-8243-1345f0fb3e7b" />


 



