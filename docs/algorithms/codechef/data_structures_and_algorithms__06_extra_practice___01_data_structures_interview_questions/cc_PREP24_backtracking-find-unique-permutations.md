# Backtracking - Find Unique Permutations

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP24 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Backtracking |
| Official Link | [PREP24](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_16/problems/PREP24) |

---

## Problem Statement

You are given an array $A_1, A_2, \dots, A_N$ of length $N$ that may contain duplicates. Find all possible unique permutations of $A$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first line of each test case contains an integer $N$ - the length of the array $A$.
- The second line of each test case contains $N$ space-separated integers $A_1,A_2,\ldots,A_N$.

---

## Output Format

For each test case, output $M+1$ lines, where $M$ is the number of unique permutations:
- The first line contains a single integer $M$.
- The next $M$ lines contain $N$ space-separated integers each which will be permutation of $A$.

Note: The permutations must be printed in **lexicographically increasing** order.
Permutatios $a_1,a_2,\ldots,a_N$ is said to be lexicographically smaller than permutation $b_1,b_2,\ldots,b_N$ if there exists a position $i$ where $a_i \lt b_i$ and $a_j = b_j$ for all $j \lt i$.

---

## Constraints

- $1 \leq T \leq 10$
- $1 \leq N, A_i \leq 10$

---

## Examples

**Example 1**

**Input**

```text
3
3
4 5 5
3
5 25 10
2
6 8
```

**Output**

```text
3
4 5 5 
5 4 5 
5 5 4 
6
5 10 25 
5 25 10 
10 5 25 
10 25 5 
25 5 10 
25 10 5 
2
6 8 
8 6
```

**Explanation**

**Test case $1$:** There are $3$ possible permutations which are $\{[4, 5, 5], [5, 4, 5], [5, 5, 4]\}$.

**Test case $2$:** There are $6$ possible permutations which are $\{[5, 10, 25], [5, 25, 10], [10, 5, 25], [10, 25, 5], [25, 5, 10], [25, 10, 5]\}$.

**Test case $3$:** There are $2$ possible permutations which are $\{[6, 8], [8, 6]\}$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial: Unique Permutations in Lexicographical Order

In this problem, we are given an array $A$ of $N$ integers, which might include duplicates. Our objective is to generate all unique permutations of the array in lexicographically increasing order. In today’s lesson, we will discuss **three different approaches** to solve the problem and provide implementations in both C++ and Python.

---

## Approach 1: Using the Next Permutation Algorithm

### Concept

The next permutation algorithm rearranges numbers into the next lexicographical order. In C++, we have the built-in function `std::next_permutation` in the `` header that simplifies this task. In Python, although there isn’t a built-in function, we can implement the same logic manually.

**Steps:**

1. **Sort the array:** Starting with the sorted array ensures that the first permutation is the lexicographically smallest.
2. **Generate permutations:** Repeatedly generate the next permutation until no more permutations exist.
3. **Store the permutations:** Collect all the unique permutations.

This method naturally generates the permutations in lexicographical order.

### C++ Implementation

```cpp
#include
#include
#include
using namespace std;

int main() {
    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;
        vector arr(N);
        for (int i = 0; i < N; i++) {
            cin >> arr[i];
        }
        sort(arr.begin(), arr.end());
        vector> permutations;
        do {
            permutations.push_back(arr);
        } while (next_permutation(arr.begin(), arr.end()));

        cout << permutations.size() << endl;
        for (auto &perm : permutations) {
            for (int num : perm) {
                cout << num << " ";
            }
            cout << endl;
        }
    }
    return 0;
}
```

### Python Implementation

```python
def next_permutation(arr):
    # Find non-increasing suffix
    i = len(arr) - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    if i == -1:
        return False
    # Find successor to pivot
    j = len(arr) - 1
    while arr[j] <= arr[i]:
        j -= 1
    arr[i], arr[j] = arr[j], arr[i]
    # Reverse suffix
    arr[i+1:] = reversed(arr[i+1:])
    return True

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    permutations = []
    current = arr.copy()
    while True:
        permutations.append(current.copy())
        if not next_permutation(current):
            break
    print(len(permutations))
    for perm in permutations:
        print(' '.join(map(str, perm)))
```

---

## Approach 2: Backtracking with a Frequency Map

### Concept

