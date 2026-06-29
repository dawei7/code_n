# cook your dish here


def solve():
    def check_palindrome(s, n):
        if(n>len(s)//2):
            return "Yes"
        if(s[n]!=s[len(s)-n-1]):
            return "No"
        return check_palindrome(s, n+1)

    s = input()
    print(check_palindrome(s, 0))


if __name__ == "__main__":
    solve()
