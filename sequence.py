import argparse

def main(args):
  print(args)


def parseArgs():
  parser = argparse.ArgumentParser(description = "Taking a shot at solving Sequence.")
  parser.add_argument(
    "--players", type = int, required = True,
    choices = {2, 3, 4, 6, 8, 9, 10, 12},
    help = "Total number of players."
  )
  parser.add_argument(
    "--teams", type = int, required = True,
    help = "Number of teams. If the number of teams equals the number of players, each player is individual. Players must be divisible by teams."
  )
  
  args = parser.parse_args()
  if ((args.players % args.teams) != 0):
    parser.error("--players ({}) is not divisble by --teams ({}).".format(args.players, args.teams))
  if ((args.players > 3) and (args.teams == args.players)):
    parser.error("Only 3 players may play individually; the {} players provided must be split into teams.".format(args.players))
  
  return args

if __name__ == "__main__":
  main(parseArgs())
