


def solve():
    def is_isomorphic(s, t):
        if len(s) != len(t):
            return False

        map_st = {}
        map_ts = {}

        for c1, c2 in zip(s, t):
            # Check mapping s -> t
            if c1 in map_st:
                if map_st[c1] != c2:
                    return False
            else:
                map_st[c1] = c2

            # Check mapping t -> s
            if c2 in map_ts:
                if map_ts[c2] != c1:
                    return False
            else:
                map_ts[c2] = c1

        return True


if __name__ == "__main__":
    solve()
