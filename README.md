## SAP IBP - External forecast Integration with Amazon Sagemaker
SAP IBP External forecasting allows customers to use external forecasting algorithms  in a tightly integrated process within IBP. This is done in a synchronous process, meaning that the external algorithm is called only if and when you trigger a forecast in SAP IBP, either through interactive forecasting in Excel or via a forecast job.
The data exchange is done through an OData Service, and the external algorithm can be written in R, Python or any other suitable tools. In this sample, We have used services like API Gateway , Lambda and Sagemaker to provide synchronous forecasting in IBP.

## Architecture
![architecture](/External_forecasting.png)


## SAP IBP integration pattern
 The architecture uses the standard documentation provided by SAP OSS note 3170544 and the steps outlined in this [Blog]( https://blogs.sap.com/2022/05/11/how-to-forecast-using-custom-external-algorithms/)   
![Architecture](/IBP_Architecture.png)


This project is intended to be sample code only. Not for use in production.

This project will create the following in your AWS cloud environment specified:
* HTTP API Gateway
* Lambda for processing requestID's
* Roles
* DynamoDB for storing request ID's and their status

Additionally a Jupyter notebook is made available in this repo under python_sample to deploy in a Sagemaker instance.
Since there are different authentication options for outbound connections, please use a [lambda authorizer](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html) appropriate for the chosen authentication method. 

## Deploying the CDK Project

This project is set up like a standard Python project.  For an integrated development environment (IDE), use `AWS Cloud9 environment` to create python virtual environment for the project with required dependencies.  

1. Launch your AWS Cloud9 environment.

2.  Clone the github repository and navigate to the directory.



To manually create a virtualenv 

```
$ python3 -m venv .env
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .env/bin/activate
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

The `appConfig.json` file takes the input paramters for the stack. Maintain the following parameters in the `appConfig.json` before deploying the stack

## AWS environment details
* `account` Enter AWS account id of your AWS cloud environment
* `region`  Enter Region information where the stack resources needs to be created
* `vpcId`   Enter the VPC for Lambda execution from where Lambda can access SAP resources and look out for vision
* `subnet`  Enter the subnet for Lambda exection
## Resource Identifiers
* `stackname` Enter an Identifier/Name for the CDK stack
* `ddbtablename` Enter a name for Dynamo DB Table that would be created as part of the stack which would hold the metadata for creating incidents in SAP
## SAP Environnment details
* `SAP_AUTH_SECRET` Provide the arn where the credentials with keys `user` and `password` and `url ` for accessing SAP IBP OData services.


Bootstrap your AWS account for CDK. Please check [here](https://docs.aws.amazon.com/cdk/latest/guide/tools.html) for more details on bootstraping for CDK. Bootstraping deploys a CDK toolkit stack to your account and creates a S3 bucket for storing various artifacts. You incur any charges for what the AWS CDK stores in the bucket. Because the AWS CDK does not remove any objects from the bucket, the bucket can accumulate objects as you use the AWS CDK. You can get rid of the bucket by deleting the CDKToolkit stack from your account.

```
$ cdk bootstrap aws://<YOUR ACCOUNT ID>/<YOUR AWS REGION>
```

Deploy the stack to your account. Make sure your CLI is setup for account ID and region provided in the appConfig.json file.

```
$ cdk deploy
```

## Cleanup

In order to delete all resources created by this CDK app, run the following command

```
cdk destroy
```

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!