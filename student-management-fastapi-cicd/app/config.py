import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./students.db")
SECRET_KEY = os.getenv("SECRET_KEY", "my-super-secret-key")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
