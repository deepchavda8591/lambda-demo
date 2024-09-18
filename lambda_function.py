import json
from test import two_num_sum

print(f"two_num_sum = {two_num_sum()}")


def lambda_handler(event, context):
    print(json.dumps({"event": "Request Data", "details": "deep"}))
    return {"statusCode": 200, "body": json.dumps("Deep Chavda :)")}
