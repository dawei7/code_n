# cook your dish here


def solve():
    def eat(n,m):
        dict1={}
        for _ in range(n):
            d,v=map(int,input().split())
            if d not in dict1:
                dict1[d]=v
            elif d in dict1 and v>dict1[d]:
                dict1[d]=v
        values=dict1.values()
        sorted_values=sorted(values,reverse=True)
        return (sorted_values[0]+sorted_values[1])

    for _ in range(int(input())):
        dict1={}
        n,m=map(int,input().split())
        k=eat(n,m)
        print(k)


if __name__ == "__main__":
    solve()
