def solve():
    T = int(input())
    while T > 0:
        check_weight()
        T-=1
        
def check_weight():
    w1, w2, x1, x2, M = map(int, input().split())
    result = 0
    min_limit = (x1 * M)
    max_limit = (x2 * M)
    weight_diff = (w2 - w1)
    if weight_diff < min_limit:
        print (result)
    elif ((weight_diff == min_limit) or (weight_diff == max_limit) or ((weight_diff > min_limit) and (weight_diff < max_limit))):
        result = 1
        print (result)
    elif weight_diff > max_limit:
        print (result)

main()


if __name__ == "__main__":
    solve()
