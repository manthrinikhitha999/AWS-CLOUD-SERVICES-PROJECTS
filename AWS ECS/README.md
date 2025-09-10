##Login to the AWS ECR:
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 688567268641.dkr.ecr.us-east-1.amazonaws.com

##Docker Build:
docker build -t 688567268641.dkr.ecr.us-east-1.amazonaws.com/demo-ecrr:latest .

##Docker Push:
docker push .dkr.ecr..amazonaws.com/:latest

