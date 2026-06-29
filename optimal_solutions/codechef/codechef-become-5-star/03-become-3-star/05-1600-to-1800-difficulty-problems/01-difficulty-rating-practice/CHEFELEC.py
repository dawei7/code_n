# www.codechef.com/problems/CHEFELEC


def solve():
    def wire_needed(conn_mask, coords):
        wire_total = 0
        dark_patch = False 
        last = -coords[-1]
        for conn, pos in zip(conn_mask, coords):
            if dark_patch:
                patch.append(pos)
                max_gap = max(max_gap, pos - last)
                if conn == "1":
                    wire_total += patch[-1] - patch[0] - max_gap
                    dark_patch = False
            elif conn == "0":
                patch = [last, pos]
                max_gap = pos - last
                dark_patch = True
            last = pos
        if dark_patch:
            wire_total += patch[-1] - patch[0]

        return wire_total



    # ======================= #

    from sys import stdin
    if __name__ == "__main__":
        T = int(stdin.readline())
        for _ in range(T):
            N = int(stdin.readline())
            connected = input().strip()
            position = list(map(int, stdin.readline().split()))
            print(wire_needed(connected, position))


if __name__ == "__main__":
    solve()
