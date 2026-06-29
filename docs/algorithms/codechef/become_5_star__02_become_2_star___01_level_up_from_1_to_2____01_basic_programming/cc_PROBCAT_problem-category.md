# Problem Category

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PROBCAT |
| Difficulty Rating | 860 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Basic Programming |
| Official Link | [PROBCAT](https://www.codechef.com/practice/course/1to2stars/LP1TO201/problems/PROBCAT) |

---

## Problem Statement

Chef prepared a problem. The admin has rated this problem for $x$ points.

A problem is called :

1) Easy if $1 \leq x \lt 100$

2) Medium if $100 \leq x \lt 200$

3) Hard if $200 \leq x \leq 300$

Find the category to which Chef’s problem belongs.

---

## Input Format

- The first line contains $T$ denoting the number of test cases. Then the test cases follow.
- The first and only line of each test case contains a single integer $x$.

---

## Output Format

For each test case, output in a single line the category of Chef's problem, i.e whether it is an `Easy`, `Medium` or `Hard` problem. **The output is case sensitive.**

---

## Constraints

- $1 \leq T \leq 50$
- $1 \leq x \leq 300$

---

## Examples

**Example 1**

**Input**

```text
3
50
172
201
```

**Output**

```text
Easy
Medium
Hard
```

**Explanation**

**Test case $1$**: The problem with rating $x = 50$ is an easy problem as $1 \leq 50 \lt 100$.

**Test case $2$**: The problem with rating $x = 172$ is a medium problem as $100 \leq 172 \lt 200$.

**Test case $3$**: The problem with rating $x = 201$ is a hard problem as $200 \leq 201 \leq 300$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
50
```

**Output for this case**

```text
Easy
```



#### Test case 2

**Input for this case**

```text
172
```

**Output for this case**

```text
Medium
```



#### Test case 3

**Input for this case**

```text
201
```

**Output for this case**

```text
Hard
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)Problem Link:

[Practice](https://www.codechef.com/problems/PROBCAT)

[Contest: Division 1](https://www.codechef.com/LTIME101A/problems/PROBCAT)

[Contest: Division 2](https://www.codechef.com/LTIME101B/problems/PROBCAT)

[Contest: Division 3](https://www.codechef.com/LTIME101C/problems/PROBCAT)

***Author:*** [Soumyadeep Pal](https://www.codechef.com/users/soumyadeep_21)

***Tester:*** [Danny Mittal](https://www.codechef.com/users/tlatoani)

***Editorialist:*** [Ritesh Gupta](https://www.codechef.com/users/rishup_nitdgp)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

NONE

#
[](#problem-4)PROBLEM:

You are given a number x (1 \leq x \leq 300) defining the strength of the problem. A problem is called :

-

Easy if 1 \leq x \lt 100

-

Medium if 100 \leq x \lt 200

-

Hard if 200 \leq x \leq 300

Find the category to which problem belongs.

#
[](#explanation-5)EXPLANATION:

This is a standard problem for conditional statements. We need to find the difficulty of the problem based on the above conditions. As the given number x is bounded within [1, 300] , we can write the conditions like this -

- if (x < 100) ? Easy

- else if (x < 200) ? Medium

- else ? Hard

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) for each testcase.

#
[](#code-7)CODE:

Setter (C++)
`#include
using namespace std;

void solve(int tc) {
  int n; cin >> n;
  if (n < 100) cout << "Easy\n";
  else if (n < 200) cout << "Medium\n";
  else cout <> t;
  for (int i = 1; i <= t; i++) solve(i);
  return 0;
}
`

Tester (Kotlin)
`import java.io.BufferedInputStream

fun main(omkar: Array) {
    val jin = FastScanner()
    repeat(jin.nextInt(50)) {
        val x = jin.nextInt(300)
        println(when {
            x < 100 -> "Easy"
            x < 200 -> "Medium"
            x <= 300 -> "Hard"
            else -> "Landslide"
        })
    }
    jin.endOfInput()
}

class InvalidInputException(message: String): Exception(message)

class FastScanner {
    private val BS = 1 shl 16
    private val NC = 0.toChar()
    private val buf = ByteArray(BS)
    private var bId = 0
    private var size = 0
    private var c = NC
    private var `in`: BufferedInputStream? = null
    private val validation: Boolean

    constructor(validation: Boolean) {
        this.validation = validation
        `in` = BufferedInputStream(System.`in`, BS)
    }

    constructor() : this(true)

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

    fun validationFail(message: String) {
        if (validation) {
            throw InvalidInputException(message)
        }
    }

    fun endOfInput() {
        if (char != NC) {
            validationFail("excessive input")
        }
        if (validation) {
            System.err.println("input validated")
        }
    }

    fun nextInt(from: Int, to: Int, endsLine: Boolean = true) = nextLong(from.toLong(), to.toLong(), endsLine).toInt()

    fun nextInt(to: Int, endsLine: Boolean = true) = nextInt(1, to, endsLine)

    fun nextLong(endsLine: Boolean): Long {
        var neg = false
        c = char
        if (c !in '0'..'9' && c != '-' && c != ' ' && c != '\n') {
            validationFail("found character other than digit, negative sign, space, and newline, character code = ${c.toInt()}")
        }
        if (c == '-') {
            neg = true
            c = char
        }
        var res = 0L
        while (c in '0'..'9') {
            res = (res shl 3) + (res shl 1) + (c - '0').toLong()
            c = char
        }
        if (endsLine) {
            if (c != '\n') {
                validationFail("found character other than newline, character code = ${c.toInt()}")
            }
        } else {
            if (c != ' ') {
                validationFail("found character other than space, character code = ${c.toInt()}")
            }
        }
        return if (neg) -res else res
    }

    fun nextLong(from: Long, to: Long, endsLine: Boolean = true): Long {
        val res = nextLong(endsLine)
        if (res !in from..to) {
            validationFail("$res not in range $from..$to")
        }
        return res
    }

    fun nextLong(to: Long, endsLine: Boolean = true) = nextLong(1L, to, endsLine)
}
`

Editorialist (C++)
`#include
using namespace std;

int main() {
	int t;
	cin >> t;

	while(t--) {
	   int n;
	   cin >> n;

	   if (n < 100) {
	      cout << "Easy\n";
	   } else if (n < 200) {
	      cout << "Medium\n";
	   } else {
	      cout << "Hard\n";
	   }
	}
	return 0;
}
`

</details>
