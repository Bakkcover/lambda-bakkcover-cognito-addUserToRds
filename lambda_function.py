import json

def lambda_handler(event, context):
    username = event['userName']
    email = event['request']['userAttributes']['email']
    sub = event['request']['userAttributes']['sub']
    
    print(username)
    print(email)
    print(sub)
    
    # Return to Amazon Cognito
    return event
