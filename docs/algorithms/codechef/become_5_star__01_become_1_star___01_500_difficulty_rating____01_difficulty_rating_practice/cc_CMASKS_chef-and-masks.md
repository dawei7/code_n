# Chef and Masks

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CMASKS |
| Difficulty Rating | 432 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [CMASKS](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CMASKS) |

---

## Problem Statement

Chef is shopping for masks. In the shop, he encounters $2$ types of masks:

- Disposable Masks — cost $X$ but last only $1$ day.
- Cloth Masks — cost $Y$ but last $10$ days.

Chef wants to buy masks to last him $100$ days. He will buy the masks which cost him the least. In case there is a tie in terms of cost, Chef will be eco-friendly and choose the cloth masks. Which type of mask will Chef choose?

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases. Then the test cases follow.
- Each test case consists of a single line of input, containing two space-separated integers $X, Y$.

---

## Output Format

For each test case, if Chef buys the cloth masks print `CLOTH`, otherwise print `DISPOSABLE`.

You may print each character of the string in uppercase or lowercase (for example, the strings `cloth`, `clOTh`, `cLoTH`, and `CLOTH` will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 5000$
- $1 \leq X \lt Y \leq 100$

---

## Examples

**Example 1**

**Input**

```text
4
10 100
9 100
88 99
1 11
```

**Output**

```text
Cloth
Disposable
Cloth
Disposable
```

**Explanation**

**Test case $1$:** The cost of the disposable masks will be $10 \cdot 100 = 1000$, while the cost of the cloth masks will be $100 \cdot 10 = 1000$. Since the price is equal and Chef is eco-friendly, Chef will buy the cloth masks.

**Test case $2$:** The cost of the disposable masks will be $9 \cdot 100 = 900$, while the cost of the cloth masks will be $100 \cdot 10 = 1000$. Since the price of disposable masks is less, Chef will buy the disposable masks.

**Test case $3$:** The cost of the disposable masks will be $88 \cdot 100 = 8800$, while the cost of the cloth masks will be $99 \cdot 10 = 990$. Since the price of the cloth masks is less, Chef will buy the cloth masks.

**Test case $4$:** The cost of the disposable masks will be $1 \cdot 100 = 100$, while the cost of the cloth masks will be $11 \cdot 10 = 110$. Since the price of disposable masks is less, Chef will buy the disposable masks.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
10 100
```

**Output for this case**

```text
Cloth
```



#### Test case 2

**Input for this case**

```text
9 100
```

**Output for this case**

```text
Disposable
```



#### Test case 3

**Input for this case**

```text
88 99
```

**Output for this case**

```text
Cloth
```



#### Test case 4

**Input for this case**

```text
1 11
```

**Output for this case**

```text
Disposable
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CGYM)

[Div-4 Contest](https://www.codechef.com/COOK141D/problems/CMASKS)

***Author:*** [Mradul Bhatnagar](https://www.codechef.com/users/mradul_adm)

***Tester:*** [Harris Leung](https://www.codechef.com/users/gamegame)

#
[](#difficulty-2)DIFFICULTY:

432

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef is shopping for masks. In the shop, he encounters 2 types of masks:

- Disposable Masks — cost X but last only 1 day.

- Cloth Masks — cost Y but last 10 days.

Chef wants to buy masks to last him 100 days. He will buy the masks which cost him the least. In case there is a tie in terms of cost, Chef will be eco-friendly and choose the cloth masks. Which type of mask will Chef choose?

#
[](#explanation-5)EXPLANATION:

For 100 days, Chef will require \frac{100}{1} = 100 disposable masks or \frac{100}{10} = 10 cloth masks.

Therefore if 100 \cdot X \lt 10 \cdot Y, Chef will buy `Disposable` masks, otherwise he will buy `Cloth` masks.

#
[](#solutions-6)SOLUTIONS:

Setter's Solution
``#include <bits/stdc++.h>
using namespace std;
int main()
{
    int test_cases;
    cin>>test_cases;

    for(int tc = 1 ; tc <= test_cases ; tc++)
    {
        int disposable_price , cloth_price;
        cin>>disposable_price>>cloth_price;

        if((100 * disposable_price) < (10 * cloth_price))
            cout<<"Disposable"<<endl;
        else
            cout<<"Cloth"<<endl;
    }

    return 0;
}
``

</details>
