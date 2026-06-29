# Odd Sum

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ODDSUM |
| Difficulty Rating | 1600 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [ODDSUM](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/ODDSUM) |

---

## Problem Statement

Given an integer $N$, consider all arrays $A$ of size $N$ such that:

- All the elements are non-negative and distinct.
- All prefix sums are odd. Formally, for all $i$ such that $1 \le i \le N$, $\sum_{j=1}^i A_j$ is odd.

Among all possible arrays $A$, output the smallest possible sum of the elements of the array.

**Note**: Since the Input/Output may be large, it is preferred to use fast I/O.

---

## Input Format

- The first line contains $T$ - the number of test cases. Then the test cases follow.
- The first line of each test case contains $N$ - the size of the array.

---

## Output Format

For each test case, output on one line the smallest sum among all arrays satisfying the constraints.

---

## Constraints

- $1 \leq T \leq 10^6$
- $1 \leq N \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
1
3
```

**Output**

```text
3
```

**Explanation**

- **Test case $1$**: A possible array is $[1, 2, 0]$. $[1, 0, 0]$ is not valid because $0$ occurs twice in it; $[0, 1, 2]$ is not valid because the prefix sum until the first index is $0$, which is even. Another possible array is $[5, 2, 4]$.
$[1, 2, 0]$ yields the sum $3$, and we can prove that there are no valid arrays that have sum less than $3$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/ODDSUM)

[Contest: Division 1](https://www.codechef.com/COOK134A/problems/ODDSUM)

[Contest: Division 2](https://www.codechef.com/COOK134B/problems/ODDSUM)

[Contest: Division 3](https://www.codechef.com/COOK134C/problems/ODDSUM)

***Author:*** [Rahul Kumar](https://www.codechef.com/users/rahularya1)

***Tester:*** [Danny Mittal](https://www.codechef.com/users/tlatoani)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

SImple

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given N, consider all arrays of length N consisting of non-negative and distinct integers whose prefix sums are all odd. Output the minimum sum of elements of such an array.

#
[](#quick-explanation-5)QUICK EXPLANATION

One possible array is A = [1, 0, 2, 4, \dots, 2N-2], whose sum is 1 + (N-1)(N-2).

#
[](#explanation-6)EXPLANATION:

First, note that the condition on all prefix sums being odd tells us that:

-
A_1 is odd

-
A_i is even for i > 1

There is only one odd number in the array, and we want to minimize the total sum. It is thus optimal to choose the smallest odd integer we can; that being 1.

The remaining N-1 elements must all be even and distinct. Once again, it is obviously optimal to choose the smallest N-1 even elements we can, which turns out to be \{0, 2, 4, 6, \dots, 2N - 4\}.

Now we know all the elements of the array, all that remains is to find their sum. Note that

0 + 2 + 4 + \dots + 2N-4 = 2\cdot (0 + 1 + 2 + \dots N-2) \\
= 2\cdot \frac{(N-2)(N-1)}{2} \\ = (N-2)(N-1)

So, the final answer turns out to be 1 + (N-2)(N-1).

###
[](#a-lesson-about-endl-7)A lesson about `endl`

This problem had rather high constraints - in most languages, the default method of taking input and printing output will likely time out, and the statement had a note asking participants to use faster methods.

However, there is one more pitfall here, specifically in `C++` - and that is the use of `endl`.

The standard way of speeding up i/o in `C++` via adding the lines

``ios::sync_with_stdio(0);
cin.tie(0);
``

speeds up output by ensuring that the output buffer is not flushed every time `cin` is called (which is what `cin.tie(0)` does).

However, `endl` always forces a flush of the buffer, so using it essentially nullifies any benefit you had in the first place.

The workaround is to always use `\n` instead of `endl`.

#
[](#time-complexity-8)TIME COMPLEXITY:

\mathcal{O}(1) per test.

#
[](#code-9)CODE:

Setter (C++)
``#include<bits/stdc++.h>
using namespace std;
#define fio ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define int long long int
#define vi vector<int>
#define w(x) int x; cin>>x; while(x--)
#define pb push_back

int32_t main() {
    #ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
    fio
    w(t)
    {
        int n;
        cin>>n;
        cout<<(n-1)*(n-2)+1<<"\n";
    }
}
``

Tester (Kotlin)
``import java.io.BufferedInputStream

fun main(omkar: Array<String>) {
    val jin = FastScanner()
    val out = StringBuilder()
    repeat(jin.nextInt(1000000)) {
        val n = jin.nextInt(1000000000).toLong()
        val answer = ((n - 1L) * (n - 2L)) + 1L
        out.appendln(answer)
    }
    print(out)
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
``import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    print(1 + (n-1)*(n-2))
``

</details>
