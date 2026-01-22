import hashlib
import hmac
import base64
import time
data = "18007"
secretkey = "2a07dab4dbf66725329d4890966d6457"


timestamp = str(int(time.time()))

data_with_timestamp = f"{data}&{timestamp}"

signature = hmac.new(secretkey.encode('utf-8'), msg=data_with_timestamp.encode('utf-8'), digestmod=hashlib.sha256).digest()

encodedSignature = base64.b64encode(signature).decode('utf-8')

print(f"X-cons-id: {data}")
print(f"X-timestamp: {timestamp}")
print(f"X-signature: {encodedSignature}")
