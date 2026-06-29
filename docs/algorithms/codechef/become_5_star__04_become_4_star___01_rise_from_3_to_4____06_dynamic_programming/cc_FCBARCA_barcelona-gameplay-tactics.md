# Barcelona Gameplay Tactics

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FCBARCA |
| Difficulty Rating | 1658 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Dynamic Programming |
| Official Link | [FCBARCA](https://www.codechef.com/practice/course/3to4stars/LP3TO406/problems/FCBARCA) |

---

## Problem Statement

As we all know, F.C. Barcelona is the best soccer team of our era! Their entangling and mesmerizing game style usually translates into very high ball possession, consecutive counter-attack plays and goals. Lots of goals, thanks to the natural talent of their attacker and best player in history, Lionel Andres Messi.

However, at the most prestigious tournament of individual teams, the UEFA Champions League, there are no guarantees and believe it or not, Barcelona is in trouble.... They are tied versus Chelsea, which is a very defending team that usually relies on counter-strike to catch opposing teams off guard and we are in the last minute of the match. So Messi decided to settle things down for good and now he is conducting the ball on his teams' midfield and he will start a lethal counter-attack :D

After dribbling the **2** strikers from Chelsea, he now finds himself near the center of the field and he won't be able to dribble the entire team on his own, so he will need to pass the ball to one of his teammates, run forward and receive the ball once again to score the final goal.

Exactly **K** players are with him on his counter-attack and the coach, Tito Villanova knows that this counter-attack will end in a goal only if after **exactly** **N** passes are performed between the players, Messi ends up with the ball.

 **(Note that the ball only needs to end with Messi after exactly N passes are performed between all the K+1 players, i.e. Messi can receive the ball several times during the N passes. See the 2nd test case explanation for further clarification. )**

However, he realized that there are many scenarios possible for this, so he asked you, his assistant coach, to tell him in how many ways can Messi score the important victory goal. So help him!!

### Input

Input will contain a number **T** denoting the number of test cases.

Then **T** test cases follow, each one consisting of two space-sparated integers **N** and **K**.

### Output

For each test case, output a single integer, the number of ways the winning play might happen modulo **1000000007 (109+7)**.

### Constraints

- **1** ≤ **T** ≤ **100**

- **2** ≤ **N** ≤ **1000**

- **1** ≤ **K** ≤ **10**

---

## Examples

**Example 1**

**Input**

```text
2
2 4
4 2
```

**Output**

```text
4
6
```

**Explanation**

In the first test case, say four players with Messi are Xavi, Busquets, Iniesta and Jordi Alba. Then the ways of the winning play to happen when **exactly**  2 passes are to be performed are:
1) Messi - Xavi - Messi
2) Messi - Busquets - Messi
3) Messi - Iniesta - Messi
4) Messi - Alba - Messi

In the second test case, also say that two players with Messi are Xavi and Iniesta. There are **6** ways for the winning play to happen when exactly **4** passes are performed. All the examples of such winning play are:
1) Messi - Xavi - Messi - Iniesta - Messi
2) Messi - Xavi - Iniesta - Xavi - Messi
3) Messi - Xavi - Messi - Xavi - Messi
4) Messi - Iniesta - Messi - Iniesta - Messi
5) Messi - Iniesta - Messi - Xavi - Messi
6) Messi - Iniesta - Xavi - Iniesta - Messi

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 4
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
4 2
```

**Output for this case**

```text
6
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/FCBARCA)

