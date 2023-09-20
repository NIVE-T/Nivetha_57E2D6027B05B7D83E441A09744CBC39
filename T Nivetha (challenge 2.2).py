#Define the base class player
class player:
    def play(self):
        print("The player is playing criket.")
      
#Define the derived class Batsman
class Batsman(player):
    def play(self):
        print(" The batsman is bating.")
      
#Define the derived class Bowler
class Bowler(player):
    def play(self):
        print("The bowler is bowling.")
      
#create objects of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

#call the play()method for each abject
batsman.play()
bowler.play()
