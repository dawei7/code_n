# Chef and the Wildcard Matching

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TWOSTR |
| Difficulty Rating | 1254 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Strings |
| Official Link | [TWOSTR](https://www.codechef.com/practice/course/1to2stars/LP1TO203/problems/TWOSTR) |

---

## Problem Statement

Chef wants to implement wildcard pattern matching supporting only the wildcard '?'. The wildcard character '?' can be substituted by any single lower case English letter for matching. He has two strings **X** and **Y** of equal length, made up of lower case letters and the character '?'. He wants to know whether the strings **X** and **Y** can be matched or not.

### Input

The first line of input contain an integer **T** denoting the number of test cases. Each test case consists of two lines, the first line contains the string **X** and the second contains the string **Y**.

### Output

For each test case, output a single line with the word **Yes** if the strings can be matched, otherwise output **No**.

### Constraints

- **1** ≤ **T** ≤ **50**

- Both **X** and **Y** have equal length and the length is between 1 and 10.

- Both **X** and **Y** consist of lower case letters and the character '?'.

---

## Examples

**Example 1**

**Input**

```text
2
s?or?
sco??
stor?
sco??
```

**Output**

```text
Yes
No
```

**Explanation**

**Test case $1$:** One of the possible ways to match both the strings is $\texttt{score}$. This can be done by:
- Replace $1^{st}$ and $2^{nd}$ $\texttt{?}$ of string $X$ by characters $\texttt{c}$ and $\texttt{e}$ respectively.
- Replace $1^{st}$ and $2^{nd}$ $\texttt{?}$ of string $Y$ by characters $\texttt{r}$ and $\texttt{e}$ respectively.

**Test case $2$:** There exists no way to fill the $\texttt{?}$ such that the strings become equal. Thus, the answer is `No`.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
s?or?
sco??
```

**Output for this case**

```text
Yes
```



#### Test case 2

**Input for this case**

```text
stor?
sco??
```

**Output for this case**

```text
No
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/TWOSTR)

[Contest](http://www.codechef.com/COOK61/problems/TWOSTR)

**Author:** [Tasnim Imran Sunny](http://www.codechef.com/users/rustinpiece)

**Tester:** [Istvan Nagy](http://www.codechef.com/users/iscsi)

**Editorialist:** [Lalit Kundu](http://www.codechef.com/users/darkshadows)

### DIFFICULTY:

Cakewalk

### PREREQUISITES:

basic programming, strings

### PROBLEM:

Chef wants to implement wildcard pattern matching supporting only the wildcard ‘?’. The wildcard character ‘?’ can be substituted by any single lower case English letter for matching. He has two strings X and Y of equal length, made up of lower case letters and the character ‘?’. He wants to know whether the strings X and Y can be matched or not.

### EXPLANATION:

================

We can reduce problem of matching two strings X and Y to matching individual characters for each index 0 \le i < N. If all characters can be matched, then we can say that both strings can also be matched.

#### MATCHING A CHARACTER

We need to check if two characters a and b can be matched or not. If either of them is ‘?’, then we can always match them by filling it with the required value. If both are ‘?’, still we can give any same value to both of them.

If both are not ‘?’, then we just need to check if the current values are same or not.

For implementation, see setter’s commented code.

### AUTHOR’S, TESTER’S SOLUTIONS:

[setter](http://www.codechef.com/download/Solutions/COOK61/Setter/TWOSTR.cpp)

[tester](http://www.codechef.com/download/Solutions/COOK61/Tester/TWOSTR.cpp)

</details>
