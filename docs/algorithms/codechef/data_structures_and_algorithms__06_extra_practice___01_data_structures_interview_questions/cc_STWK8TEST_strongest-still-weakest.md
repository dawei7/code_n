# Strongest still weakest

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | STWK8TEST |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Basic programming - 2 |
| Official Link | [STWK8TEST](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_02/problems/STWK8TEST) |

---

## Problem Statement

Soldiers are gathered in $N$ groups, and every group has exactly $M$ soldiers with ids
from $1$ to $M$ in each group. Soldier with id $j$ in $i^{th}$ group has strength $A_{ij}$.

A soldier is **strongest** in his group if there exists no soldier who has strength greater than him. Similarly, a soldier is **weakest** among all soldiers with the same id as his if there exists no soldier who has strength less than him.

The general is interested in finding if there is a soldier that is strongest in his group but
weakest among all soldiers with the same id as his. Can you help him?

---

## Input Format

- The first line of the input contains $2$ integers $N$ denoting the number of groups and $M$ denoting the number of soldiers in each group.
- Followed by $N$ lines, where $i^{th}$ line contains $M$ space separated integers $A_{i_0}, A_{i_1}, A_{i_2} ,.., A_{i_M}$ where $A_{ij}$ is the strength of the soldier in $i^{th}$ group with id as $j$.

---

## Output Format

- For each test case, output a single line containing either "Yes" if there is at least one soldier satisfying the above mentioned criteria or "No" if there is no such soldier.
- You may print each character of the string in uppercase or lowercase (for example: the strings "yes", "YeS", "YES" will be treated as the same strings).

---

## Constraints

- $1 \leq N, M \leq 1000$
- $1 \leq A_{ij} \leq 100$

---

## Examples

**Example 1**

**Input**

```text
2 2
1 1
2 1
```

**Output**

```text
Yes
```

**Explanation**

Soldier with id 1 and 2 in group 1, both of them are strongest in their group and weakest among the soldiers with the same id as them.

Soldier with id 2 in group 2 is weakest among the soldiers with same id but not the strongest in his group.

Soldier with id 1 in group 2 is strongest among his group but not the weakest among the soldiers with same id.

**Example 2**

**Input**

```text
3 2
5 1
2 3
3 2
```

**Output**

```text
No
```

**Explanation**

There is no soldier that satisfies the above given criteria.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial

In this lesson, we will tackle a problem involving groups of soldiers. Each group has exactly $M$ soldiers and there are $N$ groups. The soldier in the $i^\text{th}$ group with id $j$ has strength $A_{ij}$. We are required to determine if there is at least one soldier who is both the **strongest in his group** and the **weakest among all soldiers with his soldier id**.

More formally, for a soldier in group $i$ and with id $j$, let:
$$
\text{GroupMax}_i = \max_{0 \leq k < M} A_{ik} \quad \text{and} \quad \text{ColMin}_j = \min_{0 \leq k < N} A_{kj}.
$$
The soldier satisfies the condition if:
$$
A_{ij} = \text{GroupMax}_i \quad \text{and} \quad A_{ij} = \text{ColMin}_j.
$$

There are several approaches to solve this problem. We will discuss two important approaches below.

## Approach 1: Precomputation of Row Maximums and Column Minimums

### Overview
In this approach, we precompute:
- **Row Maximums:** For each group $i$, compute:
  $$
  \text{GroupMax}_i = \max_{0 \leq j < M} A_{ij}.
  $$
- **Column Minimums:** For each soldier id $j$, compute:
  $$
  \text{ColMin}_j = \min_{0 \leq i < N} A_{ij}.
  $$

After the precomputation, we can check every soldier at position $(i, j)$ to verify if:
$$
A_{ij} = \text{GroupMax}_i \quad \text{and} \quad A_{ij} = \text{ColMin}_j.
$$

### Complexity Analysis
- **Time Complexity:**
  - Precomputing the row maximums takes $O(N \times M)$.
  - Precomputing the column minimums takes $O(N \times M)$.
  - The final check also takes $O(N \times M)$.

  Thus, the overall time complexity is $O(N \times M)$.

- **Space Complexity:**
  - We use extra space of $O(N)$ for row maximums and $O(M)$ for column minimums.

### Code Implementation

Below are the implementations in both **C++** and **Python**.

