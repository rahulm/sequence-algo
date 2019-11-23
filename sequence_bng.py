# Blind 'n Greedy (BNG) Implementation of Sequence

class SequencePlayer():
  playerId = None
  numPlayers = None
  numTeams = None
  numSequencesToWin = None
  numCardsPerHand = None
  
  def __init__(self, playerId, numPlayers, numTeams, numSequencesToWin, numCardsPerHand):
    self.playerId = playerId
    self.numPlayers = numPlayers
    self.numTeams = numTeams
    self.numSequencesToWin = numSequencesToWin
    self.numCardsPerHand = numCardsPerHand
    
    print("--- Blind 'n Greedy (BNG) Sequence Player ---")
    print(vars(self))
  
  
  def play(self):
    print("Playing")
