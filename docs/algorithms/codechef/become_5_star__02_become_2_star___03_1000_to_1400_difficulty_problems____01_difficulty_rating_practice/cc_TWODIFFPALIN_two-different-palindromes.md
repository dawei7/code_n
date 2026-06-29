# Two Different Palindromes

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TWODIFFPALIN |
| Difficulty Rating | 1216 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [TWODIFFPALIN](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/TWODIFFPALIN) |

---

## Problem Statement

You are given two positive integers $A$ and $B$. You need to construct two **different** binary strings (i.e, they are strings which consist of only $0$s and $1$s), which satisfy these two conditions:

- Both the strings should be palindromes.
- Each string should have exactly $A$ $0$s, and exactly $B$ $1$s in them.

Output `Yes` if two such different binary strings can be constructed and `No` otherwise.

**Note:**
- A string is said to be a palindrome, if the string and the reverse of the string are identical.
- Two strings are said to be different if either their lengths are different, or if they differ in at least one character.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case contains two space-separated integers, $A$ and $B$, in a new line.

---

## Output Format

For each test case, output on a new line 'Yes', if you can construct two different binary strings satisfying the conditions. If not, output `No`.

You may print each character of the string in uppercase or lowercase (for example, the strings `YeS`, `yes`, `YES`, and `YEs` will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq A, B \leq 10^6$

---

## Examples

**Example 1**

**Input**

```text
3
2 2
2 3
3 3
```

**Output**

```text
Yes
Yes
No
```

**Explanation**

**Test case $1$:** Consider the binary strings $0110$ and $1001$. Both of them are palindromes, and both of them have exactly $2$ $0$s, and $2$ $1$s. Hence we can construct them, and so the answer is `Yes`.

**Test case $2$:** Consider the binary strings $01110$ and $10101$. Both of them are palindromes, and both of them have exactly $2$ $0$s, and $3$ $1$s. Hence we can construct them, and so the answer is `Yes`.

**Test case $3$:** There is no way to construct two such different strings. Hence the answer is `No`.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 2
```

**Output for this case**

```text
Yes
```



#### Test case 2

**Input for this case**

```text
2 3
```

**Output for this case**

```text
Yes
```



#### Test case 3

**Input for this case**

```text
3 3
```

**Output for this case**

```text
No
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest](https://www.codechef.com/START57/)

[Practice](https://www.codechef.com/problems/TWODIFFPALIN)

**Setter:** [munch_01](https://www.codechef.com/users/munch_01)

**Testers:** [tabr](https://www.codechef.com/users/tabr)

**Editorialist:** [aryanag_adm](https://www.codechef.com/users/aryanag_adm)

#
[](#difficulty-2)DIFFICULTY:

1216

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

You are given two integers A and B.

Determine whether it is possible to construct two distinct binary palindromes S and T where both S and T have exactly A 0's and B 1's.

#
[](#explanation-5)EXPLANATION:

If both A and B are even then the answer is “Yes”, because you can construct a string with \frac{A}{2} 0's, followed by B 1's, followed by \frac{A}{2} 0's.

Eg. if A = 6, B = 4, then you can construct 0001111000

You can construct the other string with \frac{B}{2} 1's, followed by A 0's, followed by \frac{B}{2} 1's.

Now, if both A and B are odd, then no palindrome exists, so the answer is “No”. This fact is easy to verify.

If exactly one of them is odd and also >1, then the answer is “Yes” again. The construction for this case is similar to the first case. If you assume that A is odd and B is even. You can construct the first string with \frac{A-1}{2} 0's, followed by \frac{B}{2} 1's, followed by a 0, followed by  \frac{B}{2} 1's, followed by \frac{A-1}{2} 0's. The second string is \frac{B}{2} 1's, followed by A 0's, followed by  \frac{B}{2} 1's.

If either A or B is 1, then the answer is “No”.

#
[](#time-complexity-6)TIME COMPLEXITY:

Time complexity is O(1).

#
[](#solution-7)SOLUTION:

Editorialist's Solution
``#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
	    int a, b;
	    cin>>a>>b;
	    if(a%2 && b%2){
	        cout<<"No\n";
	    }
	    else if(min(a, b) == 1){
	        cout<<"No\n";
	    }
	    else{
	        cout<<"Yes\n";
	    }
	}
	return 0;
}

``

</details>
