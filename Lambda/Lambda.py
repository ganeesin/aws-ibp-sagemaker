from aws_cdk import ( 
    aws_lambda as _lambda,
    aws_s3 as s3,
    aws_ec2 as ec2,
    aws_s3_notifications as s3_notifications,
    aws_apigateway as _apigw,
    App,
    Stack,
    Duration,
    
    
)
from aws_cdk.aws_lambda_event_sources import S3EventSource
from constructs import Construct

import aws_cdk.aws_apigatewayv2_alpha as _apigw
import aws_cdk.aws_apigatewayv2_integrations_alpha as _integrations




import os
from   os import path

class LambdaConstruct(Construct):
    def __init__(self, scope: Construct, id: str, props, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        __dirname = (os.path.dirname(__file__))

# Define lamda function

        self._function = _lambda.Function(
            self, 'Ibpapihandler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.from_asset(path.join(__dirname, './Ibpapihandler')),
            handler='Ibpapihandler.handler',
            environment={
                "DDB_CONFIG_TABLE": props['config'].ddbtable,
       
            },
            vpc=props['vpc'],
            vpc_subnets=ec2.SubnetSelection(subnets=props['subnet']),
            memory_size=2048,
            timeout=Duration.seconds(props['config'].timeout),
            role=props['lambdarole']
        )
        
       # Create the HTTP API with CORS
        http_api = _apigw.HttpApi(
            self, "IbpHttpApi",
            cors_preflight=_apigw.CorsPreflightOptions(
                allow_methods=[_apigw.CorsHttpMethod.GET],
                allow_origins=["*"],
                max_age=Duration.days(10),
            )
        )

        # Add a route to GET /
        http_api.add_routes(
            path="/ibp/demand/ExternalForecastNotification",
            methods=[_apigw.HttpMethod.GET],
            integration=_integrations.HttpLambdaIntegration("LambdaProxyIntegration", handler=self._function),
        )
     
       
       
       
       

        

