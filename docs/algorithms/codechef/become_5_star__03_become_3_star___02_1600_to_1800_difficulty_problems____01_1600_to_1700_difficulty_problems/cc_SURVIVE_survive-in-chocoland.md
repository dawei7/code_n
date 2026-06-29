# Survive in ChocoLand

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SURVIVE |
| Difficulty Rating | 1616 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [SURVIVE](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/SURVIVE) |

---

## Problem Statement

You are a poor person in ChocoLand. Here, people eat chocolates daily instead of normal food. There is only one shop near your home; this shop is closed on Sunday, but open on all other days of the week. You may buy **at most one** box of **N** chocolates from this shop on each day when it is open.

Currently, it's Monday, and you need to survive for the next **S** days (including the current day). You have to eat **K** chocolates everyday (including the current day) to survive. Do note that you are allowed to buy the a chocolate box and eat from it on the same day.

Compute the minimum number of days on which you need to buy from the shop so that you can survive the next **S** days, or determine that it isn't possible to survive.

### Input

- The first line of the input contains a single integer **T** denoting the number of test cases. The description of **T** test cases follows.

- The first and only line of each test case contains 3 integers **N**, **K** and **S** denoting the number of chocolates in a box, the number of chocolates you have to eat everyday to survive and the number of days you need to survive.

### Output

For each test case, print a single line containing one integer — the minimum number of days on which you need to buy from the shop to survive, or -1 if you will not be able to survive **S** days.

### Constraints

- 1 ≤ **T** ≤ 100

- 1 ≤ **N** ≤ 100

- 1 ≤ **K** ≤ 100

- 1 ≤ **S** ≤ 1000

---

## Examples

**Example 1**

**Input**

```text
2
16 2 10
50 48 7
```

**Output**

```text
2
-1
```

**Explanation**

**Example case 1:** One possible solution is to buy a box on day 1 (Monday); it's sufficient to eat from this box up to day 8 (Monday) inclusive. Now, on day 9 (Tuesday), you buy another box and use the chocolates in it to survive days 9 and 10.

**Example case 2:** You will not be able to survive even if you buy from the shop everyday except every 7-th day.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
16 2 10
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
50 48 7
```

**Output for this case**

```text
-1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](https://www.codechef.com/problems/SURVIVE)

[Contest](https://www.codechef.com/COOK90/problems/SURVIVE)

**Author:** [Sidhant Bansal](https://www.codechef.com/users/sidhant007)

**Testers:** [Hasan Jaddouh](https://www.codechef.com/users/kingofnumbers)

**Editorialist:** [Sidhant Bansal](https://www.codechef.com/users/sidhant007)

### DIFFICULTY:

easy

### PREREQUISITES:

basic math

### PROBLEM:

In this problem, the greedy approach of buying the box of chocolate for some consecutive early days is the right direction.

Let A = K * S and B = N * (S - S/7), here A denotes the total number of chocolates we need to eat and B denotes the maximum no. of chocolates we can buy. Here S - S/7 denotes the number of days the shop is open.

So if A > B or ((N - K) * 6 < K and S \geq 7), then the answer is -1.

otherwise the answer is ceil(\frac{A}{N}), where ceil(x) denotes ceiling function on x.

The first condition i.e A > B, for -1 is fairly obvious that if the total no. of chocolates we need to eat is more than we can buy at max then it is invalid.

The second condition i.e (N - K) * 6 < K and S \geq 7 is a bit tricky, it is basically the contrapositive of the statement, “if you can survive the first 7 days, then you can survive any given number of days”. So the contrapositive (i.e same statement in different words) is "if you cannot survive the first 7 days then you won’t be able to survive for S \geq 7". The condition for being able to survive on the 7^{th} day is basically if we add our remaining chocolates from the first 6 days, i.e (N - K) * 6 and it is still smaller than K, i.e the chocolates we need for the 7^{th} day, then we don’t survive. But we only need to test this when S \geq 7.

Incase, we are able to survive, then the answer is ceil(\frac{A}{N}), which is basically total number of chocolates we need to eat divided by the number of chocolates we can buy in a single day (and if a remainder exists, then we need to buy one more day). This portion is pretty straightforward.

The above reasoning to check for -1 is obviously tricky and a simpler approach exists which is to just simulate the days once we know the value of ceil(\frac{A}{N}).

### SOLUTIONS

[Setter’s solution](https://www.codechef.com/download/Solutions/COOK90/Setter/SURVIVE.cpp).

[Tester’s solution](https://www.codechef.com/download/Solutions/COOK90/Tester/SURVIVE.cpp).

</details>
