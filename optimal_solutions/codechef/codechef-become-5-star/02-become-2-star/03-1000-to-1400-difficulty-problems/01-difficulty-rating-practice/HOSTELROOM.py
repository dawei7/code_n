import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, x = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        current_people = x
        max_people = x
        for event in a:
            current_people += event
            if current_people > max_people:
                max_people = current_people
        print(max_people)


if __name__ == "__main__":
    solve()
