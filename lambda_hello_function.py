def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'text/plain; charset=utf-8'},
        'body': 'Merhaba, hoş geldiniz! 🚀'
    }