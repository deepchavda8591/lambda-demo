import json


def lambda_handler(event, context):
    print("Deep Chavda :)")
    print(json.dumps({"event": "Request Data", "details": "deep chavda ML engineer"}))
    return {"statusCode": 200, "body": json.dumps("Hello from Lambda!")}
