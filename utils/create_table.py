import boto3

def create_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

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
