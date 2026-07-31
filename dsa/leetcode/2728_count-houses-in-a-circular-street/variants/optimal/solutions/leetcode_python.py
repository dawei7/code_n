class Solution:
    def houseCount(self, street: Optional["Street"], k: int) -> int:
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
