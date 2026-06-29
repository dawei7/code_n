# Little Elephant and T-Shirts

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TSHIRTS |
| Difficulty Rating | 2242 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [TSHIRTS](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/TSHIRTS) |

---

## Problem Statement

Little Elephant and his friends are going to a party. Each person has his own collection of T-Shirts. There are **100** different kind of T-Shirts. Each T-Shirt has a unique id between **1** and **100**. No person has two T-Shirts of the same ID.

They want to know how many arrangements are there in which no two persons wear same T-Shirt. One arrangement is considered different from another arrangement if there is at least one person wearing a different kind of T-Shirt in another arrangement.

### Input

First line of the input contains a single integer ** T ** denoting number of test cases. Then **T** test cases follow.

For each test case, first line contains an integer **N**, denoting the total number of persons. Each of the next **N** lines contains at least **1** and at most **100** space separated distinct integers, denoting the ID's of the T-Shirts **i**th person has.

### Output

For each test case, print in single line the required number of ways modulo **1000000007 = 109+7**.

### Constraints

- **1 ≤ T ≤ 10**

- **1 ≤ N ≤ 10**

### Example
`**Input:**
2
2
3 5
8 100
3
5 100 1
2
5 100

**Output:**
4
4
`

### Explanation

For the first case, **4** possible ways are **(3,8)**, **(3,100)**, **(5,8)** and **(5,100)**.For the second case, **4** possible ways are **(5,2,100)**, **(100,2,5)**, **(1,2,100)**, and **(1,2,5)**.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/TSHIRTS)

[Contest](http://www.codechef.com/AUG14/problems/TSHIRTS)

**Author:** [Lalit Kundu](http://www.codechef.com/users/darkshadows)

**Tester:** [Praveen Dhinwa](http://www.codechef.com/users/dpraveen) and [Hiroto Sekido](http://www.codechef.com/users/laycurse)

**Editorialist:** [Lalit Kundu](http://www.codechef.com/users/darkshadows)

### DIFFICULTY:

EASY-MEDIUM

### PREREQUISITES:

Dynamic Programming, Bitmasking, Recursion

### PROBLEM:

There are N(<11) persons. Each person has his collection of distinct tshirts. What are the total number of different such arrangements such in which no two people wear same kind of tshirt.

A person can have atmost 100 distinct tshirts.

### EXPLANATION:

It is a very standard kind of Dynamic Programming with bitmasking. So the idea here is to keep a 2-D array DP[2N][K], where DP[i][j] will store the answer only if tshirts from id 1 to j have been used. Also, let’s say i when denoted in binary be b1,b2…bn. If bp(1 ? p ? n) is 1, it means that person with id==p has been alloted a tshirt and all persons with bits 1 are assigned distinct tshirts.

So, we’ll write a recursive DP, which is obviously easier to write.

We keep a function rec(mask, tid) which means that tshirts till id tid have been processed and mask denotes which persons have been given tshirts. At each step we assign tshirts to each possible person and recursively calculate the number of ways.a

Following pseudo code will make it more clear.

``dp[1<<N][K]={}
memset dp to -1    // dp[i][j]=-1 means it hasn't been calculated yet
def rec(mask, tid):  // tid denotes the tshirt id
    if mask==2**(N)-1:  // all bits are set, all persons have been alloted tshirts
	return dp[mask][tid]=1
    if tid==101:    // all tshirts finished
	return 0
    if dp[mask][tid]!=-1:   // it has already been calculated, we won't calculate it again
	return dp[mask][tid]
    ans=0
    ans += rec(mask,tid+1)  // the case when we don't assign tshirt with id=tid to anyone
    // the case when we assign tshirt with id=tid to someone
    // we will assign the tshirt with id=tid to all possible persons we can, and add to answer the respective number of ways
    // note that we are assigning distinct tshirts only, since tshirt with id=tid has never been assigned before to anyone.
    for persons p(0<=p<=N-1) which have tshirt with id=tid:
	if mask&(1<<p): // person p + 1 has already been alloted a tshirt
	    continue    // do nothing
	ans += rec(mask|(1<<p),tid+1)   // assign tshirt tid to person p and add to answer next cases

    return dp[mask][tid]=ans;
``

Our answer will be rec(0,1) ie. starting with mask=0(no one has been assigned any tshirt) and tid=1. Complexity will be in worst case O(K*2N).

### AUTHOR’S AND TESTER’S SOLUTIONS:

[Author’s solution](http://www.codechef.com/download/Solutions/2014/August/Setter/TSHIRTS.cpp)

[Tester’s solution](http://www.codechef.com/download/Solutions/2014/August/Tester/TSHIRTS.cpp)

### FURTHER LINKS AND SIMILAR PROBLEMS

[A little bit of classics: dynamic programming over subsets and paths in graphs](http://codeforces.com/blog/entry/337)

[SOCOLA](http://www.spoj.com/problems/SOCOLA/)

[Topcoder Problem](http://community.topcoder.com/stat?c=problem_statement&pm=11566)

[Dp with Bitmasking](http://discuss.codechef.com/questions/5483/dynamic-programming-problems-with-bitmasking)

</details>
