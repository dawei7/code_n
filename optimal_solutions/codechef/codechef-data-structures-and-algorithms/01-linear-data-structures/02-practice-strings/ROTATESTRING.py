


def solve():
    def can_rotate(s, goal):
        if len(s) != len(goal):
            return False
        doubled = s + s  # Concatenate s with itself
        return goal in doubled


if __name__ == "__main__":
    solve()
