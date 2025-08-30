


<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/548e5085-62e7-425d-8cee-9c2be00267e2" />


<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/19495629-e95b-41bb-844b-0c9268725bec" />


<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/b68b5069-fe1a-41a9-956e-71429846ad8d" />


<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/06069db9-203d-423b-8328-08c87562ae5f" />


<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/4f629493-4b45-464d-b9d3-3e8960abeb71" />

<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/bbd76203-cf6a-4d83-905f-4a4a149bd307" />


Errors we got:

<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/1822024b-7097-4f61-abae-14071be49655" />
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/b0262118-17de-49d8-a869-397065d441c4" />
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/3f3f8e8c-502a-4358-b3cb-86fc85ae3c24" />

=================================================================================================================================
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/41892cd9-4980-48fe-acb0-f9a13d96b5a1" />



CASE: 1 (without deleting the EC2 instance ,volume and snapshot.) 




<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/508dc31d-8d2e-44b8-a84f-bbf3856b83a0" />
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/c3b45ba3-f640-4ad1-bd53-2cb447f99b20" />



CASE:2 (By deleting the EC2 instance, lets click on "test" in Lambda functions.



<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/d10c59ad-1502-4d33-8904-ff815bc1674a" />


<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/2e179759-b543-4130-b781-820a7d152be0" />

<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/639600d7-bf4e-4b9a-af7b-fe6251469e51" />


CASE3: Again Create Only the Volume and the snapshot out of Volume you Created now. and test it how it behaves.

<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/8ffc9e7c-1b98-40df-9271-01ab8c81412a" />

<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/395cba28-9268-4efa-b847-84f7078a6443" />

====================================================================================================================================================================
--Here my fundamental principle is if the snapshot is stale, if it belongs to volume that is not attached to any ec2 instance then just go ahead and delete the snapshot. (not the volume)

--Here our script is in such a way that if the snapshot belongs to a volume that is not attached to any ec2 instance then delete the snapshot.
--so here it delete the snapshot . (not the volume)


<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/17174ddb-3fb0-4b0b-afb3-ab5dc39322e9" />


===================================================================================================================================================================
# AWS Cost Optimization – Automating EBS GP2 → GP3 Conversion with Lambda + CloudWatch

This project demonstrates how to implement **governance + automation** for **cost optimization in AWS** using **CloudWatch Events** and **AWS Lambda (Python)**

## 🚀 Project Steps with Screenshots:

### Step 1: Create Lambda Function

<img width="1920" height="1020" alt="Screenshot 2025-08-30 223226 - Copy" src="https://github.com/user-attachments/assets/9f1223ee-0c1f-429f-ba0c-b072cdf2fbdd" />

<img width="1920" height="1020" alt="Screenshot 2025-08-30 223226" src="https://github.com/user-attachments/assets/32ca4527-f261-4a72-b08a-d4d6af5f0ba1" />






































