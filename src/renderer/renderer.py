from abc import ABC, abstractmethod

class Renderer(ABC):
  @abstractmethod
  def render(self, url: str) -> str:
    pass