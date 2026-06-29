# 01 Subsequence

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ZEROONE |
| Difficulty Rating | 1781 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [ZEROONE](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/ZEROONE) |

---

## Problem Statement

You are handed a binary string $S$, but not in any ordinary form. Instead of being directly given the value of $S$, you are given an array $C$ of size $N$ representing the *01-compression representation* of $S$. This means $S$ first contains $C_1$ $\texttt{0}$ characters, then $C_2$ $\texttt{1}$ characters, then $C_3$ $\texttt{0}$ characters, and so on. For example, the array $C = [2, 3, 4, 3]$ corresponds with the binary string $\texttt{001110000111}$.

You are allowed to modify $S$ by swapping elements of $C$. More specifically, you are allowed to swap $C_i$ and $C_j$ *as long as* $C_i$ and $C_j$ both encodes blocks of the same character. For example, from $C = [2, 3, 4, 3]$, you can swap $C_1$ and $C_3$ because both of them encode blocks of $\texttt{0}$'s, turning $C$ to $[4, 3, 2, 3]$ and $S$ to $\texttt{000011100111}$. However, you cannot swap $C_1$ and $C_2$ because $C_1$ encodes a block of $\texttt{0}$'s, while $C_2$ encodes a block of $\texttt{1}$s.

Perform the swapping operation in any way as many times as you want (including zero times) so that the final string $S$ has as many $\texttt{01}$ subsequences as possible. As a reminder, a subsequence of a string is a sequence that can be derived by deleting zero or more characters without changing the order of the remaining characters.

You need to find any optimal final array $C$, for which the number of $\texttt{01}$ subsequence will be the largest possible.

---

## Input Format

- The first line contains $T$ - the number of test cases. Then the test cases follow.
- The first line of each test case contains a single integer $N$ - the size of the array $C$.
- The second line of each test case contains $N$ integers $C_1, C_2, \dots, C_N$ - the $\texttt{01}$-compression representation of $S$.

---

## Output Format

For each test case, output two lines: the first line contains $N$ integers representing the optimal array $C$, and the second line contains the maximum number of $\texttt{01}$ subsequences.

---

## Constraints

- $ 1 \leq T \leq 1000 $
- $ 1 \leq N \leq 100 $
- $ 1 \leq  C_i \leq 1000 $

---

## Examples

**Example 1**

**Input**

```text
1
4
2 3 4 3
```

**Output**

```text
4 3 2 3
30
```

**Explanation**

- **Test case $1$:** $C = [2, 3, 4, 3]$, which means $S$ corresponds to $\texttt{001110000111}$. The optimal list of operations is to only swap $C_1$ and $C_3$, resulting in $C = [4, 3, 2, 3]$ and $S = $ $\texttt{000011100111}$, which has $30$ subsequences of $\texttt{01}$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/ZEROONE)

