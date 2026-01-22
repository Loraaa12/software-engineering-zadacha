from abc import ABC, abstractmethod
from pathlib import Path


class StorageStrategy(ABC):
    @abstractmethod
    def save(self, filename: str, content: bytes) -> None:
        pass


class LocalStorageStrategy(StorageStrategy):
    def __init__(self, base_dir: Path):
        self.base_dir = base_dir

    def save(self, filename: str, content: bytes) -> None:
        path = self.base_dir / filename
        with open(path, "wb") as f:
            f.write(content)
