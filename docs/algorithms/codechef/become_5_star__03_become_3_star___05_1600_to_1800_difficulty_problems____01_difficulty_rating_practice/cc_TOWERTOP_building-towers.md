# Building Towers

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TOWERTOP |
| Difficulty Rating | 1693 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [TOWERTOP](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/TOWERTOP) |

---

## Problem Statement

Chef is given a contract to build towers in Chefland which are made by stacking blocks one above the other. Initially, there is only $1$ block in the inventory and no tower has been built. Chef follows the following $2$ steps in each operation:

- Either build a new tower or update an existing tower that has been built in previous operations using **any** number of blocks currently present in the inventory. After this step, the size of the inventory reduces by the number of blocks used.
- Suppose the tower Chef updated or built has $B$ blocks **after the step**, Chef gets to add $B$ new blocks to the inventory as a reward.

Find the **maximum** number of towers of height $X$ that Chef can build in $M$ operations.

**Note:** Tower of height $X$ means that the tower consists of $X$ blocks placed one above the other.

---

## Input Format

- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains a single line of input, two space separated integers $X, M$.

---

## Output Format

For each test case, output a single integer, the maximum number of towers that Chef can build.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X \leq 10^9$
- $0 \leq M \leq 10^{17}$

---

## Examples

**Example 1**

**Input**

```text
4
2 1
2 2
2 3
53 7
```

**Output**

```text
0
1
2
1
```

**Explanation**

**Test Cases $1$, $2$ and $3$:**
- Operation $1$:
    - Remove $1$ block from the inventory and build a new tower of height $1$ after which the inventory becomes empty.
    - Add $1$ block to the inventory after which the inventory has only $1$ block.
- Operation $2$:
    - Remove $1$ block from the inventory and update the tower of height $1$ to $1 + 1 = 2$ after which the inventory becomes empty.
    - Add $2$ blocks to the inventory after which the inventory has only $2$ blocks.
- Operation $3$:
    - Remove $2$ blocks from the inventory and build a new tower of height $2$ after which the inventory becomes empty.
    - Add $2$ blocks to the inventory after which the inventory has only $2$ blocks.

So after operation $1$, there is no tower of height $2$ built, after operation $2$, there is a single tower of height $2$ built and after operation $3$, $2$ towers of height $2$ are built.

**Test Case $4$:**
- Operation $1$:
    - Remove $1$ block from the inventory and build a new tower of height $1$ after which the inventory becomes empty.
    - Add $1$ block to the inventory after which the inventory has only $1$ block.
- Operation $2$:
    - Remove $1$ block from the inventory and update the tower of height $1$ to $1 + 1 = 2$ after which the inventory becomes empty.
    - Add $2$ blocks to the inventory after which the inventory has only $2$ blocks.
- Operation $3$:
    - Remove $2$ blocks from the inventory and update the tower of height $2$ to $2 + 2 = 4$ after which the inventory becomes empty.
    - Add $4$ blocks to the inventory after which the inventory has only $4$ blocks.
- Operation $4$:
    - Remove $4$ blocks from the inventory and update the tower of height $4$ to $4 + 4 = 8$ after which the inventory becomes empty.
    - Add $8$ blocks to the inventory after which the inventory has only $8$ blocks.
- Operation $5$:
    - Remove $8$ blocks from the inventory and update the tower of height $8$ to $8 + 8 = 16$ after which the inventory becomes empty.
    - Add $16$ blocks to the inventory after which the inventory has only $16$ blocks.
- Operation $6$:
    - Remove $16$ blocks from the inventory and update the tower of height $16$ to $16 + 16 = 32$ after which the inventory becomes empty.
    - Add $32$ blocks to the inventory after which the inventory has only $32$ blocks.
- Operation $7$:
    - Remove $21$ blocks from the inventory and update the tower of height $32$ to $32 + 21 = 53$ after which the inventory has $32 - 21 = 11$ blocks remaining.
    - Add $53$ blocks to the inventory after which the inventory has $53 + 11 = 64$ blocks in total.

So after $7^{th}$ operation we are able to achieve one tower of height $53$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 1
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
2 2
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
2 3
```

**Output for this case**

```text
2
```



#### Test case 4

**Input for this case**

```text
53 7
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START25A/problems/TOWERTOP)

