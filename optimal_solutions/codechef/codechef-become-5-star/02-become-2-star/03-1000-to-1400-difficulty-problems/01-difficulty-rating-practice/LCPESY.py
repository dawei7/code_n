from collections import Counter


def solve():
    for t in range(int(input())):
        a=input()
        b=input()
        s=a+b
        q=0
        dict1=Counter(a)
        dict2=Counter(b)
        for i in dict1.keys():
            for j in dict2.keys():
                if i==j:
                    q+=min(dict1[i],dict2[j])
        print(q)


if __name__ == "__main__":
    solve()
