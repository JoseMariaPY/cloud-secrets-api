import json
import boto3
ssm = boto3.client("ssm")

def handler(event, context):
    try:
        body = json.loads(event.get("body", "{}"))
        name = body.get("name")
        value = body.get("value")
        param_type = body.get("type", "SecureString")

        if not name or not value:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing 'name' or 'value'"})
            }

        ssm.put_parameter(
            Name=name,
            Value=value,
            Type=param_type,
            Overwrite=False
        )

        return {
            "statusCode": 201,
            "body": json.dumps({"message": f"Parameter '{name}' created successfully."})
        }

    except ssm.exceptions.ParameterAlreadyExists:
        return {
            "statusCode": 409,
            "body": json.dumps({"error": f"Parameter '{name}' already exists."})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
