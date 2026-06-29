def solve():
    T = int(input())
    
    for _ in range(T):
        n = int(input())
        V = list(map(int, input().split()))
        
        V.sort(reverse=True)
        
        max1, max2 = 0, 0
        i = 0
        
        # Find the first pair of equal sticks
        while i < n - 1:
            if V[i] == V[i + 1]:
                max1 = V[i]
                i += 2
                break
            i += 1
        
        # Find the second pair of equal sticks
        while i < n - 1:
            if V[i] == V[i + 1]:
                max2 = V[i]
                i += 2
                break
            i += 1
        
        if max1 > 0 and max2 > 0:
            print(max1 * max2)
        else:
            print(-1)

solve()


if __name__ == "__main__":
    solve()
