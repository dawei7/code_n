


def solve():
    def LongestSubstring(string):
        n = len(string)
        stk = []
        stk.append(-1)
        result = 0
        for i in range(n):
            if string[i] == '(':
                stk.append(i)
            else:
                if len(stk) != 0:
                    stk.pop()
                if len(stk) != 0:
                    result = max(result,i - stk[len(stk)-1])
                else:
                    stk.append(i)

        return result

    t = int(input())
    while t>0:
        s = str(input())
        s = " " + s
        q = int(input())
        while q>0:
            l,r = map(int, input().split())
            length = LongestSubstring(s[l:r+1])
            print(length, end=" ")
            q -= 1
        print()
        t -= 1


if __name__ == "__main__":
    solve()
