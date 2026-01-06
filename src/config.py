import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

class Config:
    def __init__(self):
        load_dotenv()

        self.db_server = os.getenv("DB_SERVER")
        self.db_name = os.getenv("DB_NAME")
        self.db_user = os.getenv("DB_USER")
        self.db_password = os.getenv("DB_PASSWORD")
        self.db_driver = os.getenv("DB_DRIVER")

        self._validate()

    def _validate(self):
        required_vars = {
            "DB_SERVER": self.db_server,
            "DB_NAME": self.db_name,
            "DB_USER": self.db_user,
            "DB_PASSWORD": self.db_password,
            "DB_DRIVER": self.db_driver,
        }

        missing = [k for k, v in required_vars.items() if not v]

        if missing:
            raise ValueError(f"Missing environment variables: {missing}")

    @property
    def connection_string(self):
        return (
            f"mssql+pyodbc://{self.db_user}:{self.db_password}"
            f"@{self.db_server}/{self.db_name}"
            f"?driver={str(self.db_driver).replace(' ', '+')}"
        )

    def get_engine(self):
        return create_engine(self.connection_string)
