#File 2 (BowlingGame.py)
#This file has information about Bowling Game for which the description is provided in project assessment.

class BowlingGame:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        """Append scores to list

        Args:
            pins (int): Number of pins knocked down by the ball (score)

        Returns:
            appends the rolls to the self.rolls list
        """
        self.rolls.append(pins)

    def score(self):
        """Calculates the score - checks if is strike, then if spare or adds two scores within frame

        Args:
            self.rolls (list): the player's score represented by values in the list

        Returns: 
            result (int): the results of the total score
        """
        result = 0
        rollIndex = 0
        for frameIndex in range(10):
            # if roll is a 10 then it is a strike and play would move to the next frame so rollIndex increases by 1
            if self.isStrike(rollIndex): 
                result += self.calculateStrikeScore(rollIndex) # re-named to calculateStrikeScore (there was a spelling error)
                rollIndex += 1 
            # if roll is not 10 then check if this roll + the next roll = spare, rollIndex increases by 2
            elif self.isSpare(rollIndex):
                result += self.calculateSpareScore(rollIndex)
                rollIndex += 2 
            # finally, if roll is not spare then add this roll to the next and move to next frame, rollIndex increases by 2
            else:
                result += self.calculateFrameScore(rollIndex)
                rollIndex += 2 
        return result

    def isStrike(self, rollIndex):
        """Determine if roll is a strike
        
        Args: 
            rollIndex (int): the index of the roll to check

        Returns:
            boolean: If the roll score is 10 then true

        """
        return self.rolls[rollIndex] == 10
    
    def isSpare(self, rollIndex):
        """Determine if a frame is a spare

        Args: 
            rollIndex (int): the index of the roll to check

        Returns:
            boolean: If the roll and the following roll add to 10 return true
        """
        return self.rolls[rollIndex] + self.rolls[rollIndex+1] == 10
    
    def calculateStrikeScore(self, rollIndex): # re-named to calculateStrikeScore (there was a spelling error)
        """Calculate strike score
        
        Args: 
            rollIndex (int): the index of the roll to check

        Returns:
            int: returns the score of the strike, 10 + the following 2 rolls
        """
        return  10 + self.rolls[rollIndex + 1] + self.rolls[rollIndex + 2]

    def calculateSpareScore(self, rollIndex):
        """Calculate spare score
        
        Args: 
            rollIndex (int): the index of the roll to check

        Returns:
            int: returns the score of the spare, 10 + the following roll
        """
        return  10 + self.rolls[rollIndex + 2]

    def calculateFrameScore(self, rollIndex):
        """Calculate frame score
        
        Args: 
            rollIndex (int): the index of the roll to check

        Returns:
            int: returns the score of the frame
        """
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]