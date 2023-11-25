from .party import Party

class Results:
  def __init__(self) -> None:
    self.parties = []
    self.district_name: str = ""

  def add_party(self, party: Party) -> None:
    self.parties.append(party)

  def get_parties(self) -> Party:
    for party in self.parties:
      yield party

  def __str__(self) -> str:
    res = self.district_name + "\nWyniki:"

    for party in self.get_parties():
      res += f"\n\t{party.name}\t{party.votes}"

    return res
      