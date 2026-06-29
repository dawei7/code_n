from collections import deque
import sys


def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        exit()
    t = int(input_data[0])
    index = 1
    res = []
    for _ in range(t):
        n = int(input_data[index])
        index += 1
        arr = list(map(int, input_data[index:index+n]))
        index += n
        dq = deque(arr)
        # Aman is represented as 1, Akshat as 0, starting with Aman.
        turn = 1
        last_person = None
        # Continue until only one stone left.
        while len(dq) > 1:
            if turn == 1:  # Aman's turn
                # Move 1: remove top and put to bottom.
                if len(dq) <= 1:
                    break
                dq.append(dq.popleft())
                # Move 2: if still >1, remove stone from top.
                if len(dq) <= 1:
                    break
                dq.popleft()
                last_person = 1
            else:  # Akshat's turn
                # Move 1: do two rotations.
                for _ in range(2):
                    if len(dq) <= 1:
                        break
                    dq.append(dq.popleft())
                if len(dq) <= 1:
                    break
                # Move 2: remove stone from top.
                dq.popleft()
                last_person = 0
            turn = 1 - turn
        # Last stone value in dq[0].
        res.append(f"{last_person} {dq[0]}")
    sys.stdout.write("\n".join(res))


if __name__ == "__main__":
    solve()
