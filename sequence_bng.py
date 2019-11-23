# Blind 'n Greedy (BNG) Implementation of Sequence

# d = diamonds, c = clubs, h = hearts, s = spades
# free = corner free spot
BOARD_CARD_LAYOUT = [
  ["free", "2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s", "free"],
  ["6c", "5c", "4c", "3c", "2c", "ah", "kh", "qh", "10h", "10s"],
  ["7c", "as", "2d", "3d", "4d", "5d", "6d", "7d", "9h", "qs"],
  ["8c", "ks", "6c", "5c", "4c", "3c", "2c", "8d", "8h", "ks"],
  ["9c", "qs", "7c", "6h", "5h", "4h", "ah", "9d", "7h", "as"],
  ["10c", "10s", "8c", "7h", "2h", "3h", "kh", "10d", "6h", "2d"],
  ["qc", "9s", "9c", "8h", "9h", "10h", "qh", "qd", "5h", "3d"],
  ["kc", "8s", "10c", "qc", "kc", "ac", "ad", "kd", "4h", "4d"],
  ["ac", "7s", "6s", "5s", "4s", "3s", "2s", "2h", "3h", "5d"],
  ["free", "ad", "kd", "qd", "10d", "9d", "8d", "7d", "6d", "free"]
]

CARD_LOCS = {"free": [(0, 0), (0, 9), (9, 0), (9, 9)], "2s": [(0, 1), (8, 6)], "3s": [(0, 2), (8, 5)], "4s": [(0, 3), (8, 4)], "5s": [(0, 4), (8, 3)], "6s": [(0, 5), (8, 2)], "7s": [(0, 6), (8, 1)], "8s": [(0, 7), (7, 1)], "9s": [(0, 8), (6, 1)], "6c": [(1, 0), (3, 2)], "5c": [(1, 1), (3, 3)], "4c": [(1, 2), (3, 4)], "3c": [(1, 3), (3, 5)], "2c": [(1, 4), (3, 6)], "ah": [(1, 5), (4, 6)], "kh": [(1, 6), (5, 6)], "qh": [(1, 7), (6, 6)], "10h": [(1, 8), (6, 5)], "10s": [(1, 9), (5, 1)], "7c": [(2, 0), (4, 2)], "as": [(2, 1), (4, 9)], "2d": [(2, 2), (5, 9)], "3d": [(2, 3), (6, 9)], "4d": [(2, 4), (7, 9)], "5d": [(2, 5), (8, 9)], "6d": [(2, 6), (9, 8)], "7d": [(2, 7), (9, 7)], "9h": [(2, 8), (6, 4)], "qs": [(2, 9), (4, 1)], "8c": [(3, 0), (5, 2)], "ks": [(3, 1), (3, 9)], "8d": [(3, 7), (9, 6)], "8h": [(3, 8), (6, 3)], "9c": [(4, 0), (6, 2)], "6h": [(4, 3), (5, 8)], "5h": [(4, 4), (6, 8)], "4h": [(4, 5), (7, 8)], "9d": [(4, 7), (9, 5)], "7h": [(4, 8), (5, 3)], "10c": [(5, 0), (7, 2)], "2h": [(5, 4), (8, 7)], "3h": [(5, 5), (8, 8)], "10d": [(5, 7), (9, 4)], "qc": [(6, 0), (7, 3)], "qd": [(6, 7), (9, 3)], "kc": [(7, 0), (7, 4)], "ac": [(7, 5), (8, 0)], "ad": [(7, 6), (9, 1)], "kd": [(7, 7), (9, 2)]}

# CARD_LOCS generation code below.
# CARD_LOCS = {}
# for r in range(len(BOARD_CARD_LAYOUT)):
  # for c in range(len(BOARD_CARD_LAYOUT[r])):
    # card = BOARD_CARD_LAYOUT[r][c]
    # if card in CARD_LOCS:
      # CARD_LOCS[card].append((r, c))
    # else:
      # CARD_LOCS[card] = [(r, c)]


class SequencePlayer():
  playerId = None
  numPlayers = None
  numTeams = None
  numSequencesToWin = None
  numCardsPerHand = None
  
  board = None
  boardLen = 10
  
  def __init__(self, playerId, numPlayers, numTeams, numSequencesToWin, numCardsPerHand):
    self.playerId = playerId
    self.numPlayers = numPlayers
    self.numTeams = numTeams
    self.numSequencesToWin = numSequencesToWin
    self.numCardsPerHand = numCardsPerHand
    
    print("--- Blind 'n Greedy (BNG) Sequence Player ---")
    print(vars(self))
    
    self.board = [[0 for i in range(self.boardLen)] for j in range(self.boardLen)]
  
  def printBoard(self):
    for r in self.board:
      for p in r:
        print(str(p).ljust(4), end = "")
      print("")
  
  def play(self):
    print("Playing")
    
    playerToMove = 1
    gameIncomplete = True
    
    turn = 0
    
    while (gameIncomplete):
      if (playerToMove == self.playerId):
        print("My turn.")
      else:
        print("Player {}'s turn.".format(playerToMove))
        
        card = input("Card played: ")
        
      
      self.printBoard()
      playerToMove = (playerToMove % self.numPlayers) + 1
      turn += 1
      if turn == 20:
        gameIncomplete = False
    
