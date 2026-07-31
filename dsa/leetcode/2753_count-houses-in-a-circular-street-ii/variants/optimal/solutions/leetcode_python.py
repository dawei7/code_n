class Solution:
    def houseCount(self, street: Optional['Street'], k: int) -> int:
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

