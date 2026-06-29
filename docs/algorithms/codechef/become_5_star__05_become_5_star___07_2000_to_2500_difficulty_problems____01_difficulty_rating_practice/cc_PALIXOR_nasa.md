# NASA

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PALIXOR |
| Difficulty Rating | 2014 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [PALIXOR](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/PALIXOR) |

---

## Problem Statement

*I'ma need space, I'ma, I'ma need \
You know I'm a star; space, I'ma need space \
I'ma need space, I'ma, I'ma need space (N-A-S-A)*

Given an array $A$ of size $N$.
Find total number of pairs in the array $(i, j)$ $(1\le i\le j \le N)$ such that:
- $A_i \oplus  A_j$ is a [palindrome](https://en.wikipedia.org/wiki/Palindrome#Numbers) (in **decimal** representation), where $\oplus$ denotes the [bitwise xor operator](https://en.wikipedia.org/wiki/Bitwise_operation#XOR).

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains one integer $N$ - the size of the array.
    - The next line contains $N$ space-seperated integers as array elements.

---

## Output Format

For each test case, output on a new line, the number of pairs satisfying the given condition.

---

## Constraints

- $1 \leq T \leq 10^{2}$
- $1 \leq N \leq 10^{5}$
- $0 \leq A_i \lt 2^{15}$
- The sum of N over all test cases does not exceed $2\cdot 10^{5}$.

---

## Examples

**Example 1**

**Input**

```text
2
4
13 27 12 26
3
2 2 2
```

**Output**

```text
8
6
```

**Explanation**

**Test case $1$:** The pairs which form palindrome are :
- $13 \oplus  13 = 0$
- $13 \oplus  27 = 22$
- $13 \oplus  12 = 1$
- $27 \oplus  27 = 0$
- $27 \oplus  26 = 1$
- $12 \oplus  12 = 0$
- $12 \oplus  26 = 22$
- $26 \oplus  26 = 0$

**Test case $2$:** All the pairs form palindrome.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
13 27 12 26
```

**Output for this case**

```text
8
```



#### Test case 2

**Input for this case**

```text
3
2 2 2
```

**Output for this case**

```text
6
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/PALIXOR)

[Contest: Division 1](https://www.codechef.com/START93A/problems/PALIXOR)

[Contest: Division 2](https://www.codechef.com/START93B/problems/PALIXOR)

[Contest: Division 3](https://www.codechef.com/START93C/problems/PALIXOR)

[Contest: Division 4](https://www.codechef.com/START93D/problems/PALIXOR)

***Author:*** [saksham441](https://www.codechef.com/users/saksham441)

***Tester & Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

2014

#
[](#prerequisites-3)PREREQUISITES:

Familiarity with bitwise XOR, frequency tables, observation

#
[](#problem-4)PROBLEM:

Given an array A, count the number of pairs (i, j) such that 1 \leq i \leq j \leq N and A_i \oplus A_j is a palindrome.

It’s known that A_i \lt 2^{15}.

#
[](#explanation-5)EXPLANATION:

A brute force algorithm would be to check for each (i, j) pair whether their XOR forms a palindrome; of course, this is too slow.

Notice that the number of distinct palindromes we care about is really quite small.

In particular, there are only about \mathcal{O}(10^{\frac{\log_{10}X}{2}}) (which is about  \mathcal{O}( \sqrt X)) palindromes below X, because fixing one half of the palindrome fixes the other half as well.

In particular, only 427 of the numbers upto 2^{15} are palindromes.

Further, recall that XOR is an *involution*, i.e, x\oplus y = z also means that x = z\oplus y.

So, instead of fixing i and j and checking if A_i\oplus A_j is a palindrome, we can fix i and the target palindrome; which then uniquely fixes A_j; after which we only need to count the number of valid j.

That is,

- Let \text{Pal} be a list of palindromes upto 2^{15}. This can be precomputed, and has length 427.

- Then, for each i from 1 to N, and each x in \text{Pal},

- Let y = A_i \oplus x.

- We then want to know the number of indices j such that A_j = y.

This can be found in \mathcal{O}(1) using a frequency table.

Make sure not to overcount pairs of indices, since the above algorithm didn’t account for the i \leq j condition.

That’s not too hard: all pairs except (i, i) will be counted twice, so divide by 2 appropriately.

The complexity is something like \mathcal{O}(430\cdot N) (more formally, \mathcal{O}(N\cdot \sqrt{\max A})), which is good enough to get AC.

Note that the frequency table can be implemented using either an array or a hashmap (`std::unordered_map`, `dict`, `HashMap`) and should run in time without much issue.

Using `std::map` will likely be too slow because of the extra \log factor.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N\cdot P) per test case, where P is the number of palindromes not exceeding 2^{15} (approximately 430).

#
[](#code-7)CODE:

Author's code (C++)
``#include<bits/stdc++.h>
using namespace std;
vector<int>allPalindrome;
#define fast ios_base::sync_with_stdio(false);cin.tie(NULL)
bool isPalindrome(int num){
	int rev=0;
	int temp=num;
	while (num>0){
		rev=rev*10 + (num%10);
		num/=10;
	}
	return (rev==temp);
}
void solve(){
	long long int n;
	cin>>n;
	long long int v[n];
	long long int freq[(1<<17)];
	memset(freq,0,sizeof(freq));
	for (int i=0;i<n;i++){
		cin>>v[i];
		freq[v[i]]++;
	}
    long long int ans=0;
	for (int i=0;i<allPalindrome.size();i++){
		long long int num=allPalindrome[i];
		for (int j=0;j<n;j++){
			ans+=freq[v[j]^num];
		}
	}

	//Divide ans by 2 as each pair will be calculated twice
	ans/=2;
	//add all pairs such that A[i]^A[j] = 0 means A[i] and A[j] are same
    for (int i=0;i<(1<<17);i++){
        ans = ans + (freq[i] * (freq[i]+1))/2;

    }
	cout<<ans<<endl;
}

void generatePalindromes(){
	for (int i=1;i<=(1<<17);i++){
		if (isPalindrome(i)){
			allPalindrome.push_back(i);
		}
	}
}

int main(){
	int t;
	fast;
	cin>>t;
	generatePalindromes();
	while (t--){
		solve();
	}
}
``

Editorialist's code (Python)
``mx = 1 << 15
palindromes = []
for i in range(mx):
    if str(i) == str(i)[::-1]: palindromes.append(i)

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    freq = {}
    ans = 0
    for x in a:
        if x in freq: freq[x] += 1
        else: freq[x] = 1
    for x in a:
        for y in palindromes:
            if x^y <= x: continue
            if x^y in freq: ans += freq[x^y]
    for x in freq.values(): ans += x*(x+1)//2
    print(ans)
``

</details>
