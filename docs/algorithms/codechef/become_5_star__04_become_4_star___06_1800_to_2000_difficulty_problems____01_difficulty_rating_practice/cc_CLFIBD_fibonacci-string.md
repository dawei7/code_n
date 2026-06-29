# Fibonacci String

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CLFIBD |
| Difficulty Rating | 1819 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1800 to 1900 difficulty problems |
| Official Link | [CLFIBD](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF1900/problems/CLFIBD) |

---

## Problem Statement

For a string $S$ let the unique set of characters that occur in it one or more times be $C$. Consider a permutation of the elements of $C$ as $(c_1, c_2, c_3 ... )$. Let $f(c)$ be the number of times $c$ occurs in $S$.

If any such permutation of the elements of $C$ satisfies $f(c_i) = f(c_{i-1}) + f(c_{i-2})$ for all $i \ge 3$, the string is said to be a **dynamic string**.

Mr Bancroft is given the task to check if the string is dynamic, but he is busy playing with sandpaper. Would you help him in such a state?

Note that if the number of distinct characters in the string is less than 3, i.e. if $|C| < 3$, then the string is always dynamic.

###Input:
- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of a single line of input, a string $S$.

###Output:
For each testcase, output in a single line "**Dynamic**" if the given string is dynamic, otherwise print "**Not**". (Note that the judge is case sensitive)

###Constraints
- $1 \leq T \leq 10$
- $1 \leq |S| \leq 10^5$
- $S$ contains only lower case alphabets: $a$, $b$, ..., $z$

---

## Examples

**Example 1**

**Input**

```text
3
aaaabccc
aabbcc
ppppmmnnoooopp
```

**Output**

```text
Dynamic
Not
Dynamic
```

**Explanation**

- **Testase 1:** For the given string, $C = \{a, b, c\}$ and $f(a)=4, f(b)=1, f(c)=3$. $f(a) = f(c) + f(b)$ so the permutation $(b, c, a)$ satisfies the requirement.
- **Testcase 2:** Here too $C = \{a, b, c\}$ but no permutation satisfies the requirement of a dynamic string.
- **Testcase 3:** Here $C = \{m, n, o, p\}$ and $(m, n, o, p)$ is a permutation that makes it a dynamic string.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
aaaabccc
```

**Output for this case**

```text
Dynamic
```



#### Test case 2

**Input for this case**

```text
aabbcc
```

**Output for this case**

```text
Not
```



#### Test case 3

**Input for this case**

```text
ppppmmnnoooopp
```

**Output for this case**

```text
Dynamic
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](http://www.codechef.com/problems/CLFIBD)

[Contest](https://www.codechef.com/COLE2018/problems/CLFIBD)

**Author:** [Avijit Agarwal](http://www.codechef.com/users/avijit_agarwal)

**Tester and Editorialist:** [Soumik Sarkar](http://www.codechef.com/users/meooow)

# DIFFICULTY:

CAKEWALK

# PREREQUISITES:

Strings, Sorting

# PROBLEM:

Given a string S find the frequency of each character in the string and check whether they can be rearranged into a sequence F where F_i = F_{i-2} + F_{i-1}  holds for all i \ge 3.

# EXPLANATION:

Finding the frequency of each character can be done in linear time. One possible way is below

``m = empty map
for each character c in S:
    if c in m:
        m[c] = m[c] + 1
    else:
        m[c] = 0
F = empty list
for each key, value in m:
    append value to F
``

Next we can say that because F_i = F_{i-1} + F_{i-2} and F_{i-2} cannot be 0, F_i > F_{i-1} for all i \ge 3. So it makes sense to sort the array F.

Then we can check if F satisfies the given condition for all i \ge 3. If it does, then the string is dynamic otherwise it is not, right? …But hold on, there is a catch. Indeed F_i > F_{i-1} for all i \ge 3, but what about F_2? The relation between F_2 and F_1 is not specified. So it maybe that F_4 \ne F_2 + F_3 in the sorted order but F_4 = F_1 + F_3. In that case if we can simply swap F_1 and F_2 to get the required sequence and the string is dynamic.

For example: F = (1, 2, 3, 4). Here 3 = 1 + 2 but of course 4 \ne 2 + 3. If we swap 1 and 2 we will get (2, 1, 3, 4) where 3 = 2 + 1 and 4 = 1 + 3.

``sort F
N = length of F
if N >= 4 and F[4] != F[2] + F[3]:
    swap(F[1], F[2])
ok = True
if N >= 3:
    for i in [3..N]:
        if F[i] != F[i - 1] + F[i - 2]:
            ok = False
if ok:
    S is dynamic
else:
    S is not dynamic
``

# AUTHOR’S AND TESTER’S SOLUTION:

Author’s solution can be found [here](https://gist.github.com/meooow25/fea592474e33b0817d3d0f4ad55685af)

Tester’s solution can be found [here](https://gist.github.com/meooow25/c66a9a7bd00889c6951c1a2c9cb0864d).

</details>
