import boto3

client = boto3.client('sts')

arn = '...'
sessions_name = 'web-identity-federation'
token = '...'

creds = client.assume_role_with_web_identity(
    RoleArn=arn,
    RoleSessionName=session_name,
    WebIdentityToken=token,
    ProviderId='www.amazon.com',
)

print creds['AssumedRoleUser']['Arn']
print creds['AssumedRoleUser']['AssumedRoleId']