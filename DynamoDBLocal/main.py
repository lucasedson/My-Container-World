import boto3
import time
time.sleep(3)
dynamodb = boto3.resource(
    'dynamodb',
    endpoint_url='http://localhost:8000',

    region_name='us-east-1',

    aws_access_key_id='dummy',
    aws_secret_access_key='dummy'
)

def create_table():

    try:
        table = dynamodb.create_table(
            TableName='MinhaTabela',
            KeySchema=[{'AttributeName': 'id', 'KeyType': 'HASH'}],
            AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'S'}],
            ProvisionedThroughput={'ReadCapacityUnits': 1, 'WriteCapacityUnits': 1}
        )
        table.wait_until_exists()
        print("✅ Tabela criada com sucesso no DynamoDB Local!")

    except Exception as e:
        print(f"⚠️ Erro: {e}")

def add():
    table = dynamodb.Table('MinhaTabela')
    table.put_item(
        Item={
            'id': '1',
            'name': 'Item 1'
        }
    )

def update():
    table = dynamodb.Table('MinhaTabela')
    response = table.update_item(
    Key={
        'id': '1'
    },
    UpdateExpression="SET #attr_name = :new_value",
    ExpressionAttributeNames={
        '#attr_name': 'name'
    },
    ExpressionAttributeValues={
        ':new_value': 'Item 1 Atualizado'
    },
    ReturnValues="UPDATED_NEW"
    )


def delete():
    table = dynamodb.Table('MinhaTabela')
    table.delete_item(
        Key={
            'id': '1'
        }
    )

def delete_table():
    table = dynamodb.Table('MinhaTabela')
    table.delete()

def read():
    table = dynamodb.Table('MinhaTabela')
    response = table.scan()
    items = response['Items']
    for item in items:
        print(item)

if __name__ == "__main__":
    print("🚀 Iniciando o script...")
    
    print("\nCriando a tabela...")
    create_table()

    print("\nAdicionando itens...")
    add()
    read()

    print("\nAtualizando itens...")
    update()
    read()

    print("\nDeletando itens...")
    delete()
    read()

    print("\nDeletando a tabela...")
    delete_table()