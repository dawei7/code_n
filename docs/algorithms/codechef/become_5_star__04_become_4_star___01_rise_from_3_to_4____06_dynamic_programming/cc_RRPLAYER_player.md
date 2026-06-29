# Player

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RRPLAYER |
| Difficulty Rating | 2067 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Dynamic Programming |
| Official Link | [RRPLAYER](https://www.codechef.com/practice/course/3to4stars/LP3TO406/problems/RRPLAYER) |

---

## Problem Statement

Petr, Nikita G. and Nikita are the most influential music critics in Saint-Petersburg. They have recently downloaded their favorite band's new album and going to listen to it. Nikita claims that the songs of entire album should be listened strictly in the same order as they are given, because there is the secret message from the author in the songs' order. Petr, being chaotic, does not think so, hence he loves listening to songs in a random order. Petr is pretty good in convincing other people, so after a two-hours discussion Nikita accepted listening in random order(the discussion's duration was like three times longer thatn the album's one). In this context random order means following: There are **N** songs in the album. In the very beginning random song is chosen(here and further "random song" means that every song has equal probability to be chosen). After some song is over the next one is chosen randomly and independently of what have been played before.

Nikita G., being the only one who is not going to drop out from the university, wonders, what is the expected number of songs guys have to listen to until every song is played at least once.

### Input

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

The first and only line of each test case contains a single integer **N** denoting the number of songs in the album.

### Output

For each test case, output a single line containing the expected number of songs the guys will listen to. Your answer will be considered as correct if it has an absolute or relative error less than **10−1**. More formally if the expected output is **A** and your output is **B**, your output will be considered as correct if and only if
**|A − B| ≤ 10−1 * max{|A|, |B|, 1}**.

### Constraints
**1** ≤ **T** ≤ ** 100 **
**1** ≤ **N** ≤ ** 3000 **

---

## Examples

**Example 1**

**Input**

```text
3
1
2
3
```

**Output**

```text
1.0
3.0
5.5
```

**Explanation**

**Example case 2** After playing the first song there is **1/2** chance to finish the album each time new song is played. So the expected number of songs is **2/2 + 3/4 + 4/8... = 3**

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
```

**Output for this case**

```text
1.0
```



#### Test case 2

**Input for this case**

```text
2
```

**Output for this case**

```text
3.0
```



#### Test case 3

**Input for this case**

```text
3
```

**Output for this case**

```text
5.5
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

[Practice](http://www.codechef.com/problems/RRPLAYER)

[Contest](http://www.codechef.com/COOK53/problems/RRPLAYER)

### PROBLEM LINK:

**Author:** [Roman Rubanenko](http://www.codechef.com/users/rubanenko)

**Tester:** [Tuan Anh](http://www.codechef.com/users/tuananh93)

**Editorialist:** [Florin Chirica](http://www.codechef.com/users/elfus)

### DIFFICULTY:

easy-medium

### PREREQUISITES:

dynamic programming, basic probability theory

### PROBLEM:

We add elements from 1 to n to a list until all n elements appear in the list. Each element can be added with the same probability. What’s the expected number of elements from the list?

### QUICK EXPLANATION:

Let’s keep dp[i][j] = what’s probability to have j different elements in the list, such as length of the list is i. We can simulate this solution until the probabilities become small enough. Then, we can either notice the pattern or precalculate the answers in a constant vector.

### EXPLANATION:

**Small values of n**

Approach for small values of n is pretty common in probability tasks. Let’s keep dp[i][j] = the probability to have j different elements in the list, such as length of the list is i.

Definition of expected value is sum of Probability * Value. In this case, probability is calculated by dp for a given length and value is the length itself. Since the list must contain all elements, we get that our answer is sum of dp[len][n] * len.

The trick used here is to consider precision: the precision required is very small. This means, when values dp[len][n] * len becomes *almost* zero, we can stop the simulation, since it won’t affect the result anyway (well, actually it would affect the result, but for the given precision, it doesn’t matter). In our solution, we consider *almost* zero to be < 1e-4.

We’re left with recurrences of dp. An element is being chosen with probability 1 / n. We consider dp[0][0] = 0. Suppose we’ve calculated dp[i][j] and we want to update the results for dp[i + 1][li]. What can be the recurrences?

[/li]

Well, to find them, let’s analyze the two cases we have.

- We don’t add a new element

This means, we need to add one of existing j elements. The probability to pick one of existing j elements is j / n. So we get

dp[i + 1][j] += dp[i][j] * (j / n)

- We add a new element

We can choose only (n - j) elements. The probability to pick one of them is (n - j) / n.

So we get dp[i + 1][j + 1] += dp[i][j] * ((n - j) / n).

Pay attention when you calculate dp[i][n]. You are not allowed to add result from dp[i - 1][n], since the list of length i - 1 already contains all n elements. This approach should be used for n <= 400 (or something like this). For larger values, it should time out.

**Large values of n**

There are two ways to solve for larger values. The first one is the most obvious: run your program locally, then store answers in a file, put answers in an array in your program and simply output relevant content of the array.

The not so obvious one is to notice the answer is about n * ln(n) for large values. For those who like proofs, we leave this one as a homework for you

### AUTHOR’S AND TESTER’S SOLUTIONS:

Author’s solution to be updated soon

[Tester’s solution](http://www.codechef.com/download/Solutions/COOK53/tester/RRPLAYER.cpp)

</details>