[Contest Division 2](https://www.codechef.com/START25B/problems/TOWERTOP)

[Contest Division 3](https://www.codechef.com/START25C/problems/TOWERTOP)

**Setter:** [Prakhar Kochar](https://www.codechef.com/users/prakhar_87)

**Tester:** [Tejas Pandey](https://www.codechef.com/users/tejas10p), [Abhinav Sharma](https://www.codechef.com/users/inov_360)

**Editorialist:** [Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

#
[](#difficulty-2)DIFFICULTY:

Easy

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef is given a contract to build towers in Chefland which are made by stacking blocks one above the other. Initially, there is only 1 block in the inventory and no tower has been built. Chef follows the following 2 steps in each operation:

- Step 1: Either build a new tower or update an existing tower that has been built in previous operations using the blocks currently present in the inventory. After this step, the size of the inventory reduces by the number of blocks used.

- Step 2: Suppose the tower Chef updated or built in Step 1 has B blocks after the step. Chef gets to add B new blocks to the inventory as a reward.

Find the maximum number of towers of height X Chef can build in M operations.

#
[](#quick-explanation-5)QUICK EXPLANATION:

- If M<(ceil(log_2(X))+1), the answer is 0.

- Else, we can build M-ceil(log_2(X)) towers of height X.

#
[](#explanation-6)EXPLANATION:

Observation

Note that the reward for an operation is equal to the number of blocks present in the last built or updated tower. To maximise this reward, it is optimal to update an existing tower instead of building a new one, since the former one would always have more blocks. If we keep updating the current tower, the reward increases exponentially.

Building a single tower of height X

Let us build the first tower of height X. We have 1 block initially. We use it to build a tower of height 1. We now get a reward of 1 block. If we update the current tower using this, the height of the tower becomes 2. After the reward for this move, the inventory size is also 2.

We continue using the whole inventory to build and update a single tower until it reaches the height X.

The inventory size forms a sequence while we do this process: 1, 1, 2, 4, 8, 16, 32, ….

Once the sum of this sequence reaches X, we have our first tower of height greater than equal to X.

Minimum operations required to reach the sum X can either be calculated using brute force (in O(log_2X) complexity) or using the formula (ceil(log_2(X))+1) (in O(1) complexity).

If the minimum operations required is greater than M, we cannot build even a single tower and the answer is 0.

Building maximum number of towers

Once we have built our first tower of required size, we have atleast X blocks in our inventory (due to our last operation). For all the remaining operations, we build a new tower of height X in each operation.

To sum up, the answer is 0, if M<(ceil(log_2(X))+1), else, we can build M-ceil(log_2(X)) towers of height X in M operations.

#
[](#time-complexity-7)TIME COMPLEXITY:

The time complexity is O(1) per test case.

#
[](#solution-8)SOLUTION:

Setter's Solution
``t = int(input())
for _ in range(0 ,t):
    x, m = map(int, input().split())
    cnt  = 1; size = 0; k = 0
    while(m != 0):
        m -= 1
        size += cnt
        if(size >= x):
            m += 1
            break
        k += 1
        if(k == 1):
            cnt = 1
        else:
            cnt *= 2
    if(m < 0):
        print(0)
    else:
        print(m)
``

Tester's Solution
``#include<bits/stdc++.h>
using namespace std;

#define ll long long

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r" , stdin);
    freopen("output.txt", "w" , stdout);
    #endif
    int T=1;
    cin >> T;
    while(T--){

        ll x,m;
        cin>>x>>m;

        ll curr_sz = 1;
        ll len = 0;
        ll ops = 0;

        while(len < x){
            len+=curr_sz;
            curr_sz = len;
            ops++;
        }

        cout<<max(0ll, m-ops+1)<<'\n';

    }
    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";
    return 0;
}
``

Editorialist's Solution
``#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
	    long long int x, m;
	    cin>>x>>m;
	    long long int minm = ceil(log2(x))+1;
	    if(m < minm){
	        cout<<0;
	    }
	    else{
	        cout<<m - minm + 1;
	    }
	    cout<<endl;
	}
	return 0;
}
``

</details>
