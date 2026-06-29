# Kth Number

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | GUESNUMK |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Basic programming - 2 |
| Official Link | [GUESNUMK](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_02/problems/GUESNUMK) |

---

## Problem Statement

Consider the first $N$ natural numbers. Alice decides to arrange them in a list in the following order -
- Alice starts with an empty list of numbers.
- All the numbers $X$ such that $X mod 3 = 1$ are added to the list in increasing order.
- All the numbers $X$ such that $X mod 3 = 2$ are added to the list in increasing order.
- Finally, all the numbers $X$ such that $X mod 3 = 0$ are added to the list in increasing order.

Given integer $N$ and $K$, Alice challenges you to find the $K^{th}$ number in the list.

---

## Input Format

- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of a single line of input, two integers $N, K$.

---

## Output Format

For each testcase, output a single integer equal to the $K^{th}$ number in the list.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq K \leq N \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
1
10 7
```

**Output**

```text
8
```

**Explanation**

**Test case-1**:
Alice adds the numbers to list in the following order
1 4 7 10 2 5 8 3 6 9
The $7^{th}$ number in the list is : $8$

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this problem, we are given a number $N$ and an index $K$, and we have to generate an arrangement of the first $N$ natural numbers. The arrangement is defined by placing:
- All numbers $X$ with $X \bmod 3 = 1$ in increasing order,
- Followed by all numbers $X$ with $X \bmod 3 = 2$ in increasing order,
- And finally all numbers $X$ with $X \bmod 3 = 0$ in increasing order.

The challenge is to compute the $K^{\text{th}}$ number in this constructed list without unnecessarily generating the entire list (since $N$ can be as large as $10^9$).

Below we discuss **two different approaches** to solve the problem:

---

### Approach 1: Direct Optimal Computation Using Group Counts

**Idea:**
Observe that the arranged list consists of three groups:
- **Group 1:** Numbers with $X \bmod 3 = 1$. These form an arithmetic progression (AP):
  $$1,\, 4,\, 7,\, \dots$$
  which can be written as $$3i - 2$$ for $i \ge 1.$
- **Group 2:** Numbers with $X \bmod 3 = 2$. This AP is:
  $$2,\, 5,\, 8,\, \dots$$
  which is $$3i - 1$$ for $i \ge 1.$
- **Group 3:** Numbers with $X \bmod 3 = 0$. This AP is:
  $$3,\, 6,\, 9,\, \dots$$
  which is $$3i$$ for $i \ge 1.$

**Counting the Groups:**
We can compute the number of elements in each group using:
$$
\text{group1} = \left\lfloor \frac{N+2}{3} \right\rfloor,\quad
\text{group2} = \left\lfloor \frac{N+1}{3} \right\rfloor,\quad
\text{group3} = \left\lfloor \frac{N}{3} \right\rfloor.
$$

**Determining the $K^{\text{th}}$ Element:**
- If $K \leq \text{group1}$, the answer is the $K^{\text{th}}$ element of Group 1:
  $$3K - 2.$$
- If $K$ is greater than $\text{group1}$ but $\leq \text{group1}+\text{group2}$, it belongs to Group 2. Let $i = K - \text{group1}$, then the answer is:
  $$3i - 1.$$
- Otherwise, if $K > \text{group1}+\text{group2}$, let $j = K - \text{group1} - \text{group2}$ and the answer is in Group 3:
  $$3j.$$

This approach runs in $O(1)$ per test case and is optimal for the given constraints.

---

### Approach 2: Using Arithmetic Progressions and Modulo Properties

**Idea:**
Recognize that each group forms an arithmetic progression:
- For Group 1, the $i^{\text{th}}$ term is $$a_i = 3i - 2.$$
- For Group 2, the $i^{\text{th}}$ term is $$a_i = 3i - 1.$$
- For Group 3, the $i^{\text{th}}$ term is $$a_i = 3i.$$

By determining the sizes of Group 1 and Group 2 (as computed above) and checking where $K$ falls, we can use the respective formula:
- If $K \leq \text{group1}$, then the answer is $$3K - 2.$$
- If $\text{group1} < K \leq \text{group1}+\text{group2}$, then letting $i = K - \text{group1}$ gives the answer $$3i - 1.$$
- Otherwise, letting $j = K - \text{group1} - \text{group2}$ yields the answer $$3j.$$

This approach essentially reinforces the observations made in Approach 1 and is equally optimal.

---

### Code Implementations

Below are the code implementations for each approach in both C++ and Python.

---

#### Approach 1: Direct Optimal Computation

**C++ Implementation:**
```cpp
#include
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;
    while(T--){
        long long N, K;
        cin >> N >> K;
        // Calculate group sizes using integer division.
        long long group1 = (N + 2) / 3;
        long long group2 = (N + 1) / 3;

        if(K <= group1) {
            cout << 3 * K - 2 << "\n";
        } else if(K <= group1 + group2) {
            cout << 3 * (K - group1) - 1 << "\n";
        } else {
            cout << 3 * (K - group1 - group2) << "\n";
        }
    }
    return 0;
}
```

**Python Implementation:**
```python
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    group1 = (N + 2) // 3
    group2 = (N + 1) // 3

    if K <= group1:
        print(3 * K - 2)
    elif K <= group1 + group2:
        print(3 * (K - group1) - 1)
    else:
        print(3 * (K - group1 - group2))
```

---

#### Approach 2: Using Arithmetic Progressions and Modulo Properties

**C++ Implementation:**
```cpp
#include
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while(T--){
        long long N, K;
        cin >> N >> K;
        // Determine counts for Group 1 (numbers with X mod 3 = 1) and Group 2 (X mod 3 = 2)
        long long count1 = (N + 2) / 3;
        long long count2 = (N + 1) / 3;

        if(K <= count1){
            // Kth element in the first arithmetic progression
            cout << 3 * K - 2 << "\n";
        } else if(K <= count1 + count2){
            // Kth element is in the second arithmetic progression
            cout << 3 * (K - count1) - 1 << "\n";
        } else{
            // Kth element is in the third arithmetic progression
            cout << 3 * (K - count1 - count2) << "\n";
        }
    }
    return 0;
}
```

**Python Implementation:**
```python
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    # Calculate counts for the sequences.
    count1 = (N + 2) // 3  # Sequence: 3K - 2
    count2 = (N + 1) // 3  # Sequence: 3K - 1

    if K <= count1:
        print(3 * K - 2)
    elif K <= count1 + count2:
        print(3 * (K - count1) - 1)
    else:
        print(3 * (K - count1 - count2))
```

---

### Conclusion

Both **Approach 1** and **Approach 2** provide an efficient $O(1)$ solution per test case by leveraging arithmetic progressions and modulo properties to compute the $K^{\text{th}}$ element without constructing the full list. These approaches avoid unnecessary computations and are optimal for large constraints on $N$.

Understanding these approaches not only helps solve this specific problem but also reinforces concepts such as arithmetic progressions, modulo arithmetic, and efficient computation.

</details>
