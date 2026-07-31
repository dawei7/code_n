class _Street:
    """Local adapter for the interactive circular-street interface."""

    def __init__(self, doors):
        self._doors = [bool(value) for value in doors]
        self._position = 0

    def openDoor(self):
        self._doors[self._position] = True

    def closeDoor(self):
        self._doors[self._position] = False

    def isDoorOpen(self):
        return self._doors[self._position]

    def moveRight(self):
        self._position = (self._position + 1) % len(self._doors)

    def moveLeft(self):
        self._position = (self._position - 1) % len(self._doors)


def solve(street, k):
    street = _Street(street)

    for _ in range(k):
        street.closeDoor()
        street.moveRight()

    street.openDoor()
    houses = 0
    while True:
        street.moveRight()
        houses += 1
        if street.isDoorOpen():
            return houses
