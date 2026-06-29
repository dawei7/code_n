# Alternating Work Days

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ALTER |
| Difficulty Rating | 1486 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Basic Programming |
| Official Link | [ALTER](https://www.codechef.com/practice/course/2to3stars/LP2TO301/problems/ALTER) |

---

## Problem Statement

Alice and Bob are two friends. Initially, the skill levels of them are zero. They work on alternative days, i.e one of Alice and Bob works on the odd-numbered days$(1, 3, 5, \dots)$ and the other works on the even-numbered days $(2, 4, 6, \dots)$. The skill levels of Alice and Bob increase by $A, B$ respectively on the days they work.

Determine if it is possible that the skill levels of Alice and Bob become exactly $P, Q$ respectively on some day.

---

## Input Format

- The first line contains an integer $T$, denoting the number of test cases. The $T$ test cases then follow:
- The first and only line of each test case contains four space-separated integers $A, B, P, Q$.

---

## Output Format

For each test case, print `YES` if it is possible that the skill levels of Alice and Bob become exactly $P, Q$ on some day, otherwise print `NO`.

You may print each character of the string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 10^3$
- $1 \leq A, B, P, Q \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
4
1 2 1 2
1 2 3 2
4 3 4 6
3 5 9 25
```

**Output**

```text
YES
NO 
YES
NO
```

**Explanation**

**Test Case $1$:** Alice works on the first day and gains skill level $1$. Bob works on the second day and gains skill level $2$.

**Test Case $2$:** There is no possible way that the skill levels of Alice and Bob become $3$ and $2$ respectively.

 **Test Case $3$:** Bob works on the first and third day and Alice works on the second day. Hence after the third day, the skill levels of Alice and Bob become $1\cdot4 = 4$ and $2 \cdot 3 = 6$ respectively.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 2 1 2
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
1 2 3 2
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
4 3 4 6
```

**Output for this case**

```text
YES
```



#### Test case 4

**Input for this case**

```text
3 5 9 25
```

**Output for this case**

```text
NO
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)Problem Link:

[Practice](https://www.codechef.com/problems/ALTER)

[Contest: Division 1](https://www.codechef.com/LTIME101A/problems/ALTER)

[Contest: Division 2](https://www.codechef.com/LTIME101B/problems/ALTER)

[Contest: Division 3](https://www.codechef.com/LTIME101C/problems/ALTER)

***Author:*** [Soumyadeep Pal](https://www.codechef.com/users/soumyadeep_21)

***Tester:*** [Danny Mittal](https://www.codechef.com/users/tlatoani)

***Editorialist:*** [Ritesh Gupta](https://www.codechef.com/users/rishup_nitdgp)

#
[](#difficulty-2)DIFFICULTY:

Simple

#
[](#prerequisites-3)PREREQUISITES:

Math

#
[](#problem-4)PROBLEM:

Alice and Bob are two friends. Initially, the skill levels of them are zero. They work on alternative days, i.e one of Alice and Bob works on the odd-numbered days (1, 3, 5, \dots) and the other works on the even-numbered days (2, 4, 6, \dots). The skill levels of Alice and Bob increase by A, B respectively on the days they work.

Determine if it is possible that the skill levels of Alice and Bob become exactly P, Q respectively on some day.

#
[](#quick-explanation-5)QUICK EXPLANATION:

As both Alice and Bob will get same A and B skill points for working on any day. So, they can achieve only multiple of A and B respectively at any day. Now, either their score will become P and Q on any odd day or even day. If their skill level become as given on even day then both works for same number of days which implies that P/A = Q/B else the person who start the work on odd day, will contribute one more day then other which implies that P/A = Q/B + 1 if Alice start working on odd day or P/A = Q/B - 1 if Bob start working on odd day .

#
[](#explanation-6)EXPLANATION:

We can solve the problem with these observations :

- As each person will gain same amount of skill set after working for a day that means the skill set values achieved at any day should be multiple of their respective increase value (A in case of Alice and B in case of Bob).

-
P should be the multiple of A or P\%A == 0

-
Q should be the multiple of B or Q\%B == 0

- If their skill level become the desired ones on even day that means both of them worked for same amount of days irrespective of who started working first or mathematically P/A == Q/B

- If their skill level become the desired ones on odd day that means the person who started working first will be a day ahead compare to the other person.

- If Alice started working first then P/A == Q/B + 1

- If Bob started working first then P/A == Q/B - 1

#
[](#time-complexity-7)TIME COMPLEXITY:

O(1) per testcase

#
[](#code-8)CODE:

Setter (C++)
`#include
using namespace std;

void solve(int tc) {
  int a, b, p, q;
  cin >> a >> b >> p >> q;
  if (p % a == 0 && q % b == 0 && abs(p / a - q / b) <= 1) {
    cout << "YES\n";
  } else {
    cout <> t;
  for (int i = 1; i <= t; i++) solve(i);
  return 0;
}
`

Tester (Kotlin)
`import java.io.BufferedInputStream
import kotlin.math.abs

const val BILLION = 1000000000

fun main(omkar: Array) {
    val jin = FastScanner()
    repeat(jin.nextInt(1000)) {
        val a = jin.nextInt(BILLION, false)
        val b = jin.nextInt(BILLION, false)
        val p = jin.nextInt(BILLION, false)
        val q = jin.nextInt(BILLION)
        println(if (p % a == 0 && q % b == 0 && abs((p / a) - (q / b)) <= 1) "yEs" else "nO")
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
	   int a,b,p,q;
	   cin >> a >> b >> p >> q;

	   if (p%a != 0 || q%b != 0) {
	      cout << "NO\n";
	   } else if (p/a == q/b || p/a == q/b - 1 || p/a == q/b + 1) {
	      cout << "YES\n";
	   } else {
	      cout << "NO\n";
	   }
	}
	return 0;
}

`

</details>
