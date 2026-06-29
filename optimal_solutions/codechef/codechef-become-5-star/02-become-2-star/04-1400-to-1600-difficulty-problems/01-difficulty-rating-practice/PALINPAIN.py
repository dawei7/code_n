# cook your dish here
# cook your dish here


def solve():
    for _ in range(int(input())):
        x,y=map(int,input().split());
        if(x%2==1 and y%2==1 or x==1 or y==1):
            print(-1);
        elif(x%2==0 and y%2==0):
            print('a'*(x//2)+'b'*y+'a'*(x//2));
            print('b'*(y//2)+'a'*x+'b'*(y//2));
        elif(x%2!=0 and y%2==0):
            print('b'*(y//2)+'a'*x+'b'*(y//2));
            print('a'*(x//2)+'b'*(y//2)+'a'+'b'*(y//2)+'a'*(x//2));
        elif(x%2==0 and y%2!=0):
            print('a'*(x//2)+'b'*y+'a'*(x//2));
            print('b'*(y//2)+'a'*(x//2)+'b'+'a'*(x//2)+'b'*(y//2));


if __name__ == "__main__":
    solve()
