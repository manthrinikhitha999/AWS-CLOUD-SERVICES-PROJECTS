# app.py
import aws_cdk as cdk
from my_project.my_stack import MyStack  # <- your stack file

app = cdk.App()
MyStack(app, "CdkS3Stack")   # 👈 stack name must match here
app.synth()
