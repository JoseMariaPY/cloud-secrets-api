import json
import boto3
ssm = boto3.client('ssm')


def handler(event, context):
    headers = event.get("headers", {})
    param_name = headers.get("x-parameter-name")

    if not param_name:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Missing 'x-parameter-name' header"})
        }
    try:
        response = ssm.get_parameter(
            Name=param_name,
            WithDecryption=True
        )
        value = response["Parameter"]["Value"]
        return {
            "statusCode": 200,
            "body": json.dumps({"name": param_name, "value": value})
        }
    except ssm.exceptions.ParameterNotFound:
        return {
            "statusCode": 404,
            "body": json.dumps({"error": f"Parameter '{param_name}' not found"})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }