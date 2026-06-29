# Next Permutation

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | NEXTPERM |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [NEXTPERM](https://www.codechef.com/practice/course/arrays/ARRAYSPRO/problems/NEXTPERM) |

---

## Problem Statement

It is an interesting exercise to write a program to print out all permutations of $1, 2, …, n$. However, since there are $6227020800$ permutations of $1, 2, …, 13$, it is unlikely that we would ever run this program on an input of size more than $10$.

However, here is another interesting problem whose solution can also be used to generate permutations. We can order the permutations of $1, 2, …, n$ under the lexicographic (or dictionary) order. Here are the permutations of $1,2,3$ in lexicographic order:

$$ 1 \, 2 \, 3 \quad    1 \, 3 \, 2 \quad     2 \, 1 \, 3 \quad     2 \, 3 \, 1 \quad     3 \, 1 \, 2 \quad     3 \, 2 \, 1 $$

The problem we have is the following: given a permutation of $1,2, …, n$, generate the next permutation in lexicographic order. For example, for $2 3 1 4$ the answer is $2 3 4 1$.

### Input:

The first line of the input contains two integers, $N$ and $K$. This is followed by $K$ lines, each of which contains one permutation of $1, 2,…,N$.

### Output:

The output should consist of $K$ lines. Line $i$ should contain the lexicographically next permutation correponding to the permutation on line $i+1$ in the input.

It is guaranteed that for every given permutation, a lexicographically next permutation always exists
### Constraints:

- $1 \leq N \leq 1000$.
- $1 \leq K \leq 10$.

---

## Examples

**Example 1**

**Input**

```text
3 2
3 1 2
2 3 1
```

**Output**

```text
3 2 1
3 1 2
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this problem, you are given a permutation of $1,2,\dots,N$ and asked to produce its lexicographical successor. In lexicographic (or dictionary) order, the “next” permutation is the smallest permutation that is strictly greater than the current one. For example, for the permutation “2 3 1 4”, the next permutation is “2 3 4 1”. If the given permutation is the largest (i.e. if the permutation is sorted in descending order), then its next permutation is defined as the smallest permutation (i.e. the one sorted in ascending order).

There are several ways to approach this problem. In this editorial, we discuss two important approaches:

---

### **Approach 1: Using Built-in/Library Functions**

**Overview:**

- **C++:**
  The C++ Standard Library provides a convenient function called `next_permutation` in the `` header. This function rearranges the elements into the next lexicographical permutation and returns `false` if the permutation was the largest one.

- **Python:**
  Python does not include a built-in `next_permutation` function. However, we can implement the same logic in a concise helper function. This function works as follows:
  1. Traverse from the end to find the first index $i$ such that $a[i] < a[i+1]$. This index is known as the pivot.
  2. If no such index is found, the permutation is the largest and we return the smallest permutation (sorted order).
  3. Otherwise, find the smallest element in the suffix that is greater than $a[i]$, swap them, and then reverse the suffix.

**Time Complexity:**
This approach works in $O(N)$ per test case, which is efficient even for $N$ as high as $1000$.

---

### **Approach 2: Manual Implementation – The Next Permutation Algorithm**

**Overview:**

This approach manually implements the algorithm to generate the next permutation. The steps are similar to those in Approach 1 but are written “from scratch” in both C++ and Python.

The steps are:
1. **Find the Pivot:**
   Traverse the permutation from right to left to find the largest index $k$ for which $a[k] < a[k+1]$. If no such index exists, the current permutation is the last permutation.

2. **Find the Swap Candidate:**
   Find the largest index $l$ greater than $k$ where $a[l] > a[k]$.

3. **Swap and Reverse:**
   Swap $a[k]$ with $a[l]$ and then reverse the subarray $a[k+1:]$ to obtain the next smallest lexicographical permutation.

4. **Edge Case:**
   If the permutation is the largest, then reversing it (or simply sorting it) produces the smallest permutation.

**Time Complexity:**
Just as with Approach 1, this algorithm runs in $O(N)$ per test case.

**Note on Other Methods:**
One could think about generating all permutations (for instance, using recursion or Python’s `itertools.permutations`) and then sorting them. However, since the number of permutations grows factorially, this method is unsuitable for larger values of $N$.

---

Below are the complete code implementations in both C++ and Python for each of the two approaches.

---

### **Approach 1: Using Built-in/Library Functions**

#### **C++ Code:**

```cpp
#include
#include
#include
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, K;
    cin >> N >> K;
    for (int i = 0; i < K; i++) {
        vector p(N);
        for (int j = 0; j < N; j++) {
            cin >> p[j];
        }
        // Use library function to get next permutation.
        if(!next_permutation(p.begin(), p.end()))
            sort(p.begin(), p.end());
        for (int j = 0; j < N; j++) {
            cout << p[j] << " ";
        }
        cout << "\n";
    }
    return 0;
}
```

#### **Python Code:**

```python
import sys

def next_permutation(arr):
    # Find the pivot: rightmost index where arr[i] < arr[i+1]
    i = len(arr) - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    if i == -1:
        arr.sort()
        return arr
    # Find the rightmost element greater than pivot
    j = len(arr) - 1
    while arr[j] <= arr[i]:
        j -= 1
    arr[i], arr[j] = arr[j], arr[i]
    arr[i+1:] = reversed(arr[i+1:])
    return arr

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    N, K = map(int, data[:2])
    index = 2
    for _ in range(K):
        permutation = list(map(int, data[index:index+N]))
        index += N
        next_permutation(permutation)
        print(" ".join(map(str, permutation)))

if __name__ == "__main__":
    main()
```

---

### **Approach 2: Manual Implementation of the Next Permutation Algorithm**

#### **C++ Code:**

```cpp
#include
#include
#include
using namespace std;

bool nextPermutation(vector &p) {
    int n = p.size();
    int k = n - 2;
    // Find the largest index k such that p[k] < p[k+1]
    while (k >= 0 && p[k] >= p[k + 1])
        k--;
    // If no pivot, the current permutation is the largest
    if (k < 0) {
        sort(p.begin(), p.end());
        return false;
    }
    int l = n - 1;
    // Find the largest index l > k such that p[l] > p[k]
    while(p[l] <= p[k])
        l--;
    swap(p[k], p[l]);
    // Reverse the sequence from k+1 to end
    reverse(p.begin() + k + 1, p.end());
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, K;
    cin >> N >> K;
    for (int i = 0; i < K; i++) {
        vector p(N);
        for (int j = 0; j < N; j++) {
            cin >> p[j];
        }
        nextPermutation(p);
        for (int j = 0; j < N; j++) {
            cout << p[j] << " ";
        }
        cout << "\n";
    }
    return 0;
}
```

#### **Python Code:**

```python
import sys

def next_permutation_manual(arr):
    n = len(arr)
    # Find the rightmost index i such that arr[i] < arr[i+1]
    i = n - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    # If the entire array is non-increasing, it is the last permutation.
    if i < 0:
        arr.sort()
        return arr
    # Find the element just larger than arr[i] in the suffix
    j = n - 1
    while arr[j] <= arr[i]:
        j -= 1
    arr[i], arr[j] = arr[j], arr[i]
    # Reverse the suffix starting at i+1
    arr[i+1:] = reversed(arr[i+1:])
    return arr

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    N, K = map(int, data[:2])
    index = 2
    for _ in range(K):
        permutation = list(map(int, data[index:index+N]))
        index += N
        next_permutation_manual(permutation)
        print(" ".join(map(str, permutation)))

if __name__ == "__main__":
    main()
```

</details>
