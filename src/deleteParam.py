import json
import boto3

ssm = boto3.client("ssm")


def handler(event, context):
    headers = event.get("headers", {})
    param_name = headers.get("x-parameter-name")

    if not param_name:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Missing 'x-parameter-name' header"})
        }

    try:
        ssm.delete_parameter(Name=param_name)
        return {
            "statusCode": 200,
            "body": json.dumps({"message": f"Parameter '{param_name}' deleted successfully"})
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
