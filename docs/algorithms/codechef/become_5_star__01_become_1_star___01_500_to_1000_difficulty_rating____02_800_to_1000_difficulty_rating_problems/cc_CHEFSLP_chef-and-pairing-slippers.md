# Chef and Pairing Slippers

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFSLP |
| Difficulty Rating | 930 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [CHEFSLP](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/CHEFSLP) |

---

## Problem Statement

Chef has $N$ slippers, $L$ of which are left slippers and the rest are right slippers. Slippers must always be sold in pairs, where each pair contains one left and one right slipper. If each pair of slippers cost $X$ rupees, what is the maximum amount of rupees that Chef can get for these slippers?

---

## Input Format

- The first line contains $T$ - the number of test cases. Then the test cases follow.
- The first line of each test case contains three space-separated integers $N$, $L$, and $X$ - the total number of slippers, the number of left slippers, and the price of a pair of slippers in rupees.

---

## Output Format

For each test case, output on one line the maximum amount of rupees that Chef can get by selling the slippers that are available.

---

## Constraints

- $1 \leq T \leq 10^3$
- $0 \leq L \leq N \leq 10^3$
- $0 \leq X \leq 10^3$

---

## Examples

**Example 1**

**Input**

```text
4
0 0 100
10 1 0
1000 10 1000
10 7 1
```

**Output**

```text
0
0
10000
3
```

**Explanation**

- **Test case $1$:** Chef has no pairs to sell, so the amount obtained is $0$.
- **Test case $2$:** The amount earned by selling a pair is $0$, so the total amount obtained is $0$.
- **Test case $3$:** Chef can sell $10$ pairs of slippers, each giving $1000$ rupees, so the total amount earned is $1000 \cdot 10 = 10000$.
- **Test case $4$:** Chef has $10$ slippers of which $7$ are left and $3$ are right. Therefore Chef can sell a maximum of $3$ pairs and in total can get at most $3 \cdot 1 = 3$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
0 0 100
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
10 1 0
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
1000 10 1000
```

**Output for this case**

```text
10000
```



#### Test case 4

**Input for this case**

```text
10 7 1
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CHEFSLP)

[Contest: Division 1](https://www.codechef.com/COOK134A/problems/CHEFSLP)

[Contest: Division 2](https://www.codechef.com/COOK134B/problems/CHEFSLP)

[Contest: Division 3](https://www.codechef.com/COOK134C/problems/CHEFSLP)

***Author:*** [Utkarsh Gupta](https://www.codechef.com/users/Utkarsh_25dec)

***Tester:*** [Danny Mittal](https://www.codechef.com/users/tlatoani)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef has N slippers, of which L are left slippers and the rest are right slippers. Slippers need to be sold in pairs of one left and one right slipper. If each pair sells for X, how much can Chef earn at maximum?

#
[](#quick-explanation-5)QUICK EXPLANATION:

The answer is X\cdot min(L, N-L).

#
[](#explanation-6)EXPLANATION:

There are L left slippers and N slippers in total, which leaves N-L right slippers.

Each pair of slippers sold consists of one left and one right slipper. So, Chef certainly cannot sell more pairs than there are left slippers, or more pairs than there are right slippers. This means that Chef can sell at most \min(L, N-L) pairs of slippers.

Further, this upper bound is attainable, i.e, Chef can definitely sell \min(L, N-L) pairs - for example, if there are less left slippers than right slippers, pair up each left slipper with a right slipper.

So, Chef is able to sell \min(L, N-L) slippers, each for rupees X. Chef’s maximum earning is hence X\cdot\min(L, N-L).

#
[](#time-complexity-7)TIME COMPLEXITY:

\mathcal{O}(1) per test.

#
[](#code-8)CODE:

Tester (Kotlin)
``import java.io.BufferedInputStream
import kotlin.math.min

fun main(omkar: Array<String>) {
    val jin = FastScanner()
    repeat(jin.nextInt(1000)) {
        val n = jin.nextInt(0, 1000, false)
        val l = jin.nextInt(0, n, false)
        val x = jin.nextInt(0, 1000)
        println(x * min(l, n - l))
    }
    jin.assureInputDone()
}

class FastScanner {
    private val BS = 1 shl 16
    private val NC = 0.toChar()
    private val buf = ByteArray(BS)
    private var bId = 0
    private var size = 0
    private var c = NC
    private var `in`: BufferedInputStream? = null

    constructor() {
        `in` = BufferedInputStream(System.`in`, BS)
    }

    private val char: Char
        private get() {
            while (bId == size) {
                size = try {
                    `in`!!.read(buf)
                } catch (e: Exception) {
                    return NC
                }
                if (size == -1) return NC
                bId = 0
            }
            return buf[bId++].toChar()
        }

    fun assureInputDone() {
        if (char != NC) {
            throw IllegalArgumentException("excessive input")
        }
    }

    fun nextInt(endsLine: Boolean): Int {
        var neg = false
        c = char
        if (c !in '0'..'9' && c != '-' && c != ' ' && c != '\n') {
            throw IllegalArgumentException("found character other than digit, negative sign, space, and newline")
        }
        if (c == '-') {
            neg = true
            c = char
        }
        var res = 0
        while (c in '0'..'9') {
            res = (res shl 3) + (res shl 1) + (c - '0')
            c = char
        }
        if (endsLine) {
            if (c != '\n') {
                throw IllegalArgumentException("found character other than newline")
            }
        } else {
            if (c != ' ') {
                throw IllegalArgumentException("found character other than space")
            }
        }
        return if (neg) -res else res
    }

    fun nextInt(from: Int, to: Int, endsLine: Boolean = true): Int {
        val res = nextInt(endsLine)
        if (res !in from..to) {
            throw IllegalArgumentException("$res not in range $from..$to")
        }
        return res
    }

    fun nextInt(to: Int, endsLine: Boolean = true) = nextInt(1, to, endsLine)
}
``

Editorialist (Python)
``for _ in range(int(input())):
    n, l, x = map(int, input().split())
    print(x*min(l, n - l))
``

</details>
