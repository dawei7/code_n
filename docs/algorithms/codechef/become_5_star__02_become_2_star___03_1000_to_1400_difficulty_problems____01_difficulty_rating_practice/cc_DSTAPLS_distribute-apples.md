# Distribute Apples

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DSTAPLS |
| Difficulty Rating | 1374 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [DSTAPLS](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/DSTAPLS) |

---

## Problem Statement

Yesterday, Chef found $K$ empty boxes in the cooler and decided to fill them with apples. He ordered $N$ apples, where $N$ is a multiple of $K$. Now, he just needs to hire someone who will distribute the apples into the boxes with professional passion.

Only two candidates passed all the interviews for the box filling job. In one minute, each candidate can put $K$ apples into boxes, but they do it in different ways: the first candidate puts exactly one apple in each box, while the second one chooses a random box with the smallest number of apples and puts $K$ apples in it.

Chef is wondering if the final distribution of apples can even depend on which candidate he hires. Can you answer that question?

Note: The boxes are distinguishable (labeled), while the apples are not. Therefore, two distributions of apples are different if there is a box such that the number of apples in it when the first candidate finishes working can be different from the number of apples in it when the second candidate finishes working.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated integers $N$ and $K$.

### Output
For each test case, print a single line containing the string `"YES"` if the final distributions of apples can be different or `"NO"` if they will be the same (without quotes).

### Constraints
- $1 \le T \le 250$
- $1 \le N, K \le 10^{18}$
- $N$ is divisible by $K$

### Subtasks
**Subtask #1 (30 points):** $1 \le N, K \le 10^5$

**Subtask #2 (70 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
3
5 1
4 2
10 10
```

**Output**

```text
NO
NO
YES
```

**Explanation**

**Example case 1:** No matter who is hired, all apples will be in the only box at the end.

**Example case 2:** At the end, there will be two apples in each box.

**Example case 3:** If we hire the first candidate, there will be one apple in each box, but if we hire the second one, there will be $10$ apples in one box and none in all other boxes.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 1
```

**Output for this case**

```text
NO
```



#### Test case 2

**Input for this case**

```text
4 2
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
10 10
```

**Output for this case**

```text
YES
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Div1](https://www.codechef.com/AUG19A/problems/DSTAPLS)

[Div2](https://www.codechef.com/AUG19B/problems/DSTAPLS)

[Practice](https://www.codechef.com/problems/DSTAPLS)

**Setter-**  [Yulian](https://www.codechef.com/users/y__y)

**Tester-**  [Suchan Park](https://www.codechef.com/users/tncks0121)

**Editorialist-** [Abhishek Pandey](https://www.codechef.com/users/vijju123)

### DIFFICULTY:

Simple

### PRE-REQUISITES:

Observations, Simple Maths

### PROBLEM:

Given N apples and K boxes,  he has 2 candidates who fill the boxes as following-

- Every minute, first candidate puts 1 apple in each of the K boxes.

- Every minute, the second candidate puts K apple in the box with least number of apples

We need to tell if the final configuration of apples filled by both candidates will be same or not.

### QUICK-EXPLANATION:

**Key to AC-** Configuration can be equal only at time t=K,2K,3K...\& etc. Make sure you have enough apples so that all applies are exhausted at these favorable values of t.

Realize that since first candidate puts 1 apple in each box every minute, while the second candidate puts K apples at once in the box he choses. The configuration can only be same at a time t such that t is a multiple of K. This puts a restriction that N must be divisible by K^2 so that all apples are exhausted only at such favorable t.

### EXPLANATION:

This editorial will have 2 sections -

- Proof that final configuration is same only at time t=K,2K,3K.... \&etc

- How to use the above proof to arrive at a solution.

Proof on when final configuration is same.

I will give 2 point of view, or perspective for the proof. Each point of view is based on deriving the proof by looking at actions of a candidate.

-

The first candidate puts 1 apple in each of the boxes, while second candidate puts K apples in a box per minute. This also implies that, number of apples the second candidate has put in some box is always a multiple of K (as he puts K apples every time!) Now, the final configuration can only be same if the number of apples put in by first candidate is also a multiple of K. This can occur only if time t is a multiple of K, as the first candidate puts just 1 apple per minute. Since t must be a multiple of K as proved just now, let t=i*K where i is some integer.  Now, since the number of boxes is also K, the second candidate has filled each of the K boxes with K*i apples. Also, the first candidate puts 1 apple every minute, and hence has also filled all boxes with K*i apples. Hence the final configuration is same at t=K*i for all integral values of i.

-

The alternate perspective of proof his from point of view of second candidate. In first minute, the first candidate has filled all boxes with 1 apple. Now, the final configuration can only be same iff the second candidate also fills all the boxes - else its obvious that final configuration is different. This is possible only if t is a multiple of K.

How to use above proof

Now, we know that final configurations are same at t=i*K where i is some integer. This imposes a very nice restriction on N.

The restriction is that N must be such that all N apples are exhausted at time t=i*K. We also know that each minute K apples are being used by each candidate! This means the total number of apples N, such that all apples are used at t=i*K is N=K*(i*K)=i*K^2.

This means that N must be divisible by K^2.

A solution in python, or one using big integer library in JAVA etc can comfortably do it. For C++, where support for numbers >2^{64} is not there by default, we will use below trick.

Now, since K\leq 10^{18}  hence squaring K will cause overflow. The usual procedure to then check if N is divisible by K^2 is to first check if N \%K==0 and then check that (N/K) \% K==0. Since its given that N is always a multiple of K, we just need to check if (N/K) \% K==0. If its true, then the configurations are same - else they are not!

### SOLUTION

Setter
``#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main() {
	ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
	int T;
	cin>>T;
	while(T--) {
		ll n,k;
		cin>>n>>k;
		if((n/k)%k==0) cout<<"NO\n";
		else cout<<"YES\n";
	}

	return 0;
}
``

Tester(KOTLIN)
``fun main(Args: Array<String>) {
  repeat(readLine()!!.toInt()) {
    val (N, K) = readLine()!!.trim().split(" ").map{ it.toLong() }
    require(N in 1L..1000000000000000000L)
    require(K in 1L..1000000000000000000L)
    println(if(K <= 1000000000L && N % (K * K) == 0L) "NO" else "YES")
  }
}
``

Time Complexity=O(1) per test case

Space Complexity=O(1)  per test case

### CHEF VIJJU’S CORNER

-

Solve the following variants of the problem-

-
N is not necessarily a multiple of K

- The second candidate puts K apples in a random box instead of the box with minimum apples. In this case, print `YES` if final configuration is same no matter how minute candidate puts apples. Discuss if a `YES` `NO` solution to this is even possible or not.

-

Explore a solution of this problem in python and realize why python has an advantage over C++ here.

Setter's Notes

Notice that the amount of apples in each box stays the same for the first employee. So the distribution can be the same only when apples are equally arranged in the boxes. For the second employee the arrangement is the same only in the end of every K-th minute.

So we just need to check whether the N is divisible by K^2 to get the answer (we takes K apples every minute, for K minutes).

For C++ users K^2 will result in overflow on the original constraints. But we know that N is divisible by K so we can first divide N by K and then check whether the result is divisible by K.

Related Problems

- [Chef and Adventures](https://www.codechef.com/SEPT18A/problems/CHEFADV)

- [Chef and Difficult Contests](https://www.codechef.com/NOV18B/problems/CHFTIRED)

Liked the Editorial?

Dont forget to LIKE, COMMENT, SHARE AND SUBSCRIBE,and click the bell icon so you receive notification for every editorial

</details>
