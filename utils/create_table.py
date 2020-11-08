import boto3
from db_config import default_dynamodb

def create_table(dynamodb=None):
    if not dynamodb:
        dynamodb = default_dynamodb

    table = dynamodb.create_table(
        TableName='Profiles',
        KeySchema=[
            {
                'AttributeName': 'username',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'username',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )

    return table

if __name__ == '__main__':
    profiles_table = create_table()
    print("Table status", profiles_table.table_status)

'''

        KeySchema=[
            {
                'AttributeName': 'username',
                'KeyType': 'HASH'
            }

            {
                'AttributeName': 'password',
                'KeyType': 'RANGE'
            },
            {
                'AttributeName': 'bookmarks',
                'KeyType': 'RANGE'
            },
        ],
        AttributeType=[
            {
                'AttributeName': 'username',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'password',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'bookmarks',
                'AttributeType': 'L'
            }
        ],
'''
