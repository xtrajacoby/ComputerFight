from re import search
from random import randint, random
from sys import exit

class FightSimulation:
  def __init__(self):
    self.running = True
    self.victory = True
    self.your_health = 100
    self.your_strength = 15
    self.your_speed = 10
    self.cpu_health = 150
    self.cpu_strength = 10
    self.cpu_anger = 10
    
  def play(self):
    self.intro()
    player_turn = True
    while self.running:
      if player_turn:
        self.user_choice()
      else:
        self.cpu_choice()
      player_turn = not player_turn
    if self.victory:
      self.win()
    else:
      self.lose()
  #End play
   
  def intro(self):
    action = raw_input("What would you do if your computer was evil?\n")
    if search("fight", action.lower()):
      self.your_strength += 20
      print "Good Choice, your adrenaline is PUMPING!"
  #End intro
  
  def user_choice(self):
    print "What do you do\n (a) turn it off\n (b) spill on it\n (c) punch it\n (d) headbutt it"
    action = raw_input()
    if action == "a": #Turn off
      if self.your_speed * randint(1, 12) > self.cpu_health:
        self.victory = True
        self.running = False
      else:
        print "You failed in turning off the powerful cpu\n"
    elif action == "b": #Spill
      print "You really pissed off the cpu\n"
      self.cpu_anger += 1
    elif action == "c": #Punch
      if self.your_speed * self.your_health > self.cpu_health * randint(1, 3):
        self.cpu_health -= self.your_strength
        print "Nice Shot! The computer's health is now: " + str(self.cpu_health)
      else:
        print "You suck! The computer (who can't move) dodged your attack\n"
    elif action == "d": #Headbutt
      if self.your_speed * self.your_health > self.cpu_health * randint(2, 3):
        self.cpu_health -= self.your_strength + 5
        print "Nice Shot! The computer's health is now: " + str(self.cpu_health)
      else:
        print "You suck! The computer (who can't move) dodged your attack\n"
    else:
      print "Stop Dicking around!"
  #End user_choice
    
  def cpu_choice(self):
    decision = random()
    if decision < .3:  #shock
      self.your_health -= self.cpu_strength
      print "The computer shocked your ass your health is now: " + str(self.your_health) + "\n"
      if self.your_health <= 0:
        self.victory = False
        self.running = False
    elif decision < .6:  #intimidate
      self.your_strength -= 1
      self.your_speed -= 1
      print "The cpu showed you a picture from your gradeschool yearbook and you start to tremble\n"
    elif decision < .9:  #procrastinate
      print "Your thoughts start to trail and you find yourself watching so many funny cat videos that you forget to take your turn\n"
      self.cpu_choice()
      self.cpu_choice()
    else:  #suck in
      if self.your_health < 30 or self.cpu_anger > 15:
        print "You get sucked into a world of digital style\n"
        self.victory = False
        self.running = False
      else:
        print "Computer makes an odd sound, almost like it tried to inhale something...\n"
  #End cpu_choice 
    
  def win(self):
    print "Way to go!\nYou just beat the shit out of your Computer.\nToo bad you have to buy a new one"
    raw_input("Press enter to exit")
  #End win
  
  def lose(self):
    print "Death"
    raw_input("Press enter to exit")
  #End lose
    
def main():
  fight = FightSimulation()
  fight.play()
  
if __name__ == '__main__':
  main()
  exit()