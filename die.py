class Die(object):
    def __init__(self, sides = 6, fair = True):
        self.sides = sides
        self.fairness = 'fair'

    def roll(self):
        return randint(1, self.sides)


class CrapsDice( Die ):
    """Extends Dice to add features specific to Craps."""
    def hardways( self ):
        """Returns True if this was a hardways roll?"""
        return self.myDice[0].value == self.myDice[1].value
    def isPoint( self, value ):
        """Returns True if this roll has the given total"""
        return self.getTotal() == value