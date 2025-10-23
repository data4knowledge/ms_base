import os
from dotenv import load_dotenv


class ServiceEnvironment:
    def __init__(self):
        self._filename = None
        self._load()

    @property
    def filename(self):
        return self._filename
    
    def environment(self):
        return (
            os.environ["PYTHON_ENVIRONMENT"]
            if "PYTHON_ENVIRONMENT" in os.environ
            else "development"
        )

    def production(self) -> bool:
        return self.environment() == "production"

    def get(self, name: str) -> str | None:
        return os.environ[name] if name in os.environ else None

    def _load(self):
        self._filename = f".{self.environment()}_env"
        load_dotenv(self._filename)
