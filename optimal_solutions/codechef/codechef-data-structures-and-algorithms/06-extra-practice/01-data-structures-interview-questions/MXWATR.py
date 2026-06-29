


def solve():
    T = int(input())
    def max_vol(H):
        if len(H) < 3:
            return 0
        max_height = 0
        cur_vol = 0
        max_vol = 0
        for h in H:
            if h >= max_height:
                max_height = h 
                max_vol = max(max_vol, cur_vol)
                cur_vol = 0 
            else:
                cur_vol += max_height - h
        return max_vol
    for t in range(T):
        N = int(input())
        H = list(map(int,input().split()))
        h_max = max(H)
        h_max_ind = H.index(h_max)
        H_left = H[:h_max_ind+1]
        H_right = H[h_max_ind:]
        H_right.reverse()
        max_left = max_vol(H_left)
        max_right = max_vol(H_right)
        print(max(max_left, max_right))


if __name__ == "__main__":
    solve()
