


def solve():
    class Solution:
        def floorAndCeil(self, root, key):
            floor_val, ceil_val = -1, -1
            curr = root

            # Find floor
            while curr:
                if curr.val == key:
                    floor_val = curr.val
                    break
                elif curr.val > key:
                    curr = curr.left
                else:
                    floor_val = curr.val
                    curr = curr.right

            curr = root  # reset for ceil

            # Find ceil
            while curr:
                if curr.val == key:
                    ceil_val = curr.val
                    break
                elif curr.val < key:
                    curr = curr.right
                else:
                    ceil_val = curr.val
                    curr = curr.left

            return floor_val, ceil_val


if __name__ == "__main__":
    solve()
