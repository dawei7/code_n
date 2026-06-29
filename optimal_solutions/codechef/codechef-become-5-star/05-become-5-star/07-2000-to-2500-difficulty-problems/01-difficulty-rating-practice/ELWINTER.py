# cook your dish here
# cook your dish here


def solve():
    N,M,Q = map(int,input().split())
    adjacency_mtx=[]
    for _ in range(N):
        adjacency_mtx.append([])
    for _ in range(M):
        u,v=input().split()
        adjacency_mtx[int(u)-1].append(int(v)-1)
        adjacency_mtx[int(v)-1].append(int(u)-1)
    frozen=[-1]*N
    time=0
    for _ in range(Q):
        query,param=map(int,input().split())
        if query==1:
            if frozen[param-1]==-1 or frozen[param-1]>time:
                frozen[param-1]=time
                t=time+1
                temp_prev=[param-1]
                while len(temp_prev)!=0:
                    temp_new=[]
                    for i in temp_prev:
                        for j in adjacency_mtx[i]:
                            if frozen[j]==-1 or frozen[j]>t:
                                frozen[j]=t
                                temp_new.append(j)
                    t+=1
                    temp_prev=temp_new
        elif query==2:
            time+=param
        else:
            if time>=frozen[param-1]:
                print('YES')
            else:
                print('NO')


if __name__ == "__main__":
    solve()
