import boto3
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

if __name__ == "__main__":
    add_user_to_db("pranav", "mypassword")
