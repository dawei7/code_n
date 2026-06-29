# Maximum Common Elements

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP17 |
| Difficulty Rating | 1100 |
| Difficulty Band | Two Pointers and Sliding Window Technique |
| Path | Data Structures and Algorithms |
| Lesson | Two-Pointer |
| Official Link | [PREP17](https://www.codechef.com/practice/course/two-pointers/POINTERF/problems/PREP17) |

---

## Problem Statement

Given two arrays $A$ and $B$, each of size $N$, where each array consists of **distinct** elements.

Find the number of elements that are common in both the arrays.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains an integer $N$ — the size of both the arrays.
    - The second line contains $N$ space separated integers - the elements of array $A$.
    - The third line contains $N$ space separated integers - the elements of array $B$.

---

## Output Format

For each test case, output on a new line, the number of elements that are common in both the arrays.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$, the values $A_i$ are distinct.
- $1 \leq B_i \leq 10^9$, the values $B_i$ are distinct.
- The sum of $N$ over all test cases won't exceed $2\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
4
1 2 3 4
1 3 4 5
3
2 4 1
1 4 2
1
2
3
```

**Output**

```text
3
3
0
```

**Explanation**

**Test case $1$:** There are $3$ common elements in both the arrays, which are, $1, 3,$ and $4$.

**Test case $2$:** There are $3$ common elements in both the arrays, which are, $1, 2,$ and $4$.

**Test case $3$:** There are no common elements between both arrays.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
1 2 3 4
1 3 4 5
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
3
2 4 1
1 4 2
```

**Output for this case**

```text
3
```



#### Test case 3

**Input for this case**

```text
1
2
3
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial

In this lesson, we explore various approaches to solve the problem of finding the number of common elements between two arrays with distinct elements. The goal is to determine the intersection size between the arrays.

We will discuss two approaches:

## Approach 1: Hash Set Based Approach

### Explanation:
We store all elements of the first array in a hash set. Then, we iterate over the second array and check whether each element is present in the hash set. Since the average time complexity for each lookup is $O(1)$, the overall complexity becomes $O(N)$. This approach is efficient and straightforward, making it ideal for large input sizes.

### Code Implementation:

#### C++ Implementation:
```cpp
#include
#include
#include
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;

    while (T--) {
        int N;
        cin >> N;

        unordered_set set_A;
        vector B(N);

        for (int i = 0; i < N; i++) {
            int num;
            cin >> num;
            set_A.insert(num);
        }

        for (int i = 0; i < N; i++) {
            cin >> B[i];
        }

        int common_count = 0;
        for (int num : B) {
            if (set_A.find(num) != set_A.end()) {
                common_count++;
            }
        }

        cout << common_count << "\n";
    }

    return 0;
}
```

#### Python Implementation:
```python
def solve():
    import sys
    input_data = sys.stdin.read().split()
    t = int(input_data[0])
    index = 1
    outputs = []

    for _ in range(t):
        n = int(input_data[index])
        index += 1
        arrA = list(map(int, input_data[index:index+n]))
        index += n
        arrB = list(map(int, input_data[index:index+n]))
        index += n

        set_A = set(arrA)
        common_count = sum(1 for num in arrB if num in set_A)
        outputs.append(str(common_count))

    sys.stdout.write("\n".join(outputs))

if __name__ == "__main__":
    solve()
```

## Approach 2: Sorting and Two-Pointer Technique

### Explanation:
This approach begins by sorting both arrays. With the arrays sorted, we use two pointers to traverse them simultaneously. When the elements pointed to by both pointers are equal, we have found a common element and move both pointers forward. If the current element in the first array is less than that in the second, we move the first pointer; otherwise, we move the second pointer. The sorting step takes $O(N \log N)$ time, and the traversal takes $O(N)$ time, making this method efficient for moderately sized inputs.

### Code Implementation:

#### C++ Implementation:
```cpp
#include
#include
#include
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;

    while (T--) {
        int N;
        cin >> N;
        vector A(N), B(N);

        for (int i = 0; i < N; i++) {
            cin >> A[i];
        }
        for (int i = 0; i < N; i++) {
            cin >> B[i];
        }

        sort(A.begin(), A.end());
        sort(B.begin(), B.end());

        int i = 0, j = 0, common_count = 0;
        while (i < N && j < N) {
            if (A[i] == B[j]) {
                common_count++;
                i++;
                j++;
            } else if (A[i] < B[j]) {
                i++;
            } else {
                j++;
            }
        }

        cout << common_count << "\n";
    }

    return 0;
}
```

#### Python Implementation:
```python
def solve():
    import sys
    input_data = sys.stdin.read().split()
    t = int(input_data[0])
    index = 1
    outputs = []

    for _ in range(t):
        n = int(input_data[index])
        index += 1
        arrA = list(map(int, input_data[index:index+n]))
        index += n
        arrB = list(map(int, input_data[index:index+n]))
        index += n

        arrA.sort()
        arrB.sort()

        i = j = common_count = 0
        while i < n and j < n:
            if arrA[i] == arrB[j]:
                common_count += 1
                i += 1
                j += 1
            elif arrA[i] < arrB[j]:
                i += 1
            else:
                j += 1

        outputs.append(str(common_count))

    sys.stdout.write("\n".join(outputs))

if __name__ == "__main__":
    solve()
```

## Conclusion:
The two approaches demonstrate different methods to solve the problem:

- The **Hash Set Based Approach** is optimal with a linear time complexity, making it the best choice for large arrays.
- The **Sorting and Two-Pointer Technique** offers a viable alternative with an overall complexity of $O(N \log N)$.

Understanding these approaches not only enhances your problem-solving skills but also deepens your comprehension of data structures and algorithm optimizations.

</details>
