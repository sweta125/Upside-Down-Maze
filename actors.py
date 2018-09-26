"""This file has the classes for all the 'actors' in the game: Survivors and
Enemies. Both inherit from MazePerson. A Survivor is a MazePerson with a fluctuating
health. An Enemy is a MazePerson with an attackPower. The main game dictates
how Enemies attack Survivors, and how the Survivors' health fluctuates; this is not
defined in their class methods."""

class MazePerson(object):
    def __init__(self, userR, userC, name):
        self.userR = userR
        self.userC = userC
        self.name = name
    
    def setUserR(self, row): self.userR = row
    
    def setUserC(self, col): self.userC = col
    
    def getUserR(self): return self.userR
    
    def getUserC(self): return self.userC
    
    def __repr__(self):
        return "Person is at userR: %d and userC: %d" % (self.userR, self.userC)
    
    def __eq__(self, other):
        return (isinstance(other, MazePerson) and self.userR==other.userR and \
        self.userC==other.userC and self.name==other.name)
    
class Survivor(MazePerson):
    def __init__(self, userR, userC, name, health):
        super().__init__(userR, userC, name)
        self.health = health
        self.initialHealth = health
    
    def __eq__(self, other):
        return (isinstance(other, Survivor) and self.userR==other.userR and \
        self.userC==other.userC and self.name==other.name and \
        self.health==other.health)
    
    def getUserHealth(self): return self.health
    
    def getInitialHealth(self): return self.initialHealth
    
    def setUserHealth(self, h): 
        if self.health > self.initialHealth:
            self.health = self.initialHealth
        elif self.health < 0:
            self.health = 0
        else: self.health = h
    
class Enemy(MazePerson):
    def __init__(self, userR, userC, name, attackPower):
        super().__init__(userR, userC, name)
        self.attackPower=attackPower
    
    def getAttackPower(self): return self.attackPower
    
    def __eq__(self, other):
        return (isinstance(other, Enemy) and self.userR==other.userR and \
        self.userC==other.userC and self.name==other.name and \
        self.attackPower==other.attackPower)