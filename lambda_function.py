import json


def lambda_handler(event, context):
    print(json.dumps({"event": "Request Data", "details": "deep"}))
    return {"statusCode": 200, "body": json.dumps("Hello from Lambda!")}
