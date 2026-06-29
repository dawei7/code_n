# Backtracking - Unique Combinations Sum

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP40 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Backtracking |
| Official Link | [PREP40](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_16/problems/PREP40) |

---

## Problem Statement

You are given an array $A$ consisting of $N$ and a target sum $B$.

Find the list of all *unique combinations* of the elements of $A$, such that the sum of the chosen elements equals $B$.

Note:
- The same element may be chosen from the array $A$ any number of times.
- Two combinations are unique if the frequency of at least one of the chosen elements is different.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input:
    - The first line of each test case contains two integers $N$ and $B$ - the size of the array and target sum, respectively.
    - The second line contains $N$ space-separated integers - the array $A$.

---

## Output Format

For each test case, output $M+1$ lines, where $M$ is the number of unique combinations:
- The first line contains a single integer $M$.
- The next $M$ lines contains a combination of space-separated elements of $A$ which sums to $B$.

Note:
- Elements in a combination $(C_1, C_2, \ldots, C_k)$ must be printed in non-descending order, i.e., $(C_1\le C_2\le \ldots\le C_k)$.
- The combinations must be printed in lexicographically increasing order.
We say that combination $X$ is lexicographically smaller than $Y$ if either $X$ is a prefix of $Y$ or there exists an index $i$ such that for all $j\lt i$, $X_j = Y_j$ and $X_i\lt Y_i$.

---

## Constraints

- $1 \leq T \leq 10$
- $1 \leq N \leq 20$
- $1 \leq A_i \leq 20$
- $1 \leq B \leq 20$

---

## Examples

**Example 1**

**Input**

```text
3
2 2
2 3
3 8
2 3 5
3 7
2 3 6
```

**Output**

```text
1
2
3
2 2 2 2
2 3 3
3 5
1
2 2 3
```

**Explanation**

**Test case $1$:** Given $A$ as $[2, 3]$ and $B$ as $2$.

There is only $1$ valid combination which is $\{[2]\}$.

**Test case $2$:** Given $A$ as $[2, 3, 5]$ and $B$ as $8$.

There are $3$ valid combinations which are $\{[2, 2, 2, 2], [2, 3, 3], [3, 5]\}$. Note that all these combinations are sorted and the set of combinations is printed in lexicographically increasing order.

**Test case $3$:** Given $A$ as $[2, 3, 6]$ and $B$ as $7$.

There is only $1$ valid combination which is $\{[2, 2, 3]\}$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial: Unique Combinations for Target Sum Problem

In this lesson, we will walk through a classic problem where you are given an array $A$ of $N$ integers and a target sum $B$. The task is to find all unique combinations of elements from $A$ that sum exactly to $B$, with the possibility of using the same element multiple times. Each combination must be printed in non-decreasing order, and the set of combinations should be output in lexicographical order.

We will discuss **two different approaches** to solve this problem:

---

## Approach 1: Backtracking (Depth-First Search)

### Overview

Backtracking is a natural choice for exploring all potential combinations that add up to the target sum. The key idea is to:
- **Sort the input array:** This helps in easily ignoring duplicate candidates on the same recursive level and also ensures that the combinations are built in non-decreasing order.
- **Recursively build combinations:** Begin with an empty combination and try including each number (starting from a given index) while reducing the target accordingly.
- **Avoid duplicates:** To prevent generating duplicate combinations, if the same number appears consecutively in the sorted array, skip the subsequent ones on the same recursive level.

### Detailed Explanation

1. **Sorting:** By sorting the array, we ensure that combinations are built in non-decreasing order.
2. **Recursive Function:** We define a recursive function (e.g., `findCombinations`) that:
   - Takes the current combination, the remaining target, and the starting index.
   - If the remaining target is $0$, a valid combination is found.
   - Iterates from the start index to the end of the candidate list. If a candidate exceeds the remaining target, we break out since further candidates will also be too large.
   - Skips over duplicate candidates at the same recursion level by checking if the current candidate is equal to the previous candidate.
3. **Reusing Elements:** Because the same element can be used multiple times, when we add a candidate, we do not increment the start index in the recursive call.

### Code Implementations

Below, you will find the C++ and Python implementations for the Backtracking approach.

#### C++ Code (Backtracking)

```cpp
#include
#include
#include
using namespace std;

void findCombinations(vector& candidates, int target, vector& current, vector>& result, int start) {
    if (target == 0) {
        result.push_back(current);
        return;
    }
    for (int i = start; i < candidates.size(); i++) {
        // If the candidate exceeds the target, no need to proceed further.
        if (candidates[i] > target)
            break;
        // Skip duplicates at the same recursion level.
        if (i > start && candidates[i] == candidates[i-1])
            continue;
        current.push_back(candidates[i]);
        // Reuse the same candidate, hence passing i.
        findCombinations(candidates, target - candidates[i], current, result, i);
        current.pop_back();
    }
}

vector> combinationSum(vector& candidates, int target) {
    sort(candidates.begin(), candidates.end());
    vector> result;
    vector current;
    findCombinations(candidates, target, current, result, 0);
    return result;
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        int N, B;
        cin >> N >> B;
        vector A(N);
        for (int i = 0; i < N; i++) {
            cin >> A[i];
        }
        vector> combinations = combinationSum(A, B);
        cout << combinations.size() << endl;
        for (const auto& combination : combinations) {
            for (int num : combination) {
                cout << num << " ";
            }
            cout << endl;
        }
    }
    return 0;
}
```

