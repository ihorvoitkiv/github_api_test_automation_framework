import os
import json
from abc import ABC, abstractmethod


class BaseFile(ABC):
    """
    BaseFile is an abstract class representing a file.
    Specific file formats handling is implemented in child classes.

    Attributes:
        file_path (str): The full path to the file, default data_dir is '.src/data'
    """

    def __init__(self, filename: str, data_dir: str = '../data') -> None:
        self.file_path = os.path.join(os.getcwd(), data_dir, filename)

    @abstractmethod
    def read(self) -> dict:
        """
        Abstract method for reading the contents of the file.
        """
        pass

    @abstractmethod
    def write(self, data: dict) -> None:
        """
        Abstract method for writing data to the file.
        """
        pass


class JSONFile(BaseFile):
    def read(self) -> dict:
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def write(self, data: dict) -> None:
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=2)
