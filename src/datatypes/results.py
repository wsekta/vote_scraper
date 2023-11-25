from .party import Party

class Results:
  def __init__(self) -> None:
    self.parties = []

  def add_party(self, party: Party) -> None:
    self.parties.append(party)

  def get_parties(self) -> Party:
    for party in self.parties:
      yield party