from collections import deque


def solve():
    t = int(input())  # Number of test cases 

    for _ in range(t):
        n, k = map(int, input().split())  # Number of pearls, Number of positions to move

        necklace = deque()

        # Enqueue the elements (pearls) into the queue
        pearls = list(map(int, input().split()))
        necklace.extend(pearls)

        # Rotate the queue left by k positions
        for _ in range(k):
            removed = necklace.popleft()
            necklace.append(removed)

        # Print the modified necklace
        print(" ".join(map(str, necklace)))


if __name__ == "__main__":
    solve()
