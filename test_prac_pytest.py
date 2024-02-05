import pytest
import unittest.suite

class test_addition():
    def test_twoNo(self):
        self.x=10
        self.y=20
        return self.x+self.y

    def test_validate(self):
        assert self.x+self.y==30 is True