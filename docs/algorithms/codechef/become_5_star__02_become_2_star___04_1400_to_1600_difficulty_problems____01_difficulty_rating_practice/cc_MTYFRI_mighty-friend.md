# Mighty Friend

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MTYFRI |
| Difficulty Rating | 1406 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [MTYFRI](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/MTYFRI) |

---

## Problem Statement

Motu and Tomu are very good friends who are always looking for new games to play against each other and ways to win these games. One day, they decided to play a new type of game with the following rules:
- The game is played on a sequence $A_0, A_1, \dots, A_{N-1}$.
- The players alternate turns; Motu plays first, since he's earlier in lexicographical order.
- Each player has a score. The initial scores of both players are $0$.
- On his turn, the current player has to pick the element of $A$ with the lowest index, add its value to his score and delete that element from the sequence $A$.
- At the end of the game (when $A$ is empty), Tomu wins if he has **strictly greater** score than Motu. Otherwise, Motu wins the game.

In other words, Motu starts by selecting $A_0$, adding it to his score and then deleting it; then, Tomu selects $A_1$, adds its value to his score and deletes it, and so on.

Motu and Tomu already chose a sequence $A$ for this game. However, since Tomu plays second, he is given a different advantage: before the game, he is allowed to perform at most $K$ swaps in $A$; afterwards, the two friends are going to play the game on this modified sequence.

Now, Tomu wants you to determine if it is possible to perform up to $K$ swaps in such a way that he can win this game.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $K$ denoting the number of elements in the sequence and the maximum number of swaps Tomu can perform.
- The second line contains $N$ space-separated integers $A_0, A_1, \dots, A_{N-1}$.

### Output
For each test case, print a single line containing the string `"YES"` if Tomu can win the game or `"NO"` otherwise (without quotes).

### Constraints
- $1 \le T \le 100$
- $1 \le N \le 10,000$
- $0 \le K \le 10,000$
- $1 \le A_i \le 10,000$ for each valid $i$

### Subtasks
**Subtask #1 (20 points):** $1 \le N \le 100$

**Subtask #2 (80 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
2
6 0
1 1 1 1 1 1
5 1
2 4 6 3 4
```

**Output**

```text
NO
YES
```

**Explanation**

**Example case 1:** At the end of the game, both Motu and Tomu will have scores $1+1+1 = 3$. Tomu is unable to win that game, so the output is `"NO"`.

**Example case 2:** If no swaps were performed, Motu's score would be $2+6+4 = 12$ and Tomu's score would be $4+3 = 7$. However, Tomu can swap the elements $A_2 = 6$ and $A_3 = 3$, which makes Motu's score at the end of the game equal to $2+3+4 = 9$ and Tomu's score equal to $4+6 = 10$. Tomu managed to score higher than Motu, so the output is `"YES"`.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6 0
1 1 1 1 1 1
```

**Output for this case**

```text
NO
```



#### Test case 2

**Input for this case**

```text
5 1
2 4 6 3 4
```

**Output for this case**

```text
YES
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MTYFRI)

[Contest](https://www.codechef.com/MAY18A/problems/MTYFRI)

**Author:**  [Bhushan Khanale](https://www.codechef.com/users/bhushan_)

**Tester:**  [Suchan Park](https://www.codechef.com/users/tncks0121)

**Editorialist:**  [Suchan Park](https://www.codechef.com/users/tncks0121)

# DIFFICULTY:

Easy

# PREREQUISITES:

Sorting, Greedy argument

# PROBLEM:

Given an integer sequence A_{0}, A_{1}, \cdots, A_{N-1}, Motu’s score is the sum of elements of even indices(A_{0} + A_{2} + A_{4} + \cdots) and Tomu’s score is the sum of elements of odd indices(A_{1} + A_{3} + A_{5} + \cdots). Tomu wins iff his score is larger than Motu’s score. Tomu can swap two elements in the sequence at most K times. Can Motu win?

### QUICK EXPLANATION:

It only makes sense to swap an odd-indexed element with an even-indexed element, since otherwise the sum would be the same. For Tomu to maximize his score, he should bring the maximum odd-indexed element, and throw away the minimum even-indexed element. So Tomu can compare these two elements, and if the even-indexed element is larger, then swap these two elements at most K times. This strategy gives optimal score for Tomu every time he swaps. (i.e. If he does K swaps with this strategy, the score he gets is maximal)

### EXPLANATION:

Only odd-indexed element and even-indexed element should be swapped. Otherwise, both the score and the set of elements that Motu and Tomu have don’t change, so the swap will be useless.

Suppose the odd-indexed element is x and the even-indexed element is y. When we swap these two elements, Motu’s score is increased by x - y and Tomu’s score is increased by y - x. We can see the sum of two scores doesn’t change, so the best strategy for Tomu is to pick a pair of elements such that y - x is the largest.

Since x and y are from independent sets (odd-indexed and even-indexed), we can choose the maximum y and minimum x! When y - x is positive, Tomu’s score will increase and Tomu should definitely swap these two elements. Otherwise, there is no reason to swap. This solution is always optimal (i.e. makes Motu’s score maximal), since we can think that when we swap K times, we bring K largest elements from the Tomu’s set, and throw away K smallest elements from Motu’s set.

So, the best strategy goes like: for the k-th swap, pick the k-th largest element y from Motu’s original set and the k-th smallest element x from Tomu’s original set. If y > x, increase Tomu’s score by y - x and decrease Motu’s score by y - x. Otherwise, stop the whole process. Compare Motu’s and Tomu’s final score, and print “Yes” if Tomu is the winner.

Since both gamers’ original sets don’t change, we can sort both sets by non-increasing/non-decreasing order, and pick the k-th element from the sorted array while dealing with the k-th swap.

There can be mistakes like: not considering when K > N/2, swap exactly K times without considering whether Motu’s score is increasing or not.

### AUTHOR’S AND TESTER’S SOLUTIONS:

Author’s solution can be found [here](http://www.codechef.com/download/Solutions/MAY18/setter/RD19.cpp).

Tester’s solution can be found [here](http://www.codechef.com/download/Solutions/MAY18/tester/RD19.cpp).

Editorialist’s solution can be found [here](http://www.codechef.com/download/Solutions/MAY18/editorialist/RD19.cpp).

</details>
