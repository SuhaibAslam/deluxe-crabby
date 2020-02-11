class Mark:
    EMPTY = 0  # Nothing's happening at this location
    MOLE = 1  # A mole has popped up here
    TOUCH = 2  # The player has touched this field recemment
    HIT = 3  # The player touched this field while the mole was there

    def __init__(self):
        self.mark = self.EMPTY

    def __repr__(self):
        if self.mark == 0:
            return 'EMPTY'
        elif self.mark == 1:
            return 'MOLE'
        elif self.mark == 2:
            return 'TOUCH'
        elif self.mark == 3:
            return 'HIT'
        else:
            return 'NONE'
