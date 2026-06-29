# Car Choice

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CARCHOICE |
| Difficulty Rating | 861 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [CARCHOICE](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/CARCHOICE) |

---

## Problem Statement

Chef is planning to buy a new car for his birthday. After a long search, he is left with $2$ choices:

- **Car 1**: Runs on diesel with a fuel economy of $x_1$ km/l
- **Car 2**: Runs on petrol with a fuel economy of $x_2$ km/l

Chef also knows that
- the current price of diesel is $y_1$ rupees per litre
- the current price of petrol is $y_2$ rupees per litre

Assuming that both cars cost the same and that the price of fuel remains constant, which car will minimize Chef's expenses?

Print your answer as a single integer in the following format

- If it is better to choose **Car 1**, print $-1$
- If both the cars will result in the same expenses, print $0$
- If it is better to choose **Car 2**, print $1$

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- Each test case consists of a single line containing $4$ space-separated integers — $x_1, x_2, y_1, y_2$.

---

## Output Format

For each test case, output in a single line the answer as explained earlier.

---

## Constraints

- $1 \leq T \leq 10000$
- $1 \leq x_1,x_2,y_1,y_2 \leq 50$

---

## Examples

**Example 1**

**Input**

```text
3
10 5 3 20
7 2 7 2
1 5 3 2
```

**Output**

```text
-1
0
1
```

**Explanation**

**Test Case $1$**: The cost of driving Car 1 is $\frac{3}{10} = 0.3$ rs/km, and the cost of driving Car 2 is $\frac{20}{5} = 4$ rs/km. Therefore, Car 1 is cheaper to drive, so the output is $-1$.

**Test Case $2$**: The cost of driving Car 1 is $1$ rs/km, and the cost of driving Car 2 is also $1$ rs/km. Both cars offer the same economy, so the output is $0$.

**Test Case $3$**: The cost of driving Car 1 is $3$ rs/km and the cost of driving Car 2 is $0.4$ rs/km. Therefore, Car 2 is cheaper to drive, so the output is $1$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
10 5 3 20
```

**Output for this case**

```text
-1
```



#### Test case 2

**Input for this case**

```text
7 2 7 2
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
1 5 3 2
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START28A/problems/CARCHOICE)

[Contest Division 2](https://www.codechef.com/START28B/problems/CARCHOICE)

[Contest Division 3](https://www.codechef.com/START28C/problems/CARCHOICE)

[Contest Division 4](https://www.codechef.com/START28D/problems/CARCHOICE)

Setter: [ Nandeesh Gupta](https://www.codechef.com/users/nandeesh_adm)

Tester: [Abhinav Sharma](https://www.codechef.com/users/inov_360), [Manan Grover](https://www.codechef.com/users/mexomerf)

Editorialist: [Lavish Gupta](https://www.codechef.com/users/lavish315)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef is planning to buy a new car for his birthday. After a long search, he is left with 2 choices:

-
**Car 1**: Runs on diesel with a fuel economy of x_1 km/l

-
**Car 2**: Runs on petrol with a fuel economy of x_2 km/l

Chef also knows that

- the current price of diesel is y_1 rupees per litre

- the current price of petrol is y_2 rupees per litre

Assuming that both cars cost the same and that the price of fuel remains constant, which car will minimize Chef’s expenses?

Print your answer as a single integer in the following format

- If it is better to choose **Car 1**, print -1

- If both the cars will result in the same expenses, print 0

- If it is better to choose **Car 2**, print 1

#
[](#explanation-5)EXPLANATION:

**Car 1:** It runs on diesel with a fuel economy of x_1 km/l. Current price of diesel is y_1 rupees per litre. So, Car 1 requires y_1 rupees for x_1 kilometers - \frac{y_1}{x_1} rupees for one kilometer.

**Car 2:** It runs on petrol with a fuel economy of x_2 km/l. Current price of diesel is y_2 rupees per litre. So, Car 2 requires y_2 rupees for x_2 kilometers - \frac{y_2}{x_2} rupees for one kilometer.

Using the above information, we have

- If \frac {y_1}{x_1} \lt \frac {y_2}{x_2}, then Car 1 is more economical, and answer should be -1.

- If \frac {y_1}{x_1} = \frac {y_2}{x_2}, both cars are equally economical, and answer should be 0.

- If \frac {y_1}{x_1} \gt \frac {y_2}{x_2}, then Car 2 is more economical, and answer should be 1.

Comparing two fractions

Suppose we want to compare two fractions - \frac{a}{b} and \frac{c}{d}. One of the ways is to store the values of these fraction in a floating point data type like *float* or *double*. However, this method sometime face precision issues.

Suppose we want to check if \frac{a}{b} < \frac{c}{d}.

\frac{a}{b} \lt \frac{c}{d} \implies a\cdot d \lt b \cdot c. So now, we can compare a \cdot d with b \cdot c, and this involves only integral calculations.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) for each test case.

#
[](#solution-7)SOLUTION:

Editorialist's Solution
``#include<bits/stdc++.h>
#define ll long long
#define pll pair<ll ,ll>
using namespace std ;
const ll z = 998244353 ;

int main()
{

    int t ;
    cin >> t ;
    while(t--)
    {
        int x1 , x2 , y1 , y2 ;
        cin >> x1 >> x2 >> y1 >> y2 ;

        int ans = y1*x2 - y2*x1 ;

        if(ans < 0)
            ans = -1 ;
        if(ans > 0)
            ans = 1 ;

        cout << ans << endl ;
    }

    return 0;
}
``

</details>
