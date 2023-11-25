import abc

class Renderer(abc.ABC):
  @abc.abstractmethod
  def render(self, url: str) -> str:
    pass