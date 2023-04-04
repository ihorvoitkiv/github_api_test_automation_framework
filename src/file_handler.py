import json
import os
from abc import ABC, abstractmethod


class File(ABC):
    def __init__(self, filename, data_dir=None):
        self.filename = filename
        self.data_dir = data_dir

    def read(self):
        with open(self._get_file_path(), 'r') as file:
            return self._read(file)

    def write(self, data):
        with open(self._get_file_path(), 'w') as file:
            self._write(file, data)
        return self

    def _get_file_path(self):
        current_dir = os.path.abspath(os.path.dirname(__file__))
        data_dir = self.data_dir or os.path.join(current_dir, 'data')
        return os.path.join(data_dir, self.filename)

    @abstractmethod
    def _read(self, file):
        pass

    @abstractmethod
    def _write(self, file, data):
        pass


class JSONFile(File):
    def _read(self, file):
        return json.load(file)

    def _write(self, file, data):
        json.dump(data, file)
