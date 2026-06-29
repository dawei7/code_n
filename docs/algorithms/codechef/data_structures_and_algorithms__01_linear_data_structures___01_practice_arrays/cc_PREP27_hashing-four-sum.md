# Hashing - Four Sum

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP27 |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [PREP27](https://www.codechef.com/practice/course/arrays/ARRAYSPRO/problems/PREP27) |

---

## Problem Statement

You are given an array $A$ with $N$ integers and an integer $X$.

Find all **unique** quadruples $(a, b, c, d)$ in $A$ such that $(a\le b \le c \le d)$ and $a+b+c+d = X$.

Note that:
- Two quadruples are different if at least one element is different in both the quadruples.
- An element $A_i$ can correspond to **at most** one element of the quadruple.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $X$ — the number of elements and the sum.
    - The next line contains $N$ space-separated integers, the elements of the array.

---

## Output Format

For each test case, output $M+1$ lines, where $M$ is the number of unique quadruples:
- The first line contains a single integer $M$.
- The next $M$ lines contain $4$ space-separated integers each, $(a, b, c, d)$ in $A$ such that $(a\le b \le c \le d)$ and $a+b+c+d = X$.

Note that the quadruples must be printed in **lexicographically increasing** order.
Quadruple $(a_i, b_i, c_i, d_i)$ is said to be lexicographically smaller than quadruple $(a_j, b_j, c_j, d_j)$ if one of the following satisfies:
- $a_i \lt a_j$
- $a_i = a_j$ and $b_i \lt b_j$
- $a_i = a_j$ and $b_i = b_j$ and $c_i \lt c_j$
- $a_i = a_j$ and $b_i = b_j$ and $c_i = c_j$ and $d_i \lt d_j$

---

## Constraints

- $1 \leq T \leq 1000$
- $4 \leq N \leq 200$
- $-10^9 \leq X \leq 10^9$
- $-10^5 \leq A_i \leq 10^5$
- The sum of $N$ over all test cases won't exceed $2\cdot 10^4$.

---

## Examples

**Example 1**

**Input**

```text
3
4 4
1 1 1 1
4 5
1 1 1 1
6 6
1 2 3 2 1 0
```

**Output**

```text
1
1 1 1 1 
0
2
0 1 2 3 
1 1 2 2
```

**Explanation**

**Test case $1$:** The only quadruple having sum $4$ is $(1, 1, 1, 1)$.

**Test case $2$:** There is no quadruple with given sum.

**Test case $3$:** There are $2$ quadruples having given sum:
- $(0, 1, 2, 3)$: $0+1+2+3 = 6$
- $(1, 1, 2, 2)$: $1+1+2+2 = 6$

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# DSA Interview Preparation: 4-Sum Problem Editorial

In this lesson, we explore the 4-Sum problem where we need to find all unique quadruples $(a, b, c, d)$ in array $A$ that satisfy:
$$
a + b + c + d = X \quad \text{with} \quad a \le b \le c \le d.
$$
An element in the array can be used only once in a quadruple, and the answer must be printed in lexicographically increasing order.

In this editorial, we cover an efficient approach based on the two-pointer technique.

---

## Approach: Two-Pointer Technique

### Intuition
1. **Sorting:** First, sort the given array. Sorting helps in:
   - Automatically guaranteeing $a \le b \le c \le d$.
   - Simplifying duplicate removal by checking adjacent elements.
2. **Fixing Two Numbers:** Use two nested loops to fix the first two numbers of the quadruple.
3. **Two Pointers for the Remaining Two:** For the remaining part of the array (from index `j+1` to the end), use the two-pointer technique to find two numbers whose sum equals $X - (\text{first two numbers})$.
4. **Duplicate Removal:** Skip duplicate elements in every loop to ensure each quadruple is unique.
5. **Time Complexity:** The two-pointer approach runs in $O(n^3)$ which is efficient given the constraints.

### Detailed Steps
- **Step 1:** Sort the array $A$.
- **Step 2:** For every index $i$ from $0$ to $n-4$, select $A[i]$, skipping duplicates.
- **Step 3:** For every index $j$ from $i+1$ to $n-3$, select $A[j]$, again skipping duplicates.
- **Step 4:** Initialize two pointers — `left` at `j+1` and `right` at `n-1`. Compute:
$$
\text{sum} = A[i] + A[j] + A[\text{left}] + A[\text{right}].
$$
- **Step 5:** If the computed `sum` equals $X$, add the quadruple to the result and move both pointers while skipping duplicates.
- **Step 6:** If `sum` is less than $X$, move the `left` pointer; otherwise, move the `right` pointer.
- **Step 7:** Print the total count and list all quadruples in lexicographical order.

### Code Implementation

Below is the code for this approach in both **C++** and **Python**.

#### C++ for Two-Pointer Technique
```cpp
#include
#include
#include
using namespace std;

void solve() {
    int n, x;
    cin >> n >> x;
    vector a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    sort(a.begin(), a.end());

    vector> result;
    for (int i = 0; i < n - 3; i++) {
        if (i > 0 && a[i] == a[i - 1])
            continue; // Skip duplicate for first number
        for (int j = i + 1; j < n - 2; j++) {
            if (j > i + 1 && a[j] == a[j - 1])
                continue; // Skip duplicate for second number
            int left = j + 1, right = n - 1;
            while (left < right) {
                long long sum = (long long)a[i] + a[j] + a[left] + a[right];
                if (sum == x) {
                    result.push_back({a[i], a[j], a[left], a[right]});
                    // Skip duplicates for third number
                    while (left < right && a[left] == a[left + 1])
                        left++;
                    // Skip duplicates for fourth number
                    while (left < right && a[right] == a[right - 1])
                        right--;
                    left++;
                    right--;
                } else if (sum < x) {
                    left++;
                } else {
                    right--;
                }
            }
        }
    }

    cout << result.size() << "\n";
    for (auto &quad : result) {
        cout << quad[0] << " " << quad[1] << " " << quad[2] << " " << quad[3] << "\n";
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
```

#### Python for Two-Pointer Technique
```python
def solve():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    result = []
    for i in range(n - 3):
        if i > 0 and a[i] == a[i - 1]:
            continue  # Skip duplicate for first number
        for j in range(i + 1, n - 2):
            if j > i + 1 and a[j] == a[j - 1]:
                continue  # Skip duplicate for second number
            left, right = j + 1, n - 1
            while left < right:
                curr_sum = a[i] + a[j] + a[left] + a[right]
                if curr_sum == x:
                    result.append([a[i], a[j], a[left], a[right]])
                    # Skip duplicates for third number
                    while left < right and a[left] == a[left + 1]:
                        left += 1
                    # Skip duplicates for fourth number
                    while left < right and a[right] == a[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif curr_sum < x:
                    left += 1
                else:
                    right -= 1
    print(len(result))
    for quad in result:
        print(" ".join(map(str, quad)))

t = int(input())
for _ in range(t):
    solve()
```

---

## Conclusion

The two-pointer technique is an efficient approach to solve the 4-Sum problem, especially for larger arrays. By sorting the array initially and smartly skipping duplicates, this method ensures that all quadruples are unique and are output in lexicographical order. Mastering this technique will greatly enhance your skills for tackling similar $k$-Sum problems in technical interviews.

Happy Coding!

</details>
