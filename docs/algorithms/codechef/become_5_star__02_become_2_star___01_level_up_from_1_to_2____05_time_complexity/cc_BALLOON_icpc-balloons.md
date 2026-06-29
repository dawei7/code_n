# ICPC Balloons

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BALLOON |
| Difficulty Rating | 1205 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Arrays |
| Official Link | [BALLOON](https://www.codechef.com/practice/course/1to2stars/LP1TO202/problems/BALLOON) |

---

## Problem Statement

Chef is participating in an ICPC regional contest, in which there is a total of $N$ problems (numbered $1$ through $N$) with varying difficulties. For each valid $i$, the $i$-th easiest problem is problem $A_i$.

After a team solves a problem, a balloon with a colour representing that problem is tied next to their desk. Chef is fond of colours in **VIBGYOR**, which are representative of the problems with numbers $1$ through $7$. The remaining problems have their own representative colours too.

Find the minimum number of problems which Chef's team needs to solve in order to get all the balloons for problems $1$ through $7$ (and possibly some other balloons too) tied next to their desk, if you know that Chef's team knows the difficulties of all problems and solves the problems in increasing order of difficulty.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

### Output
For each test case, print a single line containing one integer ― the minimum number of problems Chef's team needs to solve.

### Constraints
- $1 \leq T \leq 10,500$
- $7 \leq N \leq 15$
- $1 \leq A_i \leq N$ for each valid $i$
- $A_1, A_2, \ldots, A_N$ are pairwise distinct

---

## Examples

**Example 1**

**Input**

```text
3
7
1 2 3 4 5 7 6
8
8 7 6 5 4 3 2 1
9
7 4 3 5 6 1 8 2 9
```

**Output**

```text
7
8
8
```

**Explanation**

**Example case 1:** Since there are a total of $7$ problems, Chef's team will have to solve all of them.

**Example case 2:** Problems $1$ through $7$ appear among the first $8$ problems.

**Example case 3:** Problems $1$ through $7$ again appear among the first $8$ problems.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
7
1 2 3 4 5 7 6
```

**Output for this case**

```text
7
```



#### Test case 2

**Input for this case**

```text
8
8 7 6 5 4 3 2 1
```

**Output for this case**

```text
8
```



#### Test case 3

**Input for this case**

```text
9
7 4 3 5 6 1 8 2 9
```

**Output for this case**

```text
8
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/COOK130A/problems/BALLOON)

