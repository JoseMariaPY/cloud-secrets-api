import json
import boto3

ssm = boto3.client("ssm")

def handler(event, context):
    headers = event.get("headers", {})
    path_prefix = headers.get("x-parameter-path", "/")

    try:
        response = ssm.get_parameters_by_path(
            Path=path_prefix,
            Recursive=True,
            WithDecryption=True
        )
        parameters = [
            {"name": p["Name"]}
            for p in response.get("Parameters", [])
        ]
        return {
            "statusCode": 200,
            "body": json.dumps({"parameters": parameters})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
