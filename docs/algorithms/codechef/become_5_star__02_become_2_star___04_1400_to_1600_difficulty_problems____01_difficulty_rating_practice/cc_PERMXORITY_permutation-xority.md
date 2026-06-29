# Permutation Xority

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PERMXORITY |
| Difficulty Rating | 1437 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [PERMXORITY](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/PERMXORITY) |

---

## Problem Statement

You are given an integer $N$. Construct a permutation $A$ of length $N$ which is **attractive**.

A permutation is called **attractive** if the [bitwise XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) of all absolute differences of adjacent pairs of elements is equal to $0$.

Formally, a permutation $A = [A_1, A_2, \ldots, A_N]$ of length $N$ is said to be attractive if:

$$|A_{1}-A_{2}|  \oplus |A_{2}-A_{3}| \oplus \ldots \oplus |A_{N-1} - A_{N}| = 0$$

where $\oplus$ denotes the bitwise XOR operation.

Output **any** attractive permutation of length $N$. If no attractive permutation exists, print $-1$ instead.

**Note:** A permutation of length $N$ is an array $A = [A_1, A_2, \ldots, A_N]$ such that every integer from $1$ to $N$ occurs exactly once in $A$. For example, $[1, 2, 3]$ and $[2, 3, 1]$ are permutations of length $3$, but $[1, 2, 1]$, $[4, 1, 2]$, and $[2, 3, 1, 4]$ are not.

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- Each test case consists of a single line of input, containing one integer $N$.

---

## Output Format

For each test case, output on a single line an attractive permutation of $N$ integers, or $-1$ if no attractive permutation exists.

---

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^5$
- Sum of $N$ over all cases won't exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
2
3
6
```

**Output**

```text
3 2 1
5 2 3 6 4 1
```

**Explanation**

**Test Case $1$:** $ |3-2| \oplus |2-1|  =  1 \oplus 1 = 0$

Note that there are other correct answers — for example, $[1, 2, 3]$ would also be accepted as correct.

**Test Case $2$:** $ |5-2| \oplus |2-3| \oplus |3-6| \oplus |6-4| \oplus |4-1| = 3 \oplus 1 \oplus 3 \oplus 2 \oplus 3 = 0$

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
```

**Output for this case**

```text
3 2 1
```



#### Test case 2

**Input for this case**

```text
6
```

**Output for this case**

```text
5 2 3 6 4 1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START28A/problems/PERMXORITY)

[Contest Division 2](https://www.codechef.com/START28B/problems/PERMXORITY)

[Contest Division 3](https://www.codechef.com/START28C/problems/PERMXORITY)

[Contest Division 4](https://www.codechef.com/START28D/problems/PERMXORITY)

Setter: [S.Manuj Nanthan](https://www.codechef.com/users/munch_01)

Tester: [Abhinav Sharma](https://www.codechef.com/users/inov_360), [Manan Grover](https://www.codechef.com/users/mexomerf)

Editorialist: [Lavish Gupta](https://www.codechef.com/users/lavish315)

#
[](#difficulty-2)DIFFICULTY:

Simple

#
[](#prerequisites-3)PREREQUISITES:

[Bitwise XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR)

#
[](#problem-4)PROBLEM:

You are given an integer N. Construct a permutation A of length N which is **attractive**.

A permutation is called **attractive** if the [bitwise XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) of all absolute differences of adjacent pairs of elements is equal to 0.

Formally, a permutation A = [A_1, A_2, \ldots, A_N] of length N is said to be attractive if:

|A_{1}-A_{2}|  \oplus |A_{2}-A_{3}| \oplus \ldots \oplus |A_{N-1} - A_{N}| = 0

where \oplus denotes the bitwise XOR operation.

Output **any** attractive permutation of length N. If no attractive permutation exists, print -1 instead.

**Note:** A permutation of length N is an array A = [A_1, A_2, \ldots, A_N] such that every integer from 1 to N occurs exactly once in A. For example, [1, 2, 3] and [2, 3, 1] are permutations of length 3, but [1, 2, 1], [4, 1, 2], and [2, 3, 1, 4] are not.

#
[](#quick-explanation-5)QUICK EXPLANATION:

If N is odd

In this case, there are total even number of absolute difference terms. If these terms are all equal, their overall XOR will become 0.

Hence, we can have all absolute difference terms to be equal to 1. In simpler words, the permutation \{1, 2, \ldots N\} is a valid permutation.

If N is even

In this case, there are total odd number of absolute difference terms.

We cannot make XOR of 1 term to be 0 (as each term is greater than 0). Let us try to make XOR of first 3 terms to be 0, and follow the above strategy for rest of the terms.

One of the valid permutation is: \{2, 3, 1, 4, 5, 6 \ldots N\}.

Corner Case

N = 2 is a corner case. Since we have only one absolute difference term, and it is non-zero, we cannot have the overall XOR as 0. The answer would be -1 in this case.

#
[](#explanation-6)EXPLANATION:

There can be many possible constructions. This editorial explains one of the strategies to make a valid permutation.

Let us divide our solution in two parts depending on the parity of N. We will first see a valid construction when N is odd, and then we will use this solution to construct a valid permutation for even values of N. Finally, we will take a look at a corner case.

**When N is odd**

In this case, we will have even number of absolute difference terms. Now, whenever we deal with overall XOR to be equal to 0, one of the properties of XOR that we should keep in mind is: a \oplus a = 0. Let us extend this property for our case. If we take even number of a's and take their XOR, the result will be equal to 0.

So, if all the absolute terms are equal, we will have a valid permutation. One of the permutation that satisfies this property is \{1, 2, \ldots , N \}

**When N is even**

In this case, we will have odd number of absolute difference terms. Also, we already have a solution when we have even number of absolute difference terms. Let us think in the direction of breaking these odd number of terms in two parts - one having odd number of terms such that its XOR is 0, and other having even number of terms. Because we can’t have XOR of 1 term as 0 (because each term is greater than 0) , let us focus on 3 terms.

Let the permutation be \{P_1, P_2, \ldots P_N \}. The above parts corresponds to terms from the following two sequences - \{P_1, P_2, P_3, P_4\} and \{P_4, P_5, \ldots P_N\}.

We have already seen that if \{P_4, P_5, \ldots P_N\} = \{4, 5, \ldots , N\}, then we have the XOR of absolute difference terms as 0. Also, this fixes the value of P_4 as 4, and leaves 1, 2 and 3 for P_1, P_2 and P_3.

A little trial and error on paper shows that permutations like \{1, 3, 2, 4\} or \{2, 3, 1, 4\} have their XOR of absolute difference terms as 0.

Hence, one of the valid permutations is \{2, 3, 1, 4, 5, 6 \ldots N\}.

**An Important corner case**

Note that if N = 2, we have only one absolute difference term, and it is non-zero. So we cannot have the overall XOR as 0. The answer would be -1 in this case.

#
[](#time-complexity-7)TIME COMPLEXITY:

O(N) for each test case.

#
[](#solution-8)SOLUTION:

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
        int n ;
        cin >> n ;

        if(n == 2)
        {
            cout << -1 << endl ;
            continue ;
        }

        if(n%2 == 1)
        {
            for(int i = 1 ; i <= n ; i++)
                cout << i << ' ';
            cout << endl ;
        }
        else
        {
            cout << 2 << ' ' << 3 << ' ' << 1 << ' ';
            for(int i = 4 ; i <= n ; i++)
                cout << i << ' ';
            cout << endl ;
        }
    }

    return 0;
}
``

</details>
