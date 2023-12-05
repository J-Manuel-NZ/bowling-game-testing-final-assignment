#File 1 (Test.py)
#This file has information about test cases which you need to test.

import unittest
import BowlingGame

class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        """Initalises the bowling game class"""
        self.game = BowlingGame.BowlingGame()

    def testGutterGame(self):
        """Tests if all balls rolled are gutterballs"""
        for i in range(0, 20):
            self.game.roll(0)
        assert self.game.score() == 0

    def testAllOnes(self):
        """Tests if player scores only ones"""
        self.rollMany(1, 20)
        assert self.game.score() == 20

    def testOneSpare(self):
        """Tests if player scores one spare followed by a 3"""
        self.game.roll(2)
        self.game.roll(8)
        self.game.roll(3)
        self.rollMany(0,17)
        assert self.game.score() == 16

    def testOneStrike(self):
        """Tests if player scores one strike followed by a 4 and 3"""
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.rollMany(0,17)
        assert  self.game.score() == 24
    
    def testTwoStrikes(self):
        """Tests if player scores two strikes followed by a 4 and 2"""
        self.game.roll(10)
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(2)
        self.rollMany(0,14)
        assert self.game.score() == 46
    
    def testTwoSpares(self):
        """Tests if player scores two spares followed by a 3"""
        self.game.roll(2)
        self.game.roll(8)
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.rollMany(0,15)
        assert self.game.score() == 31

    def testPerfectGame(self):
        """Tests if player scores all strikes + 2 bonus balls (a perfect game)"""
        self.rollMany(10,12)
        assert self.game.score() == 300

    def testAllSpares(self):
        """Tests if player scores all spares + one bonus ball"""
        self.rollMany(5,21)
        assert self.game.score() == 150

    def rollMany(self, pins, rolls):
        """Adds many rolls to the score list
        
        Args:
            pins (int): the score of each roll
            rolls (int): the amount of rolls to add to the list
            
        Returns:
            appends the rolls to the self.game.rolls list
        """
        for i in range(rolls):
            self.game.roll(pins)