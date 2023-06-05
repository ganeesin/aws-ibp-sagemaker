#!/usr/bin/env python3
from aws_cdk import App,Environment
from aws_ibp_sagemaker.aws_ibp_sagemaker import AwsSapIbpStack
from AppConfig.config import Config

_config = Config()

app = App()

env = Environment(account=_config.account, region=_config.region)

AwsSapIbpStack(app,_config.stackname,env=env)

app.synth()
