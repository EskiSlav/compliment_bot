from __future__ import annotations

import boto3


def get_ssm_parameter_value(parameter_string, ssm_client=None):
    if ssm_client is None:
        ssm_client = boto3.client('ssm')

    parameter = ssm_client.get_parameter(
        Name=parameter_string, WithDecryption=True,
    )

    return parameter['Parameter']['Value']


def main():
    api_token = get_ssm_parameter_value('/config/bot/api_token')

    return {
        'status': 200,
        'value': api_token[:5] + '*' * len(api_token[5:]),
    }


def lambda_handler(event, context):

    return main()
