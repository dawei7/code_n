# DDMM or MMDD

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DDMMORMMDD |
| Difficulty Rating | 992 |
| Difficulty Band | Practice Strings |
| Path | Data Structures and Algorithms |
| Lesson | Strings |
| Official Link | [DDMMORMMDD](https://www.codechef.com/practice/course/strings/STRINGS/problems/DDMMORMMDD) |

---

## Problem Statement

Chef is confused by all the different formats dates can be written in. Here's a simple problem Chef wants you to solve.

You are given a date string $S$. The date follows the [Gregorian calendar](https://en.wikipedia.org/wiki/Gregorian_calendar), the one used in most parts of the world.

Identify whether it is of the form `DD/MM/YYYY` or `MM/DD/YYYY`, or if it can be of both forms. Here `DD` denotes the 2-digit day, `MM` denotes the 2-digit month and `YYYY` denotes the 4-digit year.

It is guaranteed that $S$ is a valid date taking at least one of these forms.

For example,
- `21/05/2001` is of the form `DD/MM/YYYY` and not `MM/DD/YYYY`.
- `10/15/2069` is of the form `MM/DD/YYYY` and not `DD/MM/YYYY`.
- `05/11/1999` can be of both forms.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- Each test case consists of a single line containing a string of $10$ characters $S$ — the date string $S$, which is of the form `DD/MM/YYYY` or `MM/DD/YYYY`. It is guaranteed that $S$ is a valid date taking at least one of these forms.

---

## Output Format

For each test case, output "`BOTH`" if the date string satisfies both forms. Otherwise output "`DD/MM/YYYY`" if it is of the form `DD/MM/YYYY`, else "`MM/DD/YYYY`". Note that the output may be case-insensitive. So "`DD/MM/YYYY`", "`dd/mm/yyyy`" and so on will be considered the same.

---

## Constraints

- $1 \leq T \leq 2023$
- $S$ is of the form `DD/MM/YYYY` or `MM/DD/YYYY`

---

## Examples

**Example 1**

**Input**

```text
4
21/05/2001
10/15/2069
05/11/1999
29/02/2024
```

**Output**

```text
DD/MM/YYYY
MM/DD/YYYY
BOTH
DD/MM/YYYY
```

**Explanation**

Fun fact: `29/02/2024` (read as `DD/MM/YYYY`) is a leap year day.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
21/05/2001
```

**Output for this case**

```text
DD/MM/YYYY
```



#### Test case 2

**Input for this case**

```text
10/15/2069
```

**Output for this case**

```text
MM/DD/YYYY
```



#### Test case 3

**Input for this case**

```text
05/11/1999
```

**Output for this case**

```text
BOTH
```



#### Test case 4

**Input for this case**

```text
29/02/2024
```

**Output for this case**

```text
DD/MM/YYYY
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/DDMMORMMDD)

[Contest: Division 1](https://www.codechef.com/START89A/problems/DDMMORMMDD)

[Contest: Division 2](https://www.codechef.com/START89B/problems/DDMMORMMDD)

[Contest: Division 3](https://www.codechef.com/START89C/problems/DDMMORMMDD)

[Contest: Division 4](https://www.codechef.com/START89D/problems/DDMMORMMDD)

***Author:*** [the_hyp0cr1t3](https://www.codechef.com/users/the_hyp0cr1t3)

***Tester & Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

992

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given a date string, decide whether it’s of the form `DD/MM/YYYY`, `MM/DD/YYYY`, or can be either.

It’s guaranteed that the given date is valid in at least one of the forms.

#
[](#explanation-5)EXPLANATION:

Since the given date is valid in at least one form, there’s a rather simple solution that doesn’t involve any ugly casework with days-per-month and such.

Let x denote the number formed by the first two digits in the input, and y denote the number formed by the next two digits.

So for example, if `S = 12/24/2051` then we have x = 12 and y = 24.

Then,

- If 1 \leq x \leq 12 and 1 \leq y \leq 12, the date can be both `DD/MM/YYYY` or `MM/DD/YYYY`.

- Otherwise, exactly one of x and y must denote the month, so:

- If 1 \leq x \leq 12, the answer is `MM/DD/YYYY`

- Else, the answer is `DD/MM/YYYY`

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Author's code (C++)
``#include <iostream>

int main() {
    int tests;
    std::cin >> tests;
    while (tests--) {
        std::string s;
        std::cin >> s;
        int x = (s[0] - '0') * 10 + (s[1] - '0');
        int y = (s[3] - '0') * 10 + (s[4] - '0');
        if (x <= 12 and y <= 12)
            std::cout << "BOTH" << '\n';
        else if (y <= 12)
            std::cout << "DD/MM/YYYY" << '\n';
        else
            std::cout << "MM/DD/YYYY" << '\n';
    }
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    s = input()
    x, y = int(s[0:2]), int(s[3:5])
    if 1 <= x <= 12 and 1 <= y <= 12: print('Both')
    elif 1 <= x <= 12: print('MM/DD/YYYY')
    else: print('DD/MM/YYYY')
``

</details>
