import json
import boto3
from botocore.exceptions import ClientError

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

        # ✅ Verifica si existe antes de actualizar
        ssm.get_parameter(Name=name)

        ssm.put_parameter(
            Name=name,
            Value=value,
            Type=param_type,
            Overwrite=True
        )

        return {
            "statusCode": 200,
            "body": json.dumps({"message": f"Parameter '{name}' updated successfully."})
        }

    except ssm.exceptions.ParameterNotFound:
        return {
            "statusCode": 404,
            "body": json.dumps({"error": f"Parameter '{name}' does not exist."})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
