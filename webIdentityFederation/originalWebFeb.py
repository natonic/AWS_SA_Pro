# https://web-identity-federation-playground.s3.amazonaws.com/index.html
from boto.sts.connection import STSConnection
sts = STSConnection(anon=True)
 
arn = 'arn:aws:iam::714160831934:role/WebIdFed_Amazon'
session_name = 'web-identity-federation'
token = 'Atza|IwEBIHCNkf21oo73Wt-lyq_uCiy0t4fuHW2lI83WA9x2a2mcSAMimZOwFnPh5iRubtq-YC2uY-A-V2Ly_fJq9i2oG1_Nj2FtkvKMe2nKgaPgEcr2myZ37izpH2Kt954dODS4zBBdhDnDExDEsXbZQX0QuFxqcJ575oW_OUulCiCbxg8M7LCWP6QLPIEf2wXywvLH3d_DbWnbpvaIUin71RAefPSlxjwnNd_niSsMJIq1ipBNRma_EeBFqNC7XYJq-A49tXmzxAMKt3NBK7I9VTSFQMNB-DGrBVZFFgDwwTNXmjAf3OUropTj76aDyNKXZbz5AOY1YjISXkdeW2RzXnRGOsDZsA3WDaegAOpcqn4PAsyP9ou_lrhWIQiKvUagvYYom9WqaH-RE_dTQ9YoOh253lsC3gALVHp2RBkXtek4SY-sfstSlalVa3XfLpvTa89Hi-uTIWyRZQ3UO1h9nhDYHULyEvO98bRv5d4oZ5tKrNcWEkLg5jl61ZoV33lK_GVMihpqm4Mz24AwJol3Px67Zd6f4UlgaymXwz9kUuVfhBEjRw'
 creds = sts.assume_role_with_web_identity(
    role_arn=arn,
    role_session_name=session_name,
    web_identity_token=token,
    provider_id='www.amazon.com',
)
print creds.user.arn
print creds.user.assume_role_id

