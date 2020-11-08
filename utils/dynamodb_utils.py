import boto3
import sys

sys.path.append("./utils")
from db_config import default_dynamodb


def add_user_to_db(username, password, dynamodb=None):
    if((not username) or (not password)):
        return False

    if not dynamodb:
        dynamodb = default_dynamodb

    table = dynamodb.Table('Profiles')

    user = dict()
    user["username"] = username
    user["password"] = password
    table.put_item(Item=user)
    return True

#If user does not exist, returns 0
#If user does exist but password is wrong, returns 1
#If user and password match, returns 2
def verify_login(username, password, dynamodb=None):
    if not username:
        return 0

    if not password:
        return 1

    if not dynamodb:
        dynamodb = default_dynamodb

    table = dynamodb.Table('Profiles')

    key = dict()

    key["username"] = username

    response = table.get_item(Key=key)

    if 'Item' not in response.keys():
        return 0

    elif response['Item']['password'] != password:
        return 1

    else:
        return 2


if __name__ == "__main__":
    verify_login("meaningless", "data")