[Contest: Division 1](https://www.codechef.com/COOK134A/problems/ZEROONE)

[Contest: Division 2](https://www.codechef.com/COOK134B/problems/ZEROONE)

[Contest: Division 3](https://www.codechef.com/COOK134C/problems/ZEROONE)

***Author:*** [Prasant Kumar](https://www.codechef.com/users/prasant21)

***Tester:*** [Danny Mittal](https://www.codechef.com/users/tlatoani)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

Simple

#
[](#prerequisites-3)PREREQUISITES:

Sorting, rearrangement inequality (or at least intuition for it)

#
[](#problem-4)PROBLEM:

You are given an array C which represents a binary string B, where the first C_1 characters of B are `0`, the next C_2 are `1`, the next C_3 are `0`, and so on.

You can swap two elements of C as long as they both correspond to blocks of the same character.

Maximize the number of times `01` occurs as a subsequence in B.

#
[](#quick-explanation-5)QUICK EXPLANATION

Sort the elements at odd indices (C_1, C_3, C_5, \dots) in descending order, and the elements at even indices (C_2, C_4, C_6, \dots) in ascending order.

Having done this, the answer is \displaystyle C_2\cdot C_1 + C_4\cdot (C_1 + C_3) + C_6\cdot (C_1 + C_3 + C_5) + \dots = \sum_{i = 1}^ {\lfloor\frac{n}{2}\rfloor} C_{2i} \sum_{j = 1}^i C_{2j-1}

#
[](#explanation-6)EXPLANATION:

Let us first look at how to compute the number of times `01` occurs as a subsequence given that we know C.

Consider any block of `1`s C_{2i}. Let us count the number of  `01` subsequences which have the `1` chosen from this block.

There are C_{2i} ways to choose a `1` in this block. We then multiply this by the number of ways to choose a `0` which occurs before this block, which is C_{1} + C_{3} + C_{5} + \dots + C_{2i-1}.

Summing this over all blocks gives us

\sum_{i = 1}^ {\lfloor\frac{n}{2}\rfloor} C_{2i} \sum_{j = 1}^i C_{2j-1}

Now, how to maximize this?

Note that the given operation essentially tells us that we are free to choose an ordering of the C_{2i} and of the C_{2i-1}, and these orderings are independent of each other.

So, we try to optimize these two separately.

###
[](#ordering-c_2i-7)Ordering C_{2i}

Suppose we have fixed an order of the C_{2i-1}. What is the best way to order the elements C_{2i}?

Intuitively, we see that placing larger elements later makes more sense - the later something occurs, the higher its multiplier is and so the more it contributes to the answer.

It turns out that this is indeed optimal - sorting the C_{2i} in ascending order gives the best possible answer.

A formal proof of this seemingly intuitive idea is given by the [Rearrangement inequality](https://en.wikipedia.org/wiki/Rearrangement_inequality).

###
[](#ordering-c_2i-1-8)Ordering C_{2i-1}

The idea here is exactly the same behind the one for C_{2i}.

Sorting the C_{2i-1} in descending order ensures that the larger elements have larger multipliers, which again is optimal by the rearrangement inequality.

###
[](#putting-it-all-together-9)Putting it all together

Once the even and odd indices have been sorted in their respective orders, all that is left is to compute the total sum. This can be done in \mathcal{O}(N^2) given that the constraints are small, or even \mathcal{O}(N) by maintaining a prefix sum of odd indices.

#
[](#time-complexity-10)TIME COMPLEXITY:

\mathcal{O}(N^2) or \mathcal{O}(N\log{N}) per test, depending on implementation.

#
[](#code-11)CODE:

Setter (C++)
``#include <bits/stdc++.h>
using namespace std;
#define int long long
#define endl "\n"

signed main(){
	ios_base::sync_with_stdio(0) , cin.tie(0);

	int t;cin>>t;
	while(t--){
		int n;cin>>n;
		vector<int> v[2];
		for(int i=0;i<n;i++){
			int x;cin>>x;
			if(i&1){
				v[1].push_back(x);
			}else v[0].push_back(x);
		}

		sort(v[0].begin(),v[0].end());
		sort(v[1].begin(),v[1].end(),greater<int>());

		int cnt0=0,ans=0;

		for(int i=0;i<n;i++){
			if(i&1){
				ans+=cnt0*v[1].back();
				cout<<v[1].back()<<" ";
				v[1].pop_back();
			}else{
				cnt0+=v[0].back();
				cout<<v[0].back()<<" ";
				v[0].pop_back();
			}
		}cout<<endl;
		cout<<ans<<endl;
	}

	return 0;
}
``

Tester (Kotlin)
``fun main(omkar: Array<String>) {
    repeat(readLine()!!.toInt()) {
        val n = readLine()!!.toInt()
        val xs = readLine()!!.split(" ").map { it.toInt() }
        val ys = (0 until n step 2).map { xs[it] }.sortedDescending()
        val zs = (1 until n step 2).map { xs[it] }.sorted()
        println((0 until n).map { (if (it % 2 == 0) ys else zs)[it / 2] }.joinToString(" "))
        var answer = 0
        for (j in ys.indices) {
            for (k in zs.indices) {
                if (j <= k) {
                    answer += ys[j] * zs[k]
                }
            }
        }
        println(answer)
    }
}
``

Editorialist (Python)
``for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a[::2] = sorted(a[::2], reverse = True)
    a[1::2] = sorted(a[1::2])
    print(*a)
    ans, sm = 0, 0
    for i in range(1, n, 2):
        sm += a[i-1]
        ans += a[i]*sm
    print(ans)
``

</details>
