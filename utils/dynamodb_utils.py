import boto3
import sys

sys.path.append("./utils")
from db_config import default_dynamodb
from get_summary import get_summary


#Returns 0 if username or password have errors
#Returns 1 if username already exists
#Returns 2 if user is successfully added
def add_user_to_db(username, password, dynamodb=None):

    #If input has errors
    if((not username) or (not password)):
        return 0

    #set up the database object
    if not dynamodb:
        dynamodb = default_dynamodb

    #Select the table
    table = dynamodb.Table('Profiles')

    user = dict()
    user["username"] = username

    #Verify that the user does not already exist
    verify = table.get_item(Key=user)

    if 'Item' in verify.keys():
       return 1

    user["password"] = password
    user["bookmarks"] = list()

    table.put_item(Item=user)

    return 2

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

def get_summaries(username):

    dynamodb = default_dynamodb

    table = dynamodb.Table('Profiles')

    key["username"] = username

    bookmarks = table.get_item(Key=key)['Item']['bookmarks']

    return bookmarks

def add_bookmark(username, url):

    dynamodb = default_dynamodb

    table = dynamodb.Table('Profiles')

    key = dict()
    key["username"] = username
    response = table.get_item(Key=key)

    summary = get_summary(url)

    entry = (url, summary)

    arr = response['Item']['bookmarks']

    arr.append(entry)

    table.put_item({"username":username, "password":response['Item']['password'], "bookmarks":arr})

    return True
    

if __name__ == "__main__":
    print (add_user_to_db("meaningless", "data"))
