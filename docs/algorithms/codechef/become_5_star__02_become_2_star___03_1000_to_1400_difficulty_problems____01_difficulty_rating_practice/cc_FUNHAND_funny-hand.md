# Funny Hand

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FUNHAND |
| Difficulty Rating | 1306 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [FUNHAND](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/FUNHAND) |

---

## Problem Statement

MoEngage has $3$ decks. Each deck consists of $N$ cards, numbered from $1$ to $N$. He draws out $1$ card from each deck randomly with each card having an equal probability of being drawn.

MoEngage drew cards numbered $A$ and $B$ from the decks $1$ and $2$ respectively. Now, he wonders what is the probability that he will end up with a *funny hand* after drawing the third card.

A *funny hand* is when $3$ **consecutive** numbered cards are present in your hand.
Help MoEngage calculate the probability of ending up with a *funny hand* after drawing the third card.

If the final probability of ending up with a *funny hand* is $P$, you need to print the value $P\cdot N$. It can be shown that this value is an integer.

---

## Input Format

- First line will contain $T$, the number of test cases. Then the test cases follow.
- Each test case contains a single line of input consisting of three space-separated integers $N, A,$ and $B$ denoting the size of each deck, the card drawn from the first deck, and the card drawn from the second deck respectively.

---

## Output Format

For each test case, output a single integer, denoting $P\cdot N$ on a separate line.

---

## Constraints

- $1 \leq T \leq 1000$
- $3 \leq N \leq 1000$
- $1 \leq A, B \leq N$

---

## Examples

**Example 1**

**Input**

```text
3
4 2 3
6 2 1
5 2 5
```

**Output**

```text
2
1
0
```

**Explanation**

**Test case $1$:** Drawing the cards $1$ or $4$ will result in a funny hand. Hence, the probability will be $P = \frac{1}{2}$. The value $P \cdot N = \frac{1}{2} \cdot 4 = 2$.

**Test case $2$:** Drawing the card $3$ will result in a funny hand. Hence, the probability will be $P = \frac{1}{6}$. The value $P \cdot N = \frac{1}{6} \cdot 6 = 1$.

**Test case $3$:** No matter what card MoEngage draws, he will never end up with a funny hand.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 2 3
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
6 2 1
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
5 2 5
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/COOK140A/problems/FUNHAND)

[Contest Division 2](https://www.codechef.com/COOK140B/problems/FUNHAND)

[Contest Division 3](https://www.codechef.com/COOK140C/problems/FUNHAND)

[Contest Division 4](https://www.codechef.com/COOK140D/problems/FUNHAND)

Setter: [Tejas Pandey](https://www.codechef.com/users/tejas_adm)

Tester: [Harris Leung](https://www.codechef.com/users/gamegame)

Editorialist: [Jakub Safin](https://www.codechef.com/users/xellos), [Pratiyush Mishra](https://www.codechef.com/users/foxy7)

#
[](#difficulty-2)DIFFICULTY:

Easy

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef has 3 decks consisting of N cards each, numbered from 1 to N. He draws out 1 card from each deck randomly with each card having an equal probability of being drawn.

Chef drew cards numbered A and B from the first 2 decks respectively. Now he wonders what is the probability that he will end up with a funny hand after drawing the third card.

A funny hand is when 3 consecutive numbered cards are present in your hand. Please help Chef calculate the probability of ending up with a funny hand after drawing the last card.

If the final probability of ending up with a funny hand is P. You need to print P?N, it can be shown that this value is an integer.

#
[](#explanation-5)EXPLANATION:

For a particular test case, three integers N, A and B are taken as inputs. The cards in a deck are numbered from 1 to N and, A, B are the numbers on cards drawn from the first 2 decks.

For possibility of forming a funny hand 3 cases are possible:

- The third drawn card number is the smallest and A, B are consecutive. In this case the third number takes the value which is minimum of A and B minus 1.

- The third drawn card number is the largest and A, B are consecutive. In this case the third number takes the value which is maximum of A and B plus 1.

- The third drawn card number lies between A and B and all three are consecutive.

Also the values on cards are between 1 and N so smallest number in a consecutive sequence can be 1  and the largest being N.

All the above possibilities need to be checked to find the total possible cases for forming a funny hand.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) for each test case.

#
[](#solution-7)SOLUTION:

[Editorialist’s Solution](https://p.ip.fi/P3_Z)

[Setter’s Solution](https://p.ip.fi/IXpr)

[Tester’s Solution](https://p.ip.fi/EqsU)

</details>
