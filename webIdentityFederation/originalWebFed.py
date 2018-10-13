
# https://web-identity-federation-playground.s3.amazonaws.com/index.html
from boto.sts.connection import STSConnection
sts = STSConnection(anon=True)
 
arn = 'arn:aws:iam::877950674958:role/WebIdFed_Amazon'
session_name = 'web-identity-federation'
token = 'Atza|IwEBIPIBmfyOcO_vUQ8weJgIVpxWXKNXnXNg1FVOYVEKajPe2EKUqMIqinmLNpHulbLWaeemEtenY_TzAWxR0FIw9Nsj9C7Oaj0P-AE694CxURnCwhiglXL6yvrii465Iu9_3FCEFkctp847L3R5BPk0vmFQ8YMJoSfkbvXCVvX5NKZgae8cGlLnXJNp6ImB2UzY-qGvsDkR7k8fLOil-4kUrfmg1eqTSBT2abF_obHpZi1xKcCB1aYt3uPquO4k056_0pi6H5PI0vCioHetLjo_6tBx2SYG1o2FGuX9At0jGRNIpZL_dWhcbIYvjEVSYZEfHVg7jR7wpMcnafX3ct0Q-zb2xrA9iQvDewWmizCs2_Ip5PIlnY8HPr32JiCSE7aT8oHzOh6-NIFmr_99cv7mqUi0d3d188Aj4H8AGBeaOyRAqP9li4FxvPBJoCg7ZIuMPDC02M6yzGGwCcWoJlvJTFCQLsI8zvDQrxkHm4hHMHSoNcwNQr1rXR8v-tKlzY-OKQfyZJ4KkiPCwG4FDS2A5AO_yxILLjFZzx4VHCXELmKd8w'
 creds = sts.assume_role_with_web_identity(
    role_arn=arn,
    role_session_name=session_name,
    web_identity_token=token,
    provider_id='www.amazon.com',
)
print creds.user.arn
print creds.user.assume_role_id