In this method, we use a frequency map (or dictionary) to count the occurrences of each number. By picking each number in sorted order and reducing its count when it is used, we prevent duplicate permutations from being generated.

**Steps:**

1. **Count Frequencies:** Create a frequency map of the numbers.
2. **Backtrack:** Recursively build the permutation by choosing a number (if its count is greater than zero), then backtrack after the recursive call by restoring its count.
3. **Output:** Once the current permutation reaches length $N$, add it to the result.

Since we process keys (numbers) in sorted order, the final list of permutations is lexicographically sorted.

### C++ Implementation

```cpp
#include
#include
#include
using namespace std;

void backtrack(vector& curr, int N, map& freq, vector>& result) {
    if (curr.size() == N) {
        result.push_back(curr);
        return;
    }
    for (auto &entry : freq) {
        if (entry.second > 0) {
            curr.push_back(entry.first);
            entry.second--;
            backtrack(curr, N, freq, result);
            entry.second++;
            curr.pop_back();
        }
    }
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;
        vector arr(N);
        map freq;
        for (int i = 0; i < N; i++) {
            cin >> arr[i];
            freq[arr[i]]++;
        }
        vector> result;
        vector curr;
        backtrack(curr, N, freq, result);
        cout << result.size() << endl;
        for (auto &perm : result) {
            for (int num : perm) {
                cout << num << " ";
            }
            cout << endl;
        }
    }
    return 0;
}
```

### Python Implementation

```python
def backtrack(curr, N, freq, result):
    if len(curr) == N:
        result.append(curr.copy())
        return
    for num in sorted(freq.keys()):
        if freq[num] > 0:
            curr.append(num)
            freq[num] -= 1
            backtrack(curr, N, freq, result)
            freq[num] += 1
            curr.pop()

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    result = []
    backtrack([], N, freq, result)
    print(len(result))
    for perm in result:
        print(' '.join(map(str, perm)))
```

---

## Approach 3: Backtracking with Swapping and a Set for Duplicate Elimination

### Concept

In this approach, we generate all permutations by swapping elements. To handle duplicate entries, we use a set to store only unique permutations. By starting with a sorted array and taking care not to swap identical elements at the same recursion level, we ensure that permutations are generated uniquely. Finally, we sort the set of permutations to output them in lexicographical order.

**Steps:**

1. **Sort the array:** This ensures that duplicates are adjacent.
2. **Recursion with swapping:** Recursively swap elements and backtrack.
3. **Utilize a set:** Insert each complete permutation into a set to ensure uniqueness.
4. **Sort and Output:** Convert the set to a list and sort it before printing.

### C++ Implementation

```cpp
#include
#include
#include
#include
using namespace std;

void generatePermutations(vector& arr, int index, set>& result) {
    if (index == arr.size()) {
        result.insert(arr);
        return;
    }
    for (int i = index; i < arr.size(); i++) {
        if (i != index && arr[i] == arr[index])
            continue;
        swap(arr[i], arr[index]);
        generatePermutations(arr, index + 1, result);
        swap(arr[i], arr[index]);
    }
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;
        vector arr(N);
        for (int i = 0; i < N; i++) {
            cin >> arr[i];
        }
        sort(arr.begin(), arr.end());
        set> result;
        generatePermutations(arr, 0, result);
        cout << result.size() << endl;
        for (const auto &perm : result) {
            for (int num : perm) {
                cout << num << " ";
            }
            cout << endl;
        }
    }
    return 0;
}
```

### Python Implementation

```python
def generate_permutations(arr, index, result):
    if index == len(arr):
        result.add(tuple(arr))
        return
    for i in range(index, len(arr)):
        if i != index and arr[i] == arr[index]:
            continue
        arr[i], arr[index] = arr[index], arr[i]
        generate_permutations(arr, index + 1, result)
        arr[i], arr[index] = arr[index], arr[i]

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    result = set()
    generate_permutations(arr, 0, result)
    res_list = sorted(list(result))
    print(len(res_list))
    for perm in res_list:
        print(' '.join(map(str, perm)))
```

---

Each approach has its advantages:

- **Approach 1** is concise and leverages built-in functions in C++.
- **Approach 2** avoids generating duplicate permutations by managing counts.
- **Approach 3** uses a straightforward swapping method with a set to ensure uniqueness.

Based on your understanding and comfort with recursion or library functions, you can choose the approach that best fits your style. All three methods are efficient for the given constraints.

</details>
