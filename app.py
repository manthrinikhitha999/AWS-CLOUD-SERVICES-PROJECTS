#!/usr/bin/env python3
import aws_cdk as cdk
from cdk_s3.cdk_s3_stack import CdkS3BucketStack   # ✅ correct import

app = cdk.App()
CdkS3BucketStack(app, "CdkS3Stack")   # ✅ use your actual class
app.synth()