[Contest Division 2](https://www.codechef.com/COOK130B/problems/BALLOON)

[Contest Division 3](https://www.codechef.com/COOK130C/problems/BALLOON)

[Practice](https://www.codechef.com/problems/BALLOON)

**Setter:** [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

**Tester & Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

# DIFFICULTY

Cakewalk

# PREREQUISITES

None

# PROBLEM

Given N problems in a contest given in the increasing order of difficulty, whose ids are given in sequence A. The team solves the problems in the order of difficulty. Find the minimum number of problems to be solved such that all problems with id in the range [1, 7] are solved.

# QUICK EXPLANATION

The minimum number of problems to be solved is the maximum among positions of any problem with difficulty in the range [1, 7].

# EXPLANATION

We need to solve all problems with ids in the range [1, 7] and we want to solve the minimum number of problems. We can solve problems only in increasing order of difficulty.

### Method 1

Since we can only solve the problems in one order, let’s keep solving the problem until we have solved all problems with ids in the range [1, 7] and stop. i.e. Let’s solve the problem one by one, and after solving each problem, check if we solved all problems with ids in the range [1, 7]. If yes, terminate, otherwise, we proceed to solve the next problem.

We’d need to keep a set of solved problems, and checking if all problems in the range are solved by looping over problem ids in the range [1,7] and checking if all of them are present. When a problem is solved, its id is added to the set.

This sikytuib works in O(N*log(N)) time.

### Method 2

Let’s start from the end. Assume we have solved all problems. Now, try reducing the number of solved problems, by leaving problems with the highest difficulty unsolved one by one. When, the problem with the highest difficulty has an id in the range [1, 7], we can no more delete a problem, so the minimum number of problems to be solved is N less the number of problems left unsolved.

This solution can be implemented by a pointer starting from the right end, and moving towards the left one step at a time until it reaches a problem with id in the range [1, 7].

The time complexity of this solution is O(N)

### Method 3

Find the positions of all problems, whose ids are in the range [1, 7]. Let’s say X is the maximum among those positions. Then we need to solve exactly X problems, as X is the minimum number of problems, such that by solving the first X problems, we solved all problems with ids in the range [1,7]

The time complexity of this approach is O(N) as well.

### Bonus

Let’s say you want to solve at least 6 problems with ids in the range [1, 7]. What is the minimum number of problems you must solve to achieve that, given you can solve the problems in the order of difficulty, and A_i denotes the id of ith problem

# TIME COMPLEXITY

The time complexity is O(N) or O(N*log(N)) per test case depending upon implementation.

# SOLUTIONS

Setter's Solution
``#include<bits/stdc++.h>
# define pb push_back
#define pii pair<int, int>
#define mp make_pair
# define ll long long int

using namespace std;

const int maxn = 15, maxtn = 1e5;
bool inc[16];
int cnt[16];
int main()
{
    int t, n, x; cin >> t;
    int tn = 0;
    while(t--){
        cin >> n;
        tn += n;
        memset(inc, false, sizeof(inc));
        int mask = 0, rmask = (1 << 7) - 1;
        bool found = false;
        for(int i = 1; i <= n; i++){
            cin >> x;
            assert(!inc[x]); inc[x] = true;
            if(found)continue;
            mask |= (1 << (x - 1));
            if((mask & rmask) == rmask){
                cout << i << endl;
                cnt[i]++;
                found = true;
            }
        }
    }
}
``

Tester's Solution
``#include <iostream>
#include <assert.h>
#include <algorithm>
#include <vector>
#include <set>
#include <string>
#include <queue>
#include <map>
using namespace std;

long long readInt(long long l,long long r,char endd){
    long long x=0;
    int cnt=0;
    int fi=-1;
    bool is_neg=false;
    while(true){
	    char g=getchar();
	    if(g=='-'){
		    assert(fi==-1);
		    is_neg=true;
		    continue;
	    }
	    if('0'<=g && g<='9'){
		    x*=10;
		    x+=g-'0';
		    if(cnt==0){
			    fi=g-'0';
		    }
		    cnt++;
		    assert(fi!=0 || cnt==1);
		    assert(fi!=0 || is_neg==false);

		    assert(!(cnt>19 || ( cnt==19 && fi>1) ));
	    } else if(g==endd){
		    if(is_neg){
			    x= -x;
		    }
		    assert(l<=x && x<=r);
		    return x;
	    } else {
		    assert(false);
	    }
    }
}
string readString(int l,int r,char endd){
    string ret="";
    int cnt=0;
    while(true){
	    char g=getchar();
	    assert(g!=-1);
	    if(g==endd){
		    break;
	    }
	    cnt++;
	    ret+=g;
    }
    assert(l<=cnt && cnt<=r);
    return ret;
}
long long readIntSp(long long l,long long r){
    return readInt(l,r,' ');
}
long long readIntLn(long long l,long long r){
    return readInt(l,r,'\n');
}
string readStringLn(int l,int r){
    return readString(l,r,'\n');
}
string readStringSp(int l,int r){
    return readString(l,r,' ');
}

int main(){
    int T = readIntLn(1, 10500);
    while(T-->0){
        int N = readIntLn(7, 15);
        vector<int> A;
        int ans = -1;
        for(int i = 1; i<= N; i++){
            int x;
            if(i+1 <= N)x = readIntSp(1, N);
            else x = readIntLn(1, N);
            A.push_back(x);
            if(x <= 7)ans = i;
        }
        sort(A.begin(), A.end());
        for(int i = 0; i< N; i++)assert(A[i] == i+1);
        cout<<ans<<endl;
    }
    assert(getchar()==-1);
    cerr<<"SUCCESS\n";
}
``

Feel free to share your approach. Suggestions are welcomed as always.

</details>
