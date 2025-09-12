#!/usr/bin/env python3
import os
import aws_cdk as cdk
from cdk_s3.cdk_s3_stack import CdkS3BucketStack  # ✅ fix here

app = cdk.App()
CdkS3BucketStack(app, "CdkS3BucketStack")  # ✅ use the right class name
app.synth()
