#File 2 (BowlingGame.py)
#This file has information about Bowling Game for which the description is provided in project assessment.

class BowlingGame:
    def __init__(self):
        self.rolls=[]

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        [10,0,4,3]
        result = 0
        rollIndex = 0
        for frameIndex in range(10):
            if self.isStrike(rollIndex):
                result += self.strikeScore(rollIndex) # re-named to strikeScore (there was a spelling error)
                self.rolls.insert(rollIndex + 1, 0) # If the roll is a strike, then add the next 'roll' as 0
                rollIndex +=2 # every loop checks the whole 'frame' which is every 2 'rollIndex' values 
            elif self.isSpare(rollIndex):
                result += self.spareScore(rollIndex)
                rollIndex +=2 # changed to 2
            else:
                result += self.frameScore(rollIndex)
                rollIndex +=2 # changed to 2
        return result

    def isStrike(self, rollIndex):
        return self.rolls[rollIndex] == 10
    
    def isSpare(self, rollIndex):
            return self.rolls[rollIndex] + self.rolls[rollIndex+1] == 10
    
    def strikeScore(self, rollIndex): # re-named to strikeScore (there was a spelling error)
        return  10 + self.rolls[rollIndex+1] + self.rolls[rollIndex+2]

    def spareScore(self,rollIndex):
        return  10 + self.rolls[rollIndex+2]

    def frameScore(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]
		

#Your tasks for code parts:
#1: If there are any bugs in the code, you have to remove using debugging and run the project and test cases.
#2: Refactor the code (Improve its structure without changing external behaviour).
#3: Report everything using github commits and versioning control.


###### Important #####
# Please complete your project and all tasks according to assessment description provided in CANVAS.