import boto3


def get_ssm_parameter_value(parameter_string, ssm_client=None):
    if ssm_client is None:
        ssm_client = boto3.client('ssm')

    parameter = ssm_client.get_parameter(Name=parameter_string, WithDecryption=True)

    return parameter['Parameter']['Value']


def lambda_handler(event, context):
    get_ssm_parameter_value("/config/bot/api_token")
    
    return { 
        'status': 200
    }