#### Python Code (Backtracking)

```python
def find_combinations(candidates, target, start, current, result):
    if target == 0:
        result.append(list(current))
        return
    for i in range(start, len(candidates)):
        # If the candidate exceeds the target, no need to continue further.
        if candidates[i] > target:
            break
        # Skip duplicates at the same recursion level.
        if i > start and candidates[i] == candidates[i - 1]:
            continue
        current.append(candidates[i])
        # Reuse the same candidate (i remains the same).
        find_combinations(candidates, target - candidates[i], i, current, result)
        current.pop()

def combination_sum(candidates, target):
    candidates.sort()
    result = []
    find_combinations(candidates, target, 0, [], result)
    return result

def main():
    T = int(input())
    for _ in range(T):
        N, B = map(int, input().split())
        A = list(map(int, input().split()))
        combinations = combination_sum(A, B)
        print(len(combinations))
        for combo in combinations:
            print(" ".join(map(str, combo)))

if __name__ == "__main__":
    main()
```

---

## Approach 2: Iterative Dynamic Programming

### Overview

The iterative dynamic programming (DP) approach builds combinations for every sub-target from $0$ up to $B$. In this method:
- **DP Table:** We use an array $dp$ where $dp[t]$ stores all combinations that sum to $t$.
- **Initialization:** $dp[0]$ is initialized with an empty combination since there is one way to have a sum of zero.
- **Building Solutions:** For every candidate (from the sorted unique candidates) and for every sum $t$ from the candidate's value to $B$, we can append the candidate to all combinations that form $t - candidate$, ensuring that the current candidate is not less than the last element in the combination to maintain non-decreasing order.

### Detailed Explanation

1. **Unique and Sorted Candidates:** First, sort the candidates and remove duplicates to simplify the DP process.
2. **DP Initialization:** Set $dp[0] = \{\emptyset\}$.
3. **Iterative Update:**
   - For each candidate and each target sum from the candidate value up to $B$, extend all combinations from $dp[t - candidate]$ by appending the candidate if it does not break the non-decreasing order.
4. **Final Result:** After filling the DP table, $dp[B]$ holds all combinations that sum to $B$. Sorting $dp[B]$ lexicographically ensures the output order.

### Code Implementations

Below are the C++ and Python implementations for the Iterative DP approach.

#### C++ Code (Iterative DP)

```cpp
#include
#include
#include
using namespace std;

int main() {
    int T;
    cin >> T;
    while (T--) {
        int N, B;
        cin >> N >> B;
        vector A(N);
        for (int i = 0; i < N; i++) {
            cin >> A[i];
        }
        // Sort and remove duplicates to simplify the process.
        sort(A.begin(), A.end());
        A.erase(unique(A.begin(), A.end()), A.end());

        // DP table: dp[t] will store all combinations that sum up to t.
        vector>> dp(B + 1);
        dp[0].push_back(vector());

        for (int candidate : A) {
            for (int j = candidate; j <= B; j++) {
                for (auto comb : dp[j - candidate]) {
                    // Ensure non-decreasing order.
                    if (comb.empty() || candidate >= comb.back()) {
                        vector newComb = comb;
                        newComb.push_back(candidate);
                        dp[j].push_back(newComb);
                    }
                }
            }
        }

        // Lexicographically sort the combinations.
        sort(dp[B].begin(), dp[B].end());
        cout << dp[B].size() << "\n";
        for (auto comb : dp[B]) {
            for (auto num : comb) {
                cout << num << " ";
            }
            cout << "\n";
        }
    }
    return 0;
}
```

#### Python Code (Iterative DP)

```python
def combination_sum_dp(candidates, target):
    # Remove duplicates and sort the candidates.
    candidates = sorted(set(candidates))
    dp = [[] for _ in range(target + 1)]
    dp[0] = [[]]

    for num in candidates:
        for t in range(num, target + 1):
            for comb in dp[t - num]:
                # Ensure the combination remains non-decreasing.
                if not comb or num >= comb[-1]:
                    dp[t].append(comb + [num])

    dp[target].sort()
    return dp[target]

def main():
    T = int(input())
    for _ in range(T):
        N, B = map(int, input().split())
        A = list(map(int, input().split()))
        result = combination_sum_dp(A, B)
        print(len(result))
        for comb in result:
            print(" ".join(map(str, comb)))

if __name__ == "__main__":
    main()
```

---

## Conclusion

Both approaches guarantee that the combinations are output in non-decreasing order and lexicographical order. The **Backtracking** approach is more intuitive and closely follows a depth-first search method, which is ideal given the constraints. The **Iterative DP** approach is a creative alternative that builds up the solution incrementally using a dynamic programming table.

Choose the approach that best suits your style and problem constraints. For beginners, the backtracking approach often offers a clearer insight into the recursive exploration of choices.

Happy coding and best of luck with your interviews!

</details>
