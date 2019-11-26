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

ONE_EYED_JACKS = {"jh", "js"}
TWO_EYED_JACKS = {"jd", "jc"}

# VALID_CARDS generation code below.
# VALID_CARDS = set(CARD_LOCS.keys())
# VALID_CARDS.update(ONE_EYED_JACKS)
# VALID_CARDS.update(TWO_EYED_JACKS)
# VALID_CARDS.remove("free")

VALID_CARDS = {"5c", "5s", "7d", "5d", "8s", "10d", "jc", "3c", "3s", "4c", "7c", "qs", "8h", "3h", "6c", "10c", "ad", "jd", "8c", "ks", "2h", "7h", "6d", "3d", "2c", "jh", "5h", "4d", "js", "9s", "9h", "kc", "10h", "qh", "10s", "4s", "9c", "6s", "4h", "kd", "qd", "2s", "8d", "ah", "as", "2d", "7s", "qc", "6h", "ac", "9d", "kh"}


ASCII_COLOR_CODES = {
  "blue" : "\033[94m",
  "green" : "\033[92m",
  "red" : "\033[91m",
  "end" : "\033[0m"
}

class SequencePlayer():
  playerId = None
  numPlayers = None
  numTeams = None
  numSequencesToWin = None
  numCardsPerHand = None
  playerToTeamMap = None
  teamScores = None
  
  teamColorNames = None
  teamColorAscii = None
  
  board = None
  boardLen = 10
  numPawnsInASequence = 5
  
  botHand = None
  
  def __init__(self, playerId, numPlayers, numTeams, numSequencesToWin, numCardsPerHand, teamColors = None):
    self.playerId = playerId
    self.numPlayers = numPlayers
    self.numTeams = numTeams
    self.numSequencesToWin = numSequencesToWin
    self.numCardsPerHand = numCardsPerHand
    
    self.playerToTeamMap = {(player + 1) : ((player % self.numTeams) + 1) for player in range(self.numPlayers)}
    
    print("--- Blind 'n Greedy (BNG) Sequence Player ---")
    print(vars(self))
    
    self.board = [[0 for i in range(self.boardLen)] for j in range(self.boardLen)]
    for r in [0, self.boardLen - 1]:
      for c in [0, self.boardLen - 1]:
        self.board[r][c] = "free"
    
    self.teamScores = {team : 0 for team in range(1, self.numTeams + 1)}
    
    self.botHand = []
    
    if teamColors is None:
      self.teamColorNames = {t : str(t) for t in range(1, self.numTeams + 1)}
      self.teamColorAscii = {t : "" for t in range(1, self.numTeams + 1)}
      self.teamColorAscii["end"] = ""
    else:
      # assumes teamColors is a list, ordered by team order
      self.teamColorNames = {(t + 1) : tcolor.lower() for t, tcolor in enumerate(teamColors)}
      self.teamColorAscii = {t : ASCII_COLOR_CODES[tcolor] for t, tcolor in self.teamColorNames.items()}
      self.teamColorAscii["end"] = ASCII_COLOR_CODES["end"]
  
  def printMatrix(self, matrix, spacing):
    for row in matrix:
      for val in row:
        print(str(val).ljust(spacing), end = "")
      print("")
  
  def printCardLayout(self):
    self.printMatrix(BOARD_CARD_LAYOUT, 6)
  
  def printBoard(self):
    for row in self.board:
      for val in row:
        head = "" if ((val == "free") or (val == 0)) else self.teamColorAscii[abs(val)]
        foot = "" if ((val == "free") or (val == 0)) else self.teamColorAscii["end"]
        print("{}{}{}".format(head, str(val).ljust(6), foot), end = "")
      print("")
  
  def printSequence(self, seq):
    emptyBoard = [[0 for r in range(self.boardLen)] for c in range(self.boardLen)]
    for (r, c) in seq:
      emptyBoard[r][c] = "X"
    self.printMatrix(emptyBoard, 6)
  
  def initBotHand(self):
    print("What cards do I start off with?")
    while True:
      cards = input("Initial hand (card codes separated by spaces): ")
      cards = cards.lower().split(" ")
      
      if (len(cards) != self.numCardsPerHand):
        print("Wrong number of cards. Need {} cards total. Retrying.".format(self.numCardsPerHand))
        continue
      
      if any((c not in VALID_CARDS) for c in cards):
        print("Hand is invalid. Retrying.")
        continue
      
      # if successful, break
      self.botHand = cards
      print("Bot hand: {}".format(self.botHand))
      break
  
  def play(self):
    print("Playing")
    self.printCardLayout()
    print("")
    
    self.initBotHand()
    print("")
    
    playerToMove = 1
    gameIncomplete = True
    
    # markers
    markers = {
      "retry" : False,
      "twoEyedJack" : False,
      "oneEyedJack" : False
    }
    
    while (gameIncomplete):
      teamToMove = self.playerToTeamMap[playerToMove]
      
      shouldPrintBoard = True
      
      if (playerToMove == self.playerId):
        self.playBotTurn(playerToMove, teamToMove)
      else:
        self.recordPlayerTurn(playerToMove, teamToMove, markers)
        if any(markers.values()):
          continue
      
      # reset markers
      # TODO: check if this is necessary
      markers["retry"] = False
      markers["oneEyedJack"] = False
      markers["twoEyedJack"] = False
      
      playerToMove = (playerToMove % self.numPlayers) + 1
      
      print("---\n\n")
      
      # check if any team has won
      for teamId, teamScore in self.teamScores.items():
        if (teamScore >= self.numSequencesToWin):
          gameIncomplete = False
          print("Team {} wins!".format(self.teamColorNames[teamId]))
          break
  
  def recordPlayerTurn(self, playerToMove, teamToMove, markers):
    if not (markers["retry"] or markers["oneEyedJack"] or markers["twoEyedJack"]):
      print("Player {}'s (team {}) turn.".format(playerToMove, self.teamColorNames[teamToMove]))
    
    prompt = "Card played: "
    if markers["twoEyedJack"]:
      prompt = "Card to place pawn at: "
    if markers["oneEyedJack"]:
      prompt = "Card to remove pawn at: "
    card = input(prompt)
    
    if (card == "pass"):
      print("Passing.")
    elif (card in ONE_EYED_JACKS):
      if (markers["twoEyedJack"] or markers["oneEyedJack"]):
        print("Need a non-jack card.")
        markers["retry"] = True
        return
      
      # only proceed if there are pawns that can be removed
      allowedVals = {team for team in range(1, self.numTeams + 1) if (teamToMove != team)}
      options = [
        (r, c) for r in range(self.boardLen) for c in range(self.boardLen)
        if (self.board[r][c] in allowedVals)
      ]
      
      if (len(options) == 0):
        print("No pawns can be removed. Play a different card.")
        markers["retry"] = True
        return
      else:
        print("One eyed jack. Need a card to remove a pawn from.")
        markers["oneEyedJack"] = True
        return
      
    elif (card in TWO_EYED_JACKS):
      if (markers["twoEyedJack"] or markers["oneEyedJack"]):
        print("Need a non-jack card.")
        markers["retry"] = True
        return
      
      # only proceed if there are spaces where a pawn can be placed
      allowedVals = {0}
      options = [
        (r, c) for r in range(self.boardLen) for c in range(self.boardLen)
        if ((BOARD_CARD_LAYOUT[r][c] != "free") and (self.board[r][c] in allowedVals))
      ]
      
      if (len(options) == 0):
        print("No open spaces to place a pawn. Play a different card.")
        markers["retry"] = True
        return
      else:
        print("Two eyed jack. Need another card for pawn placement.")
        markers["twoEyedJack"] = True
        return
      
    elif (card == "free") or (card not in CARD_LOCS):
      print("Not a valid card. Retrying.")
      markers["retry"] = True
      return
      
    else:
      # This handles 3 situations:
      # - normal non-jack card
      # - finding a pawn to remove due to a one eyed jack
      # - finding a pawn to add due to a two eyed jack
      
      allowedVals = {0}
      
      # Note: the one eyed jack solution here assumes all teams consist of one player
      # TODO: add support for non-singular teams
      if markers["oneEyedJack"]:
        allowedVals = {team for team in range(1, self.numTeams + 1) if (teamToMove != team)}
      
      options = [(r, c) for (r, c) in CARD_LOCS[card] if (self.board[r][c] in allowedVals)]
      
      if len(options) == 0:
        print("No options were found for that card. Retrying.")
        markers["retry"] = True
        return
      else:
        print("Options (top to down, left to right):")
        for optionInd, (r, c) in enumerate(options):
          print("    {}  -  row={} col={}".format(optionInd + 1, r, c))
        optionChoice = input("Select: ")
        
        try:
          optionChoice = int(optionChoice) - 1
          if (optionChoice <= -1) or (optionChoice >= len(options)):
            raise Exception()
        except:
          print("Choice was invalid. Retrying.")
          markers["retry"] = True
          return
        
        optionR, optionC = options[optionChoice]
        self.board[optionR][optionC] = 0 if markers["oneEyedJack"] else teamToMove
    
    # reset markers if finished move without returning
    markers["retry"] = False
    markers["oneEyedJack"] = False
    markers["twoEyedJack"] = False
    
    # check if sequences were completed
    while True:
      seqs = self.newSequencesMade(teamToMove)
      if (len(seqs) == 0):
        break
      
      print(">>> New sequences found <<<")
      seqToApply = None
      
      # if only one option, then apply it
      if (len(seqs) == 1):
        seqToApply = seqs[0]
      else:
        # otherwise, show possibilities, allow player to select one at a time
        print("Select which one to apply from below:")
        for seqInd, seq in enumerate(seqs):
          # 9 * 6 + 1
          # 54 + 1
          # 54 / 2 = 27
          # 52 / 2 = 26
          print("{0} {1} {0}".format("-"*int(52 / 2), seqInd + 1))
          self.printSequence(seq)
          print("")
        
        while True:
          seqInd = input(">>> Sequence to apply: ")
          try:
            seqInd = int(seqInd) - 1
            if (seqInd <= -1) or (seqInd >= len(seqs)):
              raise Exception()
          except:
            print("Choice was invalid. Retrying.")
            continue
          
          seqToApply = seqs[seqInd]
          break
        
      # apply single sequence
      for (r, c) in seqToApply:
        if self.board[r][c] == teamToMove:
          self.board[r][c] = -teamToMove
      
      # increment team score
      self.teamScores[teamToMove] += 1
      
      # if the score is already a winning one, then end
      if self.teamScores[teamToMove] >= self.numSequencesToWin:
        break
    
    print("")
    self.printBoard()
  
  def getPawnForHeuristic(self, r, c):
    if ((r < 0) or (c < 0) or (r >= self.boardLen) or (c >= self.boardLen)):
      return 0
    return self.board[r][c]
  
  def calculateHeuristicScoreOnSegment(self, teamId, segmentLength, rStart, cStart, rSlope, cSlope):
    numPawnsPerTeam = {t : 0 for t in range(1, self.numTeams + 1)}
    countedUsedPawn = {t : False for t in range(1, self.numTeams + 1)}
    
    totalSpaceCount = 0
    r, c = rStart, cStart
    
    while (totalSpaceCount < segmentLength):      
      pawnAtSpace = self.getPawnForHeuristic(r, c)
      teamsToIncrement = []
      if (pawnAtSpace == "free"):
        for t in numPawnsPerTeam.keys():
          numPawnsPerTeam[t] += 1
      elif (pawnAtSpace in numPawnsPerTeam.keys()):
        numPawnsPerTeam[pawnAtSpace] += 1
      elif ((pawnAtSpace < 0) and not countedUsedPawn[-pawnAtSpace]):
        numPawnsPerTeam[-pawnAtSpace] += 1
        countedUsedPawn[-pawnAtSpace] = True
      
      r += rSlope
      c += cSlope
      totalSpaceCount += 1
    
    # calculate score
    numBotPawns = numPawnsPerTeam[teamId]
    totalScore = 0
    for t in range(1, self.numTeams + 1):
      numPawns = numPawnsPerTeam[t]
      if (t == teamId):
        weight = pow((self.teamScores[t] + 1) / self.numSequencesToWin, 3)
        ts = pow(numPawns + (1 if (numPawns == self.numPawnsInASequence) else 0), 2)
        totalScore += (weight * ts)
      else:
        weight = pow((self.teamScores[t]
            + (2 if
              ((numPawns == (self.numPawnsInASequence - 1)) and (numBotPawns == 0) and (self.teamScores[t] == (self.numSequencesToWin - 1)))
            else 1))
          / self.numSequencesToWin,
          3)
        ts = pow(numPawns, 2)
        totalScore -= (weight * ts)
    
    return totalScore
  
  def calculateHeuristicScore(self, teamId):
    # This heuristic score is based on averaging the heuristic score of every possible 5 segment on the board.
    vals = []
    
    # calculate downward segements
    # adding virtual padding to top and bottom of board
    for r in range(-self.numPawnsInASequence + 1, self.boardLen):
      for c in range(self.boardLen):
        vals.append(self.calculateHeuristicScoreOnSegment(teamId, self.numPawnsInASequence, r, c, 1, 0))
    
    # calculate rightward segements
    # adding virtual padding to left and right of board
    for r in range(self.boardLen):
      for c in range(-self.numPawnsInASequence + 1, self.boardLen):
        vals.append(self.calculateHeuristicScoreOnSegment(teamId, self.numPawnsInASequence, r, c, 0, 1))
    
    # calculate diagonal right segements
    # adding virtual padding to all sides of board
    for r in range(-self.numPawnsInASequence + 1, self.boardLen):
      for c in range(-self.numPawnsInASequence + 1, self.boardLen):
        vals.append(self.calculateHeuristicScoreOnSegment(teamId, self.numPawnsInASequence, r, c, 1, 1))
    
    # calculate diagonal left segements
    # adding virtual padding to all sides of board
    for r in range(-self.numPawnsInASequence + 1, self.boardLen):
      for c in range(0, self.boardLen + self.numPawnsInASequence - 1):
        vals.append(self.calculateHeuristicScoreOnSegment(teamId, 5, r, c, 1, -1))
    
    return float(sum(vals)) / len(vals)
  
  def playBotTurn(self, botPlayerId, botTeamId):
    print("My turn.")
    
    # for this algo:
    # - always replace dead cards first
    # - determine card to play based on heuristic-based planning. see below.
    
    # replace dead card, if possible
    for cardInd in range(len(self.botHand)):
      card = self.botHand[cardInd]
      
      # ignore jacks
      if (card in ONE_EYED_JACKS) or (card in TWO_EYED_JACKS):
        continue
      
      # get open slots
      slots = sum(1 for (r, c) in CARD_LOCS[card] if (self.board[r][c] == 0))
      
      # replace card if no open slots found
      if (slots == 0):
        print("Discarding {}. Please pick up a replacement.".format(card))
        while True:
          replacementCard = input("Card picked for replacement: ")
          if (replacementCard not in VALID_CARDS):
            print("Replacement card is invalid. Retrying.")
          else:
            del self.botHand[cardInd]
            self.botHand.append(replacementCard)
            break
        
        # once replacement is complete, break out of dead card check
        break
    
    print("Bot hand: {}".format(self.botHand))
    
    bestAction = {
      "card" : None,
      "location" : None,
      "score" : float("-inf")
    }
    # bestAction contains:
    # - card : the card to use from self.botHand
    # - location : the (r, c) where the action should take place
    # - score : the score of this action
    # The action (addition or removal) is inferred from the card.
    
    # flag if the bot should search for a killer move
    killerMoveNeeded = (self.teamScores[botTeamId] == (self.numSequencesToWin - 1))
    
    # perform search to find the best card to place
    for card in self.botHand:
      
      # the list of locations where the action can be taken
      locationOptions = None
      
      # note the type of action for ease of use
      isRemoval = False
      
      if card in ONE_EYED_JACKS:
        isRemoval = True
        allowedVals = {t for t in range(1, self.numTeams + 1) if (t != botTeamId)}
        locationOptions = [
          (r, c) for r in range(self.boardLen) for c in range(self.boardLen)
          if (self.board[r][c] in allowedVals)
        ]
      elif card in TWO_EYED_JACKS:
        allowedVals = {0}
        locationOptions = [
          (r, c) for r in range(self.boardLen) for c in range(self.boardLen)
          if (self.board[r][c] in allowedVals)
        ]
      else:
        locationOptions = [
          (r, c) for (r, c) in CARD_LOCS[card]
          if (self.board[r][c] == 0)
        ]
      
      # save the value to place, for ease of use
      valToPlace = 0 if isRemoval else botTeamId
      
      killerMoveFound = False
      # try placing (or removing) a pawn from each location in locationOptions
      for (pawnR, pawnC) in locationOptions:
        # get previous value for restoration
        prevVal = self.board[pawnR][pawnC]
        
        # place valToPlace
        self.board[pawnR][pawnC] = valToPlace
        
        # killer move check:
        # if the bot team needs only one more sequence to win, and this pawn placement created a new sequence, then use this
        if killerMoveNeeded:
          # test if any sequences were made
          killerMoveFound = (len(self.newSequencesMade(botTeamId)) > 0)
        
        # if a killer move was not found, then continue search
        if not killerMoveFound:
          placementScore = self.calculateHeuristicScore(botTeamId)
          if (placementScore > bestAction["score"]):
            bestAction["card"] = card
            bestAction["location"] = (pawnR, pawnC)
            bestAction["score"] = placementScore
        
        # replace prevVal to pawn location at the end of this iteration
        self.board[pawnR][pawnC] = prevVal
        
        # break if a killer move was found
        if killerMoveFound:
          break
        
    
    
    # if the action is unfilled, then no valid one was found, and we must continue without performing it
    if (bestAction["card"] is None):
      print("No valid card found. Please skip my turn.")
    else:
      # remove card from botHand to play it
      bestCard = bestAction["card"]
      bestLocR = bestAction["location"][0]
      bestLocC = bestAction["location"][1]
      self.botHand.remove(bestCard)
      
      # save prevTeamVal for printing
      prevTeamVal = self.board[bestLocR][bestLocC]
      
      # place or remove pawn at location, as necessary
      valToPlace = 0 if (bestCard in ONE_EYED_JACKS) else botTeamId
      self.board[bestLocR][bestLocC] = valToPlace
      
      # print action
      print(">>> Played {} at row={} col={} <<<".format(bestCard, bestLocR, bestLocC))
      # if it was a removal (replacement with empty=0), notify
      if (valToPlace == 0):
        print(">>> Removed team {}'s pawn from {} <<<".format(self.teamColorNames[prevTeamVal], BOARD_CARD_LAYOUT[bestLocR][bestLocC]))
      # if it was a two eyed jack, notify
      if (bestCard in TWO_EYED_JACKS):
        print(">>> Placed pawn on {} space <<<".format(BOARD_CARD_LAYOUT[bestLocR][bestLocC]))
    
    # after performing the action, check if any sequences were made.
    # if they were, automatically select the first one every time.
    while True:
      seqsMade = self.newSequencesMade(botTeamId)
      if (len(seqsMade) == 0):
        break
      else:
        # apply the first sequence
        seqToApply = seqsMade[0]
        for (r, c) in seqToApply:
          if (self.board[r][c] == botTeamId):
            self.board[r][c] = -botTeamId
        
        # increment bot sequence count
        self.teamScores[botTeamId] += 1
    
    # print updated board
    self.printBoard()
    
    # print new team score
    print("Bot team score: {}\n".format(self.teamScores[botTeamId]))
    
    # ask for next card
    print("I need to pick up a card.")
    while True:
      nextCard = input("Card picked up: ")
      if nextCard in VALID_CARDS:
        self.botHand.append(nextCard)
        print("Added card {}.".format(nextCard))
        break
      else:
        print("Card '{}' invalid. Retrying.".format(nextCard))
    
    
    
    # perform heuristic-based planning.
    # select the card/placement that will maximize the path score.
    # the path score for the board = (bot's heuristic score) - (alpha * (sum of heuristic scores of all other teams))
    # alpha is a hyperparmeter to place more or less weight on minimizing opponent scores.
    # need to determine an appropriate heuristic score.
    # can keep the best action in a dictionary for ease.
    
    """
    Heuristic ideas:
    (can be combined, such as with a weighted average)
    (this is per team)
    
    + number of completed sequences
    + number of pawns on the board
    + average length of all sequences (even incomplete)
    
    ---
    For each 5 card segment on the board:
      = ((# bot pawns) - (# opponent pawns))^3
    Average or sum the above values.
    
    [ b b b 0 0 ]
    = (3 - 0)^3 = 27
    [ b b b b 0 ]
    = (4 - 0)^3 = 64
    delta = 64 - 27 = 37
    
    [ g g g g 0 ]
    = (0 - 4)^3 = (-4)^3 = -64
    [ g g g g b ]
    = (1 - 4)^3 = (-3)^3 = -27
    delta = (-27) - (-64) = 37
    
    
    ---
    For each 5 card segment on the board:
      h(team) = ((alpha * (# team pawns)) - (# opponent pawns))^3
        (alpha > 1)
      
      h(bot) = ((# bot pawns) - (# opponent pawns))^3 - (sum of h(team) for all opponent teams)
    Average or sum the above h(bot) values.
    
    alpha = 2
    [ b b b 0 0 ]
    = (3 - 0)^3 - (0) = 27
    [ b b b b 0 ]
    = (4 - 0)^3 - (0) = 64
    delta = 64 - 27 = 37
    
    [ g g g g 0 ]
    = (0 - 4)^3 - (2*4 - 0)^3 = (-4)^3 - (8)^3 = -64 - 512 = -576
    [ g g g g b ]
    = (1 - 4)^3 - (2*4 - 1)^3 = (-3)^3 - (7)^3 = -27 - 343 = -370
    delta = (-370) - (-576) = 206
    
    ---
    For each 5 card segment on the board:
      h(team) = ((# team pawns) - (# opponent pawns))^3
      
      h(bot) = ((# bot pawns) - (# opponent pawns))^3 - (sum of h(team) for all opponent teams)
    Average or sum the above h(bot) values.
    
    [ b b b 0 0 ]
    = (3 - 0)^3 - (0) = 27
    [ b b b b 0 ]
    = (4 - 0)^3 - (0) = 64
    delta = 64 - 27 = 37
    
    [ g g 0 0 0 ]
    = (0 - 2)^3 - (2 - 0)^3 = (-2)^3 - (2)^3 = -8 - 8 = -16
    [ g g b 0 0 ]
    = (1 - 2)^3 - (2 - 1)^3 = (-1)^3 - (1)^3 = -1 - 1 = -2
    delta = (-2) - (-16) = 14
    
    [ g g g 0 0 ]
    = (0 - 3)^3 - (3 - 0)^3 = (-3)^3 - (3)^3 = -27 - 27 = -54
    [ g g g b 0 ]
    = (1 - 3)^3 - (3 - 1)^3 = (-2)^3 - (2)^3 = -8 - 8 = -16
    delta = (-16) - (-54) = 38
    
    [ g g g g 0 ]
    = (0 - 4)^3 - (4 - 0)^3 = (-4)^3 - (4)^3 = -64 - 64 = -128
    [ g g g g b ]
    = (1 - 4)^3 - (4 - 1)^3 = (-3)^3 - (3)^3 = -27 - 27 = -54
    delta = (-54) - (-128) = 74
    
    [ b b b b 0 ]
    = (4 - 0)^3 - (0) = 64
    [ b b b b b ]
    = (5 - 0)^3 - (0) = 125
    delta = 125 - 64 = 61
    
    
    ---
    For each 5 card segment on the board:
      h(team) = ((teamScore[team] + 1)/numSequencesToWin) * ((# team pawns) - (# opponent pawns))^3
      
      score = h(bot) - (sum of h(team) for all opponent teams)
      
    Average or sum the above score values.
    
    >>> For now, hardcode the "killer move".
    >>> That is, if the bot's team only needs one more sequence to win, and the bot finds a 5 card segment it can fill to make a sequence, immediately select that and return.
    >>> Need to look into better heuristic/score functions.
    >>> May be able to train a CNN-type model through reinforcement learning based only on the current game state and the bot's hand. (Through simulated play against itself.)
    
    
    """
    
    

  def newSequencesMade(self, teamId):
    
    validSeqs = []
    
    for row in range(self.boardLen):
      for col in range(self.boardLen):
        startTeam = self.board[row][col]
        
        # skip if not a valid starting point
        if ((startTeam != "free") and (abs(startTeam) != teamId)):
          continue
        
        # in each of the 4 directions, attempt to make a sequence
        # directions: right, down, diagonal right, diagonal left
        for (rSlope, cSlope) in [
          (0, 1), # right
          (1, 0), # down
          (1, 1), # diagonal right
          (1, -1), # diagonal left
        ]:
          # start counting
          seq = []
          count = 0
          allNew = True
          r, c = row, col
          while ((r >= 0) and (r < self.boardLen) and (c >= 0) and (c < self.boardLen)):
            pawn = self.board[r][c]
            
            if ((pawn == teamId) or (pawn == "free")):
              count += 1
              seq.append((r, c))
            elif ((pawn == -teamId) and allNew):
              allNew = False
              count += 1
              seq.append((r, c))
            else:
              break
            
            if (count == self.numPawnsInASequence):
              validSeqs.append(seq)
              break
            
            r += rSlope
            c += cSlope
    
    return validSeqs

