import jwt

secret_key = "kufcw2kuyegc26wqdj3chwq1dcljy9"
algorithm = "HS256"


class CredentialsRepository:
    def decode_token(self, token: str) -> str:
        payload = jwt.decode(token, secret_key, [algorithm])
        return payload["username"]

    def make_token(self, username: str) -> str:
        payload = {"username": username}
        token = jwt.encode(payload, secret_key, algorithm)
        return token

    def is_valid_token(self, token: str) -> bool:
        try:
            jwt.decide(token, secret_key, [algorithm])
            return True
        except jwt.ExpiredSignatureError:
            print("Срок годности токена")
            return False
        except Exception:
            print("Какая-то ошибка!")
            return False