#### C++ Code for Approach 1
```cpp
#include
#include
#include
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;
    vector> A(N, vector(M));
    for (int i = 0; i < N; i++){
        for (int j = 0; j < M; j++){
            cin >> A[i][j];
        }
    }

    vector max_in_group(N);
    vector min_in_id(M, 101); // Since A[i][j] <= 100, initialize with 101.

    // Compute the maximum in each group (row).
    for (int i = 0; i < N; i++){
        max_in_group[i] = *max_element(A[i].begin(), A[i].end());
        // At the same time, update the minimum for each soldier id (column).
        for (int j = 0; j < M; j++){
            min_in_id[j] = min(min_in_id[j], A[i][j]);
        }
    }

    bool found = false;
    // Check for a soldier that is both strongest in the group and weakest in his column.
    for (int i = 0; i < N && !found; i++){
        for (int j = 0; j < M; j++){
            if (A[i][j] == max_in_group[i] && A[i][j] == min_in_id[j]){
                found = true;
                break;
            }
        }
    }

    cout << (found ? "Yes" : "No") << "\n";
    return 0;
}
```

#### Python Code for Approach 1
```python
def solve():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))

    # Build matrix A
    A = []
    for _ in range(N):
        row = [int(next(it)) for _ in range(M)]
        A.append(row)

    # Compute row maximums.
    max_in_group = [max(row) for row in A]

    # Compute column minimums.
    min_in_id = [101] * M  # 101 is used as a high initial value since A[i][j] <= 100.
    for i in range(N):
        for j in range(M):
            min_in_id[j] = min(min_in_id[j], A[i][j])

    found = False
    # Check each soldier.
    for i in range(N):
        for j in range(M):
            if A[i][j] == max_in_group[i] and A[i][j] == min_in_id[j]:
                found = True
                break
        if found:
            break

    sys.stdout.write("Yes\n" if found else "No\n")

if __name__ == '__main__':
    solve()
```

## Approach 2: Naïve Check for Each Soldier

### Overview
In the naïve approach, we directly evaluate each soldier by:
- Iterating over each soldier in the matrix.
- For each soldier at position $(i, j)$, we:
  1. **Check if he is the strongest in his group:**
     Iterate over the entire $i^\text{th}$ row and ensure no other soldier has greater strength.
  2. **Check if he is the weakest among soldiers with the same id:**
     Iterate over the entire $j^\text{th}$ column and ensure no soldier has lower strength.

If both conditions hold for any soldier, we output "Yes".

### Complexity Analysis
- **Time Complexity:**
  For each cell $(i, j)$, we perform two scans:
  - One over the row ($O(M)$).
  - One over the column ($O(N)$).

  In the worst case, this results in a time complexity of $O(N \times M \times (N+M))$. This approach is less efficient than Approach 1 but is easier to understand conceptually.

- **Space Complexity:**
  This method uses $O(1)$ additional space aside from the input matrix.

### Code Implementation

Below are the implementations in **C++** and **Python**.

#### C++ Code for Approach 2
```cpp
#include
#include
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;
    vector> A(N, vector(M));
    for (int i = 0; i < N; i++){
        for (int j = 0; j < M; j++){
            cin >> A[i][j];
        }
    }

    bool found = false;
    // Evaluate each soldier.
    for (int i = 0; i < N && !found; i++){
        for (int j = 0; j < M; j++){
            int curr = A[i][j];

            // Check if current soldier is the strongest in his group.
            bool isStrongest = true;
            for (int k = 0; k < M; k++){
                if (A[i][k] > curr){
                    isStrongest = false;
                    break;
                }
            }
            if (!isStrongest) continue;

            // Check if current soldier is the weakest among all soldiers with the same id.
            bool isWeakest = true;
            for (int k = 0; k < N; k++){
                if (A[k][j] < curr){
                    isWeakest = false;
                    break;
                }
            }
            if (isStrongest && isWeakest) {
                found = true;
                break;
            }
        }
    }

    cout << (found ? "Yes" : "No") << "\n";
    return 0;
}
```

#### Python Code for Approach 2
```python
def solve():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))

    # Build the matrix A.
    A = []
    for _ in range(N):
        A.append([int(next(it)) for _ in range(M)])

    found = False
    # Evaluate each soldier.
    for i in range(N):
        for j in range(M):
            curr = A[i][j]
            # Check if this soldier is the strongest in his group.
            is_strongest = True
            for k in range(M):
                if A[i][k] > curr:
                    is_strongest = False
                    break
            if not is_strongest:
                continue

            # Check if this soldier is the weakest among those with the same id.
            is_weakest = True
            for k in range(N):
                if A[k][j] < curr:
                    is_weakest = False
                    break

            if is_strongest and is_weakest:
                found = True
                break
        if found:
            break

    sys.stdout.write("Yes\n" if found else "No\n")

if __name__ == '__main__':
    solve()
```

## Final Thoughts

Both approaches correctly solve the problem, but **Approach 1** is far more efficient with a time complexity of $O(N \times M)$, which is important given the worst-case constraints of up to $1000 \times 1000$ elements. **Approach 2** is useful for understanding the underlying logic without relying on precomputation, although it may be too slow for larger inputs.

Understanding both methods helps build a solid intuition about how precomputation can drastically reduce the number of operations and improve efficiency in algorithmic problems.

</details>
