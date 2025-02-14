from datetime import datetime, timedelta, timezone
import jwt

JWT_SECRET_KEY = 'secret_key'

payload = {
    'user': 'Shiro Goto',
    'password': 'password',
    'exp': datetime.now(timezone.utc) + timedelta(seconds=30)
}

print(payload)

token = jwt.encode(payload, JWT_SECRET_KEY, algorithm='HS256')
print(token)