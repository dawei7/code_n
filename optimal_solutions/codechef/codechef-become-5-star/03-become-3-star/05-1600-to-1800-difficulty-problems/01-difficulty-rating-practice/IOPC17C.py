def solve():
    n = int(input())
    v = list(map(int, input().split()))
    
    v.sort()
    j = n - 2
    
    while j >= 0 and v[j] == v[n - 1]:
        j -= 1
        
    if j < 0:
        print(0)
    else:
        print(v[j])

t = int(input())
for _ in range(t):
    solve()


if __name__ == "__main__":
    solve()
