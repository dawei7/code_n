# Full Barrier Alchemist

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PIPSQUIK |
| Difficulty Rating | 1426 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [PIPSQUIK](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/PIPSQUIK) |

---

## Problem Statement

Edward Elric is chasing after Scar. To stop Edward, Scar creates $N$ barriers in the way, numbered from $1$ to $N$.
Each barrier Scar created is either one of the following two types.
- Type 1 barrier - This barrier starts from a height $X$ above the ground and extends till the sky.
- Type 2 barrier - This barrier starts from the ground and extends up to height $X$ above the ground.

The height of Edward is $H$ units and he has an alchemic life force of $L$ units. Moreover, he can duck by $Y_{1}$ units and jump by height $Y_{2}$ units (as explained in the figures). He starts crossing barriers in sequence, starting from barrier $1$ till the barrier $N$. Whenever he can't pass a barrier by ducking or jumping (considered passed even when the barrier just touches him), he uses Alchemy to break the barrier. However, this costs him a single unit of his alchemic life force.

If after breaking a barrier no life force is left, Edward gets completely exhausted, unable to pass that barrier.
How many barriers can Edward cross?

And remember never to call him a pipsqueak if his height is too short!

### Input:

- The first line contains $T$, the number of test cases. Then the test cases follow.
- For each test case, the first line contains five integers $N$, $H$, $Y_{1}$, $Y_{2}$ and $L$.
- The i-th of the next $N$ lines contains two integers $t_{i}$ and $X_{i}$ for the $i^{th}$ barrier where $t_{i} = 1$ denotes a Type 1 Barrier and $t_{i} = 2$ denotes a Type 2 barrier.

### Output:
For each test case print a single line containing the number of barriers Edward can pass.

### Constraints
- $1 \leq T\leq 100$
- $1 \leq N\leq 10^{3}$
- $2 \leq H\leq 10^{3}$
- $1 \leq Y_{1} < H$
- $1 \leq Y_{2} \leq 10^{3}$
- $1 \leq L \leq N$
- $1 \leq t_{i} \leq 2$
- $1 \leq X_{i}\leq 10^{3}$

---

## Examples

**Example 1**

**Input**

```text
3
6 5 1 2 3
2 2
2 1
1 10
2 8
2 4
1 2
1 4 2 5 1
2 6
6 5 1 2 3
2 2
2 1
1 10
2 8
2 4
1 6
```

**Output**

```text
5
0
6
```

**Explanation**

**Test Case 1:**

Given $N = 6$, $H = 5$, $Y_{1} = 1$, $Y_{2} = 2$ and $L = 3$.
He passes the first three barriers by either ducking or jumping. He uses alchemic life force for breaking $4^{th}$, $5^{th}$ and $6^{th}$ barriers because he cannot pass them by either jumping or ducking. He gets exhausted after breaking the $6^{th}$ barrier and is unable to pass it. So, in total he passes $5$ barriers.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

[Practice](https://www.codechef.com/problems/PIPSQUIK)

[Contest: Division 1](https://www.codechef.com/DCOD19A/problems/PIPSQUIK)

[Contest: Division 2](https://www.codechef.com/DCOD19B/problems/PIPSQUIK)

*Author:* [Sachin Yadav](https://www.codechef.com/users/sachin_yadav)

*Tester:* [Vraj Patel](https://www.codechef.com/users/alphatron99)

*Editorialist:* [Nishikant Parmar](https://www.codechef.com/users/niksparmar)

## DIFFICULTY:

CAKEWALK

## PREREQUISITES:

Simple conditional operators

## PROBLEM:

There is a man of height H. He can duck by Y_{1}  and jump by Y_{2}. There are barriers of two types namely t= 1 and t  = 2. The barriers of type 1 start from a height X above the ground while the barriers of type 2 start from the ground and extend up to the height X above the ground. (Refer to the figure given in problem for better understanding )

He has life L and every time he can’t pass a barrier by bending or jumping he smashes into the barrier, breaking it, which costs him a single life and the barrier is considered passed. He can pass the barrier even if the barrier merely touches him on bending or jumping.

If after breaking a barrier no life is left, the man dies immediately, unable to pass that barrier.

How many barriers can he cross before dying finally?

## QUICK EXPLANATION:

For each barrier, we look for condition in which man can pass it and decrease the life count if he can not pass. As soon as life becomes zero we stop traversing.

## EXPLANATION:

This problem can be solved by traversing through the barriers one-by-one and checking the given conditions.

**Case 1** : When t = 1

Since the barrier starts from a height X above the ground, the man can cross the barrier only if his height is less than or equal to X, the minimum height the man can achieve is H-Y_{1}, so if his minimum height is more than X then decrease the life by 1.

**Case 2**: When t = 2

Since the barrier extends up to a height X from the ground; the man can cross the barrier only if he jumps a height more than or equal to X. Thus, if Y_{2} is less than X, then decrease the life by 1.

While traversing the array if life becomes zero, then you should stop traversing. In the end, the answer is the number of barriers traversed.

Note: Do not count the barrier at which life becomes zero.

## TIME COMPLEXITY

O(N)

## SOLUTIONS:

Setter's Solution
``#include<iostream>
using namespace std;
int arr[1001], types[1001];
int main()
{
    int T; cin>>T;
    while(T--)
    {
        int N,H, Y1, Y2, L; cin>>N>>H>>Y1>>Y2>>L;
        int count=0;
        for(int i=0; i<N; i++) cin>>types[i]>>arr[i];
        for(int i=0; i<N; i++)
        {
            if(types[i]==1 && arr[i]<H-Y1)
                --L;
            else if(types[i]==2 && arr[i]>Y2)
                --L;
            if(L==0) break;
            ++count;
        }
        cout<<count<<"\n";
    }
    return 0;
}
``

Tester's Solution
``for _ in range(int(input())):
	N,H,y1,y2,L = [int(i) for i in input().split()]
	barr_l = [[int(i) for i in input().split()] for j in range(N)]
	bc = 0
	for bt,x in barr_l:
		if(bt==1):
			if(x<H-y1):
				L-=1
		else:
			if(y2<x):
				L-=1
		if L>0:
			bc+=1
		if L<=0:
			break
	print(bc)
``

Editorialist's Solution
``T=int(input())
for k in range(T):
    N, H, Y1, Y2, L = map(int,input().split())
    barriers = [(0,0)]*N
    for i in range(N):
        t,X = map(int,input().split())
        barriers[i]=(t,X)
    ans = 0
    for j in range(N):
        t = barriers[j][0]
        X = barriers[j][1]
        if t==1:
            if H-Y1 > X:
                L = L - 1
        else:
            if Y2 < X:
                L = L - 1
        if L==0:
            break
        ans = ans + 1

    print(ans)

``

</details>