[Contest](http://www.codechef.com/APRIL13/problems/FCBARCA)

**Author:** [Bruno Oliveira](http://www.codechef.com/users/kuruma)

**Tester:** [Hiroto Sekido](http://www.codechef.com/users/laycurse)

**Editorialist:** [Anton Lunyov](http://www.codechef.com/users/anton_lunyov)

### DIFFICULTY:

SIMPLE

### PREREQUISITES:

Simple Math

### PROBLEM:

Let Messi have index **0**, while all other players have indexes from **1** to **K**.

Denote as **f[n][x]** the number of sequences **{a[0], a[1], …, a[n]}** of integers such that:

-
**0 ? a[j] ? K** for **j = 0, 1, 2, …, n**;

-
**a[0] = 0**, **a[n] = x**;

-
**a[j?1] ? a[j]** for **j = 1, 2, …, n**.

We need to find **f[N][0] mod P**, where **P = 1000000007**.

### QUICK EXPLANATION:

Let **K** be fixed and **g[n]** denotes **f[n][0] mod P**. Then **g[0] = 1**, **g[1] = 0** and

**g[n] = ((K ? 1) * g[n?1] + K * g[n?2]) mod P**  for **n ? 2**.

See **EXPLANATION** for proof.

So the problem can be solved using simple loop. But be careful with modular arithmetic. The following code:

``g[n] = ((long long) (K-1) * g[n-1] + (long long) K * g[n-2]) % 1000000007;
``

is safe at C++ for calculating **g[n]** for the above recurrence. Not writing `long long` will cause `int` overflow.

Alternatively the problem can be solved using formula **(KN + K * (?1)N) / (K + 1)**. But using this formula requires either inverse residue modulo **P** or arbitrary precision arithmetic. So use it on your own risk

See **ALTERNATIVE SOLUTION** for details.

### EXPLANATION:

At this section we justify recurrence for **g[n]**.

It is clear that **f[0][0] = 1** and **f[0][x] = 0** for **x = 1, …, K**.

Basic combinatorial reasoning yields that **f[n][x]** for **n > 0** is the sum of **f[n?1][y]** for all **y** from **0**  to **K**, inclusive, such that **y ? x**. Indeed, term **a[n?1]** can be any number from **0**  to **K**, inclusive, except **x**. So after fixing **y = a[n?1]** and deleting **a[n]** we get the arbitrary sequence that is counted by **f[n?1][y]**.

The constraints are very soft. So even such quadratic DP will pass the TL, but we continue further.

It is clear that **f[n][1] = f[n][2] = … = f[n][K]** since all players except Messy are non-distinguishable by the above definition. Hence denoting **g[n] = f[n][0]** and **h[n] = f[n][1]** we can get the following formulas for **g[n]** and **h[n]**:

**g[n] = f[n][0] = f[n?1][1] + … + f[n?1][K] = K * h[n?1]**;

**h[n] = f[n][1] = f[n?1][0] + f[n?1][2] + … + f[n?1][K] = g[n?1] + (K?1) * h[n?1]**.

Summarizing we get:

**g[0] = 1**, **h[0] = 0**,

**g[n] = K * h[n?1]**,

**h[n] = g[n?1] + (K?1) * h[n?1]**.

By theses formulas we already get simple **O(N)** solution (refer to the [tester’s solution](http://www.codechef.com/download/Solutions/2013/April/Tester/FCBARCA.cpp)).

But we can get another simplification.

Multiplying formula for **h[n]** by **K** we get:

**K * h[n] = K * g[n?1] + (K?1) * (K * h[n?1])**.

Note that **K * h[n] = g[n+1]** and **K * h[n?1] = g[n]**.

Hence we get

**g[n+1] = K * g[n?1] + (K?1) * g[n]** for **n > 1**.

Together with **g[1] = K * h[0] = 0** we get the solution described in the **QUICK EXPLANATION** section.

Note also that using [exponentiation by squaring](http://en.wikipedia.org/wiki/Exponentiation_by_squaring) for **2 × 2** matrices we can solve the problem in **O(log N)** time using recurrent formulas for **g[n]** and **h[n]**. Most of the related problems listed below require similar considerations but also require some advanced technique like exponentiation by squaring in the end.

### ALTERNATIVE SOLUTION:

Here we prove the explicit formula mentioned in the **QUICK EXPLANATION** section.

We apply the basic theory of [linear homogeneous recurrence relations with constant coefficients](http://en.wikipedia.org/wiki/Recurrence_relation#Linear_homogeneous_recurrence_relations_with_constant_coefficients) to the recurrent sequence **g[n]**. For this we write down the characteristic polynomial:

**p(t) = t2 ? (K?1) * t ? K**.

Its roots are **r1 = ?1** and **r2 = K**. Hence the general solution for this recurrence is

**g[n] = C1 * r1N + C2 * r2N = C1 * (?1)N + C2 * KN**.

Constants **C1** and **C2** can be found from relations **g[0] = 1**, **g[1] = 0**.

Namely, substituting **n = 0** and **n = 1** to the general form of **g[n]** we get

**
 C1 + C2 = 1;
?C1 + K * C2 = 0.
**

Solving this **2 × 2** system we get **C1 = K / (K + 1)** and **C2 = 1 / (K + 1)**.

Hence **g[n] = (Kn + K * (?1)n) / (K + 1)** and we are done.

The simplest way to use this formula is to use language with built-in arbitrary precision arithmetic like Java or Python and calculate the above expression directly and then take it modulo **P** in the end.

### AUTHOR’S AND TESTER’S SOLUTIONS:

Author’s solution can be found [here](http://www.codechef.com/download/Solutions/2013/April/Setter/FCBARCA.cpp).

Tester’s solution can be found [here](http://www.codechef.com/download/Solutions/2013/April/Tester/FCBARCA.cpp).

### RELATED PROBLEMS:

[Codeforces Round #113 (Div. 2) - Problem E - Tetrahedron](http://www.codeforces.com/problemset/problem/166/E)

[NEWSCH](http://www.codechef.com/problems/NEWSCH)

[CKISSHUG](http://www.codechef.com/problems/CKISSHUG)

[CROWD](http://www.codechef.com/problems/CROWD)

[CSUMD](http://www.codechef.com/problems/CSUMD)

[CHESSGM](http://www.codechef.com/problems/CHESSGM/)

[HAREJUMP](http://www.codechef.com/problems/HAREJUMP/)

[CAKEDOOM](http://www.codechef.com/problems/CAKEDOOM)

</details>
