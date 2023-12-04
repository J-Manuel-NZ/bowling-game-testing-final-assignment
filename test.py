#File 1 (Test.py)
#This file has information about test cases which you need to test.

import unittest
import BowlingGame

class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame.BowlingGame()

    def testGutterGame(self):
        for i in range(0, 20):
            self.game.roll(0)
        assert self.game.score() == 0

    def testAllOnes(self):
        self.rollMany(1, 20)
        assert self.game.score() == 20

    def testOneSpare(self):
        self.game.roll(2)
        self.game.roll(8)
        self.game.roll(3)
        self.rollMany(0,17)
        assert self.game.score() == 16

    def testOneStrike(self):
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.rollMany(0,17)
        assert  self.game.score() == 24
    
    def testTwoStrikes(self):
        self.game.roll(10)
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(2)
        self.rollMany(0,14)
        assert self.game.score() == 46
    
    def testTwoSpares(self):
        self.game.roll(2)
        self.game.roll(8)
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.rollMany(0,15)
        assert self.game.score() == 31

    def testPerfectGame(self):
        self.rollMany(10,12)
        assert self.game.score() == 300

    def testAllSpares(self):
        self.rollMany(5,21)
        assert self.game.score() == 150

    def rollMany(self, pins, rolls):
        for i in range(rolls):
            self.game.roll(pins)