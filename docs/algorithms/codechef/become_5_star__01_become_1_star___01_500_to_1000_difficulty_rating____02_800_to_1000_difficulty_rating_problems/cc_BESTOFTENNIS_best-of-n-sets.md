# Best of N Sets

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BESTOFTENNIS |
| Difficulty Rating | 830 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [BESTOFTENNIS](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/BESTOFTENNIS) |

---

## Problem Statement

Sonu and Titu are playing a tennis match. They are playing a "best of $N$ sets" match ($N$ is always odd). That means that they will play at most $N$ sets, and the person who has won most sets wins the match. But they are smart, and if they notice at any point that one of them has no chance of winning the match, they will stop the match right then, without playing out all the $N$ sets needlessly.

For example, suppose $N = 11$. And at some point, Sonu has won 5 sets, and Titu has won 4 sets. Sonu is leading now, but it is possible that Titu wins the two remaining sets and wins the whole match. So they will not stop right now.

But suppose Sonu wins the next set as well, and so now the score is $(6, 4)$. Now, even though there is one set remaining, there is no chance of Titu winning the whole match, since at best, even if he wins the next set, the score will become $(6, 5)$, and Sonu still wins. So, they will stop at a score of $(6, 4)$ and declare Sonu as the winner.

As another example, if $N=15$, and the score is currently $(8, 2)$, then they'll stop right now, since there is no way for Titu to win the match. Even if Titu wins all the $5$ remaining sets, Titu cannot win the match.

---

You are watching the match, and you see that the match has ended with a score of $(X, Y)$. That is, Sonu has won $X$ sets, and Titu has won $Y$ sets. But you don't know what $N$ is. Can you find out $N$ from just knowing the final score?

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line of input containing two space-separated integers $X$ and $Y$ where $X$ is the number of sets won by Sonu and $Y$ is the number of sets won by Titu.

---

## Output Format

- For each test case, output on a new line the value of $N$.
- Note that you should only output an odd integer.

---

## Constraints

- $1 \leq T \leq 10000$
- $1 \leq X \leq 100$
- $1 \leq Y \leq 100$
- $X ≠ Y$, since they would never stop when they have won the same number of sets.

---

## Examples

**Example 1**

**Input**

```text
4
2 5
8 10
99 1
4 8
```

**Output**

```text
9
19
197
15
```

**Explanation**

**Testcase 1:** Sonu has won 2 sets and Titu has won 5. They have played 7 sets and Titu has been decided to be the winner.

Suppose $N = 11$, then 4 more sets are remaining and if Sonu wins them all, Sonu's score ($2 + 4 = 6$) will become greater than Titu's score of $5$. So at this point, they could not have stopped playing, and so $N$ cannot be $11$ or more.

But suppose $N = 9$, then 2 more sets are remaining and even if Sonu wins them all, he still cannot win, since $2 + 2 = 4$ is still $< 5$. So it makes sense that they stopped right now.

$N$ can't be lower than $9$, since they would have stopped the match sooner.

So, the answer is $N = 9$.

**Testcase 2:** Sonu has won 8 sets and Titu has won 10. They have played 18 sets and Titu has been decided to be the winner.

Suppose $N = 21$, then 3 more sets are remaining and if Sonu wins them all, Sonu's score ($8 + 3 = 11$) will become greater than Titu's score of $10$. So at this point, they could not have stopped playing, and so $N$ cannot be $21$ or more.

But suppose $N = 19$, then 1 more set is remaining and even if Sonu wins that set, he still cannot win, since $8 + 1 = 9$ is still $< 10$. So it makes sense that they stopped right now.

$N$ can't be lower than $19$, since they have played $18$ sets.

So, the answer is $N = 19$.

**Testcase 3:** Sonu has won 99 sets and Titu has won 1. They have played 100 sets and Sonu has been decided to be the winner.

Suppose $N = 199$, then 99 more sets are remaining and if Titu wins them all, Titu's score ($1 + 99 = 100$) will become greater than Titu's score of $99$. So at this point, they could not have stopped playing, and so $N$ cannot be $199$ or more.

But suppose $N = 197$, then 97 more sets are remaining and even if Titu wins that set, he still cannot win, since $1 + 97 = 98$ is still $< 9$. So it makes sense that they stopped right now.

$N$ can't be lower than $197$, since they would have stopped the match sooner.

So, the answer is $N = 197$.

**Testcase 4:** Sonu has won 4 sets and Titu has won 8. They have played 12 sets and Titu has been decided to be the winner.

Suppose $N = 17$, then 5 more sets are remaining and if Sonu wins them all, Sonu's score ($4 + 5 = 9$) will become greater than Titu's score of $8$. So at this point, they could not have stopped playing, and so $N$ cannot be $17$ or more.

But suppose $N = 15$, then 3 more sets are remaining and even if Sonu wins them all, he still cannot win, since $4 + 3 = 7$ is still $< 8$. So it makes sense that they stopped right now.

$N$ can't be lower than $15$, since they would have stopped the match sooner.

So, the answer is $N = 15$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 5
```

**Output for this case**

```text
9
```



#### Test case 2

**Input for this case**

```text
8 10
```

**Output for this case**

```text
19
```



#### Test case 3

**Input for this case**

```text
99 1
```

**Output for this case**

```text
197
```



#### Test case 4

**Input for this case**

```text
4 8
```

**Output for this case**

```text
15
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/BESTOFTENNIS)

[Contest: Division 1](https://www.codechef.com/START109A/problems/BESTOFTENNIS)

[Contest: Division 2](https://www.codechef.com/START109B/problems/BESTOFTENNIS)

[Contest: Division 3](https://www.codechef.com/START109C/problems/BESTOFTENNIS)

[Contest: Division 4](https://www.codechef.com/START109D/problems/BESTOFTENNIS)

***Tester:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

TBD

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

Sonu and Titu play a best of N sets match of tennis.

They will stop playing once it is clear that one player is definitely the winner, no matter the result of the following games.

You know that they stopped playing when they’d won X and Y sets, respectively. Find N.

# [](#explanation-5)EXPLANATION:

First, let’s think about when Sonu and Titu would stop playing if N is known.

If one player wins more than half the matches, the other player can never reach them so they’ll definitely stop playing.

Conversely, if both Sonu and Titu have won less than half the matches, they wouldn’t stop playing because there’s still a way for both players to win.

Why?

Suppose Sonu has A wins and Titu has B. Without loss of generality, let A \leq B.

This means there are x = N - A - B sets remaining.

Since we’re assuming both A and B are at most half of N, and N is odd, we know x \neq 0.

Clearly, if Titu wins all the remaining sets, he’ll win the overall match as well, since B+x\gt A.

However, if Sonu wins all the remaining sets, he’ll win the overall match too!

A+x = A+(N-A-B) = N-B

B was at most half of N, so N-B is greater than half of N; meaning N-B is greater than B.

So, they stop playing exactly when one player wins greater than half of the sets.

We know X and Y, and we know from above that they stopped as soon as one player won more than half of the sets.

That is, \max(X, Y) is the smallest number greater than N/2.

This tells us that N = 2\cdot\max(X, Y)-1 is the answer.

# [](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(1) per testcase.

# [](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    x, y = map(int, input().split())
    print(2*max(x,y) - 1)
``

</details>
