#jwt library
import jwt

#encoded jwt using header consists of algorithm jwt hs256
encoded_jwt = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
print(encoded_jwt)

jwt.decode(encoded_jwt, "secret", algorithms=["HS256"])

