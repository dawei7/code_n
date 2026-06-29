


def solve():
    t = int(input())
    for i in range(t):
    	N=int(input())
    	sta=input().strip()
    	stb=input().strip()
    	if sta==stb:
    		r='YES'
    	else:
    		sta+='1'
    		p=0
    		while sta[p]=='0':
    			p+=1

    		if p==N:
    			r='NO'
    		else:
    			stb+='00'
    			p=1
    			while stb[p]!=stb[p-1]:
    				p+=1
    			if p<N:
    				r='YES'
    			else:
    				r='NO'
    	print (r)


if __name__ == "__main__":
    solve()
