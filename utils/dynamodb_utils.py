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


if __name__ == "__main__":
    add_user_to_db("Vishal", "new_password")
