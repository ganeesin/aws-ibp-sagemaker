from aws_cdk import ( 
    aws_ec2 as ec2,
    aws_s3 as s3,
    Stack,
    RemovalPolicy,
)
# import constructs
from constructs import Construct
from Lambda.Lambda import LambdaConstruct
from Roles.roles import rolesConstruct
from AppConfig.config import Config
from Dynamo.ddb import ddbConstruct


# Requires docker
# from aws_cdk.aws_lambda_python import(
#     PythonLayerVersion
#     PythonFunction
# )
class AwsSapIbpStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
         
        #Configuration parameters for CDK from 'appConfig.json'
        appConfig = Config()
        
        #1.VPC
        vpc = ec2.Vpc.from_lookup(self,"VPC",vpc_id=appConfig.vpc)
         
        privateSubnets = vpc.select_subnets(subnet_type=ec2.SubnetType.PRIVATE_WITH_NAT)

        lamdbasubnet=[]

        for subnet in privateSubnets.subnets:
            if subnet.subnet_id==appConfig.subnet:
                lamdbasubnet.append(subnet)
 
        
        #3.Roles
        ibprole = rolesConstruct(self, 'p4srole')

        #4.DDB
        ddbConstruct(self, 'ibpconfigddb',props={
             'config': appConfig,
             'ddbrole': ibprole._lambdarole
         } )

     
        #7.Lambda
        LambdaConstruct(self, 'poclambda', props={
            'vpc': vpc,
            'subnet': lamdbasubnet,
            'config': appConfig,
            'lambdarole': ibprole._lambdarole
            })


