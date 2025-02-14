import jwt

JWT_SECRET_KEY = 'secret_key'

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiU2hpcm8gR290byIsInBhc3N3b3JkIjoicGFzc3dvcmQiLCJleHAiOjE3Mzk1Mjk0NzR9.hrGho38UIR_kI7oG3O0V6F_BUoELbSObJIv_zehx_pc'

try:
    decoded = jwt.decode(token, JWT_SECRET_KEY, algorithms=['HS256'])
    print(decoded)
except jwt.ExpiredSignatureError:
    print('expired')
except jwt.InvalidTokenError:
    print('invalid')
