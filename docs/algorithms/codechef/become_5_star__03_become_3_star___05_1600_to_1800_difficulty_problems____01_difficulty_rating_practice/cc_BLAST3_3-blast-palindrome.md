# 3-Blast Palindrome

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BLAST3 |
| Difficulty Rating | 1699 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [BLAST3](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/BLAST3) |

---

## Problem Statement

You are given a string $S$ of length $N$.
Your task is to convert the string into a **non-empty** [palindrome](https://en.wikipedia.org/wiki/Palindrome#Characters,_words,_or_lines) using the following operation any (possibly zero) number of times:
- Choose an index $1\lt i\lt |S|$, where $|S|$ denotes the current length of string;
- Remove the characters at indices $(i-1)$, $i$, and $(i+1)$ from the string and concatenate remaining part(s) of the string.

Print `YES` if it is possible to convert the string into a non-empty palindrome and `NO` otherwise.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains $N$ - the length of string.
    - The next line contains string $S$.

---

## Output Format

For each test case, print on a new line, `YES`, if it is possible to convert the given string into a non-empty palindrome, otherwise print `NO`.

Each character of the output may be printed in either uppercase or lowercase, i.e, the strings `Yes`, `YES`, `yes`, and `yEs` will be treated as identical.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 2 \cdot 10^5$
- $S$ consists of lowercase english alphabets only.
- The sum of $N$ over all test cases won't exceed $5 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
5
aaaaa
5
abcde
5
aabcd
```

**Output**

```text
YES
NO
YES
```

**Explanation**

**Test case $1$:** The given string is already a palindrome. Thus, we need $0$ operations.

**Test case $2$:** It is not possible to convert the string `abcde` into a palindrome using any number of operations.

**Test case $3$:** Choose $i = 4$ and delete the characters at indices $3, 4,$ and $5$. Thus, the string `aabcd` becomes `aa`, which is a palindrome.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
aaaaa
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
5
abcde
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
5
aabcd
```

**Output for this case**

```text
YES
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/BLAST3)

[Contest: Division 1](https://www.codechef.com/START98A/problems/BLAST3)

[Contest: Division 2](https://www.codechef.com/START98B/problems/BLAST3)

[Contest: Division 3](https://www.codechef.com/START98C/problems/BLAST3)

[Contest: Division 4](https://www.codechef.com/START98D/problems/BLAST3)

***Author:*** [pols_agyi_pols](https://www.codechef.com/users/pols_agyi_pols)

***Tester & Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

1699

# [](#prerequisites-3)PREREQUISITES:

Observation

# [](#problem-4)PROBLEM:

You’re given a string S of length N.

In one move, you can delete a substring of length 3 from it.

Is it possible to obtain a non-empty palindrome by performing this operation several times?

# [](#explanation-5)EXPLANATION:

Let’s think about this problem in reverse: suppose we end up with a palindrome — can we say anything about it?

In particular, suppose we end up with a palindrome P of length K. Then,

- If K \geq 7, we can use our operation to delete the first 3 and last 3 characters of P to obtain a shorter one, of length K - 6.

This means it’s enough to check if it’s possible to obtain a palindrome of length \leq 6.

- In fact, we can reduce this even further:

- If K = 4, delete the first three characters and we’re left with a length-1 string; which is a palindrome.

- If K = 5, delete the middle three characters to obtain a length-2 palindrome.

- If K = 6, delete the second, third, fourth characters to obtain a length-3 palindrome.

- Together, this tells us that we only really need to check whether a palindrome of length \leq 3 can be obtained.

Now, notice that the length of the string doesn’t change modulo 3, since we delete three characters at a time.

So, whether we need to check for length = 1, 2,  or 3 is uniquely determined by the value of N modulo 3.

Let’s look at what happens for different values of N. There are three cases here.

Case 1

**Case 1:** N = 3x+1 for some x

Here, it’s always possible to obtain a palindrome: keep the first character and delete the remaining ones.

Case 2

**Case 2:** N = 3x+2 for some x.

Here, we need to check whether a length-2 palindrome can exist.

Suppose i and j are the indices remaining in the end, and everything else is deleted. Then,

- We should have S_i = S_j.

- Everything before i has to be deleted, so the number of characters before i should be a multiple of 3.

That is, i = 3k_1 + 1 for some integer k_1, or i \bmod 3 = 1.

- Everything after j has to be deleted, so the number of characters after j should also be a multiple of 3.

That is, j \bmod 3 = N\bmod 3.

- If the above two conditions are satisfied, the condition N = 3x+2 means that the number of

characters between i and j will also be a multiple of 3, so everything inbetween can be deleted.

Checking whether some valid i and j exist isn’t too hard.

- First, fix a character c, and consider only positions containing c.

- Find the leftmost i such that S_i = c and i\bmod 3 = 1.

- Find the rightmost j such that S_j = c and j\bmod 3 = N\bmod 3.

- If i \leq j, we’ve found a valid pair for this character.

This can be implemented in \mathcal{O}(N), though straightforward \mathcal{O}(26\cdot N) is also fast enough.

If a valid pair is found for any character, the answer is `Yes`.

If the check fails for all characters, the answer is `No`.

Case 3

**Case 3:** N = 3x for some x.

This is in fact basically the same as case 2 above.

Here, we need to check whether a valid length-3 palindrome can be formed.

However, the middle character doesn’t matter much - it can be anything.

So, once again if we’re able to find indices i and j such that:

- i \leq j and S_i = S_j

- Everything before i and everything after j can be deleted

we’ll be done, because the number of characters between such i and j will be 1 modulo 3; meaning we can delete all but one of them.

The exact same \mathcal{O}(26\cdot N) algorithm to compute i and j as case 2 will work here.

As for implementation, note that the actual algorithm is exactly the same across all three cases: so you don’t actually need to perform any casework to implement it.

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) or \mathcal{O}(26\cdot N) per testcase.

# [](#code-7)CODE:

Author's code (C++, O(26N))
``#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
    ll kitne_cases_hain;
    kitne_cases_hain=1;
    //freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
    cin>>kitne_cases_hain;
    while(kitne_cases_hain--){
        ll n;
        cin>>n;
        string s;
        cin>>s;
        if((n%3)==1){
            cout<<"YES\n";
            continue;
        }
        ll flag=0;
        ll l,r;
        for(int i=0;i<26;i++){
            l=0;r=0;
            for(int j=0;j<n;j++){
                if((s[j]-'a')==i && (j%3)==0){
                    l=j+1;
                    break;
                }
            }
            for(int j=n-1;j>0;j--){
                if((s[j]-'a')==i && ((n-1-j)%3)==0){
                    r=j+1;
                    break;
                }
            }
            if(r>l && l!=0){
                flag=1;
                break;
            }
        }
        if(flag){
            cout<<"YES\n";
        }else{
            cout<<"NO\n";
        }
    }
	return 0;
}
``

Editorialist's code (Python, O(N))
``for _ in range(int(input())):
    n = int(input())
    s = input()
    left, right = [n]*26, [-1]*26
    for i in range(n):
        ch = ord(s[i]) - ord('a')
        if i%3 == 0: left[ch] = min(left[ch], i)
        if (n-1-i)%3 == 0: right[ch] = i
    print('Yes' if sum(left[i] <= right[i] for i in range(26)) > 0 else 'No')
``

</details>
