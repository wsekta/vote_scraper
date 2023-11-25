from abc import ABC, abstractmethod
from datatypes import Results

class Parser(ABC):
  @abstractmethod
  def parse(self, html: str) -> Results:
    pass