def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/html"},
        "body": "<h1>Merhaba, teleskop projesine hoş geldiniz!</h1>"
    }