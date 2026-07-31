class Street:
    """Local equivalent of LeetCode's restricted Street interface."""

    def __init__(self, doors):
        self._doors = [bool(value) for value in doors]
        self._position = 0

    def closeDoor(self):
        self._doors[self._position] = False

    def isDoorOpen(self):
        return self._doors[self._position]

    def moveRight(self):
        self._position = (self._position + 1) % len(self._doors)


def solve(street: Street, k: int) -> int:
    found_first = False
    first_open_step = 0
    answer = 0

    for step in range(2 * k):
        if street.isDoorOpen():
            if not found_first:
                found_first = True
                first_open_step = step
            else:
                answer = step - first_open_step
                street.closeDoor()
        street.moveRight()

    return answer
