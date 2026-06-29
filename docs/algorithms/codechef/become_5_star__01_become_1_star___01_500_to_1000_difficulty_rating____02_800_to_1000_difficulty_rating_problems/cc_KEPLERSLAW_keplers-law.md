# Keplers Law

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | KEPLERSLAW |
| Difficulty Rating | 992 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [KEPLERSLAW](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/KEPLERSLAW) |

---

## Problem Statement

Kepler’s Law states that the planets move around the sun in elliptical orbits with the sun at one focus. Kepler's 3rd law is The Law of Periods, according to which:

- The **square of the time period** of the planet is directly proportional to the **cube of the semimajor axis** of its orbit.

You are given the Time periods ($T_1, T_2$) and Semimajor Axes ($R_1, R_2$) of two planets orbiting the same star.

Please determine if the Law of Periods is satisfied or not, i.e, if the [constant of proportionality](https://en.wikipedia.org/wiki/Proportionality_(mathematics)) of both planets is the same.

Print `"Yes"` (without quotes) if the law is satisfied, else print `"No"`.

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- Each test case consists a single line of input, containing four space-separated integers $T_1, T_2, R_1, R_2$.

---

## Output Format

For each test case, output a single line containing one string — `"Yes"` or `"No"` (without quotes); the answer to the problem.

You may print each character of the answer in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq T_1,T_2 \leq 10$
- $1 \leq R_1,R_2 \leq 10$

---

## Examples

**Example 1**

**Input**

```text
3
1 1 1 1
1 2 3 4
1 8 2 8
```

**Output**

```text
Yes
No
Yes
```

**Explanation**

- **Test Case $1$**: $1^2/1^3 = 1^2/1^3$
- **Test Case $2$**: $1^2/3^3 \neq 2^2/4^3$
- **Test Case $3$**: $1^2/2^3 =  8^2/8^3$

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 1 1 1
```

**Output for this case**

```text
Yes
```



#### Test case 2

**Input for this case**

```text
1 2 3 4
```

**Output for this case**

```text
No
```



#### Test case 3

**Input for this case**

```text
1 8 2 8
```

**Output for this case**

```text
Yes
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/JAN221A/problems/KEPLERSLAW)

[Contest Division 2](https://www.codechef.com/JAN221B/problems/KEPLERSLAW)

[Contest Division 3](https://www.codechef.com/JAN221C/problems/KEPLERSLAW)

**Setter:** [Srikkanth R](https://www.codechef.com/users/srikkanth_adm)

**Tester:** [Venkata Nikhil Medam](https://www.codechef.com/users/nikhil_medam), [Tejas Pandey](https://www.codechef.com/users/tejas10p)

**Editorialist:** [Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Kepler’s Law of Period states - “The square of the time period of the planet is directly proportional to the cube of the semimajor axis of its orbit.”

Given the Time periods (T_1, T_2) and Semimajor Axes (R_1, R_2) of two planets orbiting the same star, determine if the Law of Periods is satisfied.

#
[](#quick-explanation-5)QUICK EXPLANATION:

The Law of Periods is satisfied when  {T_1}^2 \cdot {R_2}^3 = {T_2}^2 \cdot {R_1}^3.

#
[](#explanation-6)EXPLANATION:

Let T denote the time period of the planet and R denote the length of the semimajor axis of its orbit. Then, according to Kepler’s Law of Periods, T^2 ? R^3. In other words, the ratio \frac{T^2}{R^3} = K, is a constant, also known as *Kepler’s Constant*.

We are given the values of (T, R) for two planets. Those are, (T_1, R_1) for planet 1 and (T_2, R_2) for planet 2. The respective Kepler’s Constants are K_1 = \frac{{T_1}^2}{{R_1}^3}, and K_2 = \frac{{T_2}^2}{{R_2}^3}.

For both the planets to follow Kepler’s Law, the value of both the constants should be same.

In other words,  \frac{{T_1}^2}{{R_1}^3} =  \frac{{T_2}^2}{{R_2}^3}.

**Comparing the ratios:** If we compare the ratios, we need to keep in mind that the data types of the variables is float/double. If we declare them as integers, the ratios are rounded down to the nearest integer which results in a wrong answer.

Another way is to cross multiply  the denominators and check if  {T_1}^2 \cdot {R_2}^3 = {T_2}^2 \cdot {R_1}^3. This works even when the data type is integer.

#
[](#time-complexity-7)TIME COMPLEXITY:

The time complexity is O(1) per test case.

#
[](#solution-8)SOLUTION:

Tester's Solution
``#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;
    while(t--) {
        int t1,t2,r1,r2;
        cin >> t1 >> t2 >> r1 >> r2;
        int ok = 0;
        ok = (t1*t1*r2*r2*r2 == t2*t2*r1*r1*r1);
        cout << (ok?"YES\n":"NO\n");
    }
}
``

Editorialist's Solution
``#include <bits/stdc++.h>
using namespace std;

#define sync {ios_base ::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);}
#define rep(n) for(int i = 0;i<n;i++)
#define rep1(a,b) for(int i = a;i<b;i++)
#define int long long int
#define mod 1000000007

int t1, t2, r1, r2;

void solve()
{
    cin>>t1>>t2>>r1>>r2;

    int product1 = (t1*t1)*(r2*r2*r2);
    int product2 = (t2*t2)*(r1*r1*r1);

    if(product1 == product2){
        cout<<"Yes";
    }
    else{
        cout<<"No";
    }
}

int32_t main()
{

    #ifndef ONLINE_JUDGE
        freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
    #endif

    sync;
    int t = 1;
    cin>>t;
    while(t--){
        solve();
        cout<<"\n";
    }
    return 0;
}
``

</details>
