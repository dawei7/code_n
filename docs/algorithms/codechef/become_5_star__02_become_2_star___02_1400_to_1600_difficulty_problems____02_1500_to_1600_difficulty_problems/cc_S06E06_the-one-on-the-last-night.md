# The One On The Last Night

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | S06E06 |
| Difficulty Rating | 1596 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1500 to 1600 difficulty problems |
| Official Link | [S06E06](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1600/problems/S06E06) |

---

## Problem Statement

*Chandler wants to give Joey money as Joey is going through some financial struggles. He believes $1500 will be enough to pay off the bills. Chandler makes up a game on the spot called "Cups", which has no rules. Every move Joey makes in the "game", Chandler says that he wins a lot of money. Joey, being "smart", finds this out and thus wants to set some rules.*

Joey and Chandler have a set of cards, where the **value** of a card is defined as the product of all the digits of the number printed on that card.

For example, value of the card with the number $7$ equals $7$, value of the card with the number $203$ equals $2 \cdot 0 \cdot 3 = 0$.

The initial number on Joey's card is $N$ (without any leading zeroes). Chandler can make at most $K$ changes on the digits of the number before it gets noticed. In one change, he can choose any digit $x$ ($x ≠ 9$) of the number printed on card and replace it with $x+1$.
Find the maximum possible value of Joey's card after making the changes.

---

## Input Format

- First line will contain $T$, number of testcases. Then the testcases follow.
- For each test case, given two integer $N$ and $K$, denoting the initial number on Joey's card and the number of changes Chandler can make.

---

## Output Format

For each testcase, output in a single line the maximum possible value of Joey's card after making the changes.

---

## Constraints

- $1 \leq T \leq 10^3$
- $1 \leq N \leq 10^6$
- $0 \leq K \leq 10^6$

---

## Examples

**Example 1**

**Input**

```text
3
1 5
2221 3
123456 0
```

**Output**

```text
6
36
720
```

**Explanation**

**Test case 1**: Chandler can increase the digit $1$ five times to make the final number on card $6$.

**Test case 2**: Chandler can increase the first digit of the given number once and the last digit twice. After making these changes, the final number on the card would be $3223$, whose value is equal to $36$. There are other ways to make changes on the printed number which may lead to one of the following numbers being the resulting number on card : $2233$, $2323$, $2332$, $3232$, $3322$; note that all these numbers have their values equal to $36$ as well.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 5
```

**Output for this case**

```text
6
```



#### Test case 2

**Input for this case**

```text
2221 3
```

**Output for this case**

```text
36
```



#### Test case 3

**Input for this case**

```text
123456 0
```

**Output for this case**

```text
720
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 2](https://www.codechef.com/FOUR21B/problems/S06E06)

[Contest Division 3](https://www.codechef.com/FOUR21C/problems/S06E06)

**Setter:** [ Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

**Tester:** [ Nishant Shah](https://www.codechef.com/users/nishant403)

**Editorialist:** [ Abhishek Ghosh](https://www.codechef.com/users/ghosh_abhishek)

#
[](#difficulty-2)DIFFICULTY

Easy

#
[](#prerequisites-3)PREREQUISITES

None

#
[](#problem-4)PROBLEM

Given a number N. You need to maximize the product of its digits by incrementing them at most K times.

#
[](#explanation-5)EXPLANATION

***Observation***: Incrementing smaller numbers contribute more to the overall product as compared to incrementing larger numbers.

Proof

A product of 2 numbers can be laid out on a 2-dimensional grid. E.g. 3 * 5 can be represented as

Incrementing the larger number i.e. 5 will include region 1 and increase the product by 3.

Whereas, incrementing the smaller number i.e. 3 will include region 2 and increase the product by 5.

The same idea can be extended to any product of multiple numbers.

So, we increment the digits in the increasing order of their value until either we exhaust all our operations or reach the maximum possible number.

#
[](#implementation-6)IMPLEMENTATION

In each operation we take the current minimum digit (If it is not equal to 9) ?and increase that by 1.

 ? Example:

Consider the sample test case with N=2221 and K=3.

In the first iteration, there is no digit less than 1 in the array.

In the second iteration, 2221 ? 2222 and K=2.

In the third iteration, 2222 ? 3322 and K=0 (No more moves left).

So, the maximum product = 3 * 3 * 2 * 2 = 36.

Time complexity - O(9*K), where K is the number of digits in N

#
[](#solutions-7)SOLUTIONS

Setter's Solution
``#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;
    while(t--){
        string s;
        int k;
        cin >> s >> k;
        for(int i = 1; i <= 9; i++){
            for(int j = 0; j < s.length(); j++){
                if(s[j] < char('0' + i)){
                    if(k == 0){
                        break;
                    }
                    s[j] = '0' + i;
                    k--;
                }
            }
        }
        int ans = 1;
        for(char j : s){
            ans *= (j - '0');
        }
        cout << ans << '\n';
    }

    return 0;
}
``

</details>
