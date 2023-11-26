from abc import ABC, abstractmethod

class Election(ABC):
  @abstractmethod
  def process(self) -> None:
    pass