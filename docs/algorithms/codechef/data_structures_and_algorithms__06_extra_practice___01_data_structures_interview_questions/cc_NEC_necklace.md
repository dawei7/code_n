# Necklace

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | NEC |
| Difficulty Rating | 800 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Queues |
| Official Link | [NEC](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_09/problems/NEC) |

---

## Problem Statement

Your best friend has a very interesting necklace with $n$ pearls. On each of the pearls of the necklace there is an integer. However, your friend wants to modify the necklace a bit and asks you for help. She wants to move the first pearl $k$ spots to the left (and do so with all other pearls).

For example: if the necklace was originally $1, 5, 3, 4, 2$ and $k = 2$, now it becomes $3, 4, 2, 1, 5$.

Help your best friend determine how the necklace will look after the modification.

---

## Input Format

- First line will contain $T$, the number of test cases. Then the test cases follow.
- Each test case contains two lines of input, the first containing two integers $n, k$.
- The second line of each test case contains $n$ integers $a_1, a_2, ..., a_n$ representing the integers on the pearls starting from the first one.

---

## Output Format

For each testcase, output in a single line $n$ integers representing the necklace after modification.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq n \leq 10^5$
- The sum of $n$ over all test cases does not exceed $3 \cdot 10^5$
- $0 \leq k \leq n$
- $-10^9 \leq a_i \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
2
5 3
1 5 3 4 2
6 5
10 1 2 9 8 2
```

**Output**

```text
4 2 1 5 3
2 10 1 2 9 8
```

**Explanation**

The first test case is the example from the statement.
In the second test case, when we move every element 5 to the left we get the answer.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 3
1 5 3 4 2
```

**Output for this case**

```text
4 2 1 5 3
```



#### Test case 2

**Input for this case**

```text
6 5
10 1 2 9 8 2
```

**Output for this case**

```text
2 10 1 2 9 8
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Necklace Rotation Editorial

In this lesson, we discuss how to perform a left rotation on a necklace (an array of integers) by moving the first $k$ elements to the end. The problem requires us to output the modified necklace after rotating it $k$ positions to the left. We will explore three approaches to solve this problem.

## Approach 1: Modular Indexing (Direct Computation)

**Idea:**
Instead of rearranging the array explicitly, we can calculate the new position of each pearl using the modulo operator. For each index $i$, the element that should appear in the new array comes from index $(i + k) \% n$, where $n$ is the number of pearls. This technique avoids creating an entirely new array and prints the result in a straightforward way.

**Time Complexity:** $O(n)$ per test case.

**C++ Implementation:**
```cpp
#include
#include
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while(t--){
        int n, k;
        cin >> n >> k;
        vector necklace(n);
        for (int i = 0; i < n; i++){
            cin >> necklace[i];
        }
        k %= n;  // Normalize k

        // Use modular indexing to print the rotated necklace
        for (int i = 0; i < n; i++){
            cout << necklace[(i + k) % n] << " ";
        }
        cout << "\n";
    }
    return 0;
}
```

**Python Implementation:**
```python
import sys

def main():
    input_data = sys.stdin.read().split()
    t = int(input_data[0])
    index = 1
    output_lines = []

    for _ in range(t):
        n = int(input_data[index])
        k = int(input_data[index + 1])
        index += 2
        arr = list(map(int, input_data[index:index + n]))
        index += n

        k %= n  # Normalize k
        rotated = [arr[(i + k) % n] for i in range(n)]
        output_lines.append(" ".join(map(str, rotated)))

    sys.stdout.write("\n".join(output_lines))

if __name__ == "__main__":
    main()
```

---

## Approach 2: Slicing/Array Concatenation

**Idea:**
Many high-level languages and libraries support slicing, which lets us divide the array into segments. For a left rotation by $k$, we split the array into two parts: the segment from index $0$ to $k-1$ and the segment from index $k$ to $n-1$. We then concatenate these two segments in reversed order. This method is very intuitive and easy to implement in languages like Python.

**Time Complexity:** $O(n)$ per test case.

**C++ Implementation:**
```cpp
#include
#include
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while(t--){
        int n, k;
        cin >> n >> k;
        vector necklace(n);
        for (int i = 0; i < n; i++){
            cin >> necklace[i];
        }
        k %= n;  // Normalize k

        // Create the rotated list by slicing the vector into two parts
        vector result;
        result.insert(result.end(), necklace.begin() + k, necklace.end());
        result.insert(result.end(), necklace.begin(), necklace.begin() + k);

        for (int x : result) {
            cout << x << " ";
        }
        cout << "\n";
    }
    return 0;
}
```

**Python Implementation:**
```python
def main():
    import sys
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    output = []

    for _ in range(t):
        n = int(data[index])
        k = int(data[index + 1])
        index += 2
        arr = list(map(int, data[index:index + n]))
        index += n

        k %= n  # Normalize k
        # Slice the list into two segments and concatenate them
        rotated = arr[k:] + arr[:k]
        output.append(" ".join(map(str, rotated)))

    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()
```

---

## Approach 3: In-place Reversal Algorithm

**Idea:**
A popular method for array rotation is the reversal algorithm. You perform three reversals:
1. **Reverse the first $k$ elements.**
2. **Reverse the remaining $n-k$ elements.**
3. **Reverse the entire array.**

This sequence of reversals will result in the array being rotated by $k$ positions to the left, and it does so in-place with $O(1)$ extra space.

**Step-by-Step Example:**
Consider the array `[1, 5, 3, 4, 2]` and $k = 3$.
- **Step 1:** Reverse the first $3$ elements:
  `[1, 5, 3]` becomes `[3, 5, 1]`.
  Array becomes `[3, 5, 1, 4, 2]`.
- **Step 2:** Reverse the remaining elements:
  `[4, 2]` becomes `[2, 4]`.
  Array becomes `[3, 5, 1, 2, 4]`.
- **Step 3:** Reverse the entire array:
  `[3, 5, 1, 2, 4]` becomes `[4, 2, 1, 5, 3]`, which is the desired result.

**C++ Implementation:**
```cpp
#include
#include
#include
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while(t--){
        int n, k;
        cin >> n >> k;
        vector necklace(n);
        for (int i = 0; i < n; i++){
            cin >> necklace[i];
        }
        k %= n;  // Normalize k

        // Reverse the first k elements
        reverse(necklace.begin(), necklace.begin() + k);
        // Reverse the remaining n-k elements
        reverse(necklace.begin() + k, necklace.end());
        // Reverse the entire vector
        reverse(necklace.begin(), necklace.end());

        for (int x : necklace) {
            cout << x << " ";
        }
        cout << "\n";
    }
    return 0;
}
```

**Python Implementation:**
```python
def reverse_sublist(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def main():
    import sys
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    output_lines = []

    for _ in range(t):
        n = int(data[index])
        k = int(data[index + 1])
        index += 2
        arr = list(map(int, data[index:index + n]))
        index += n

        k %= n  # Normalize k

        # Reverse the first k elements
        reverse_sublist(arr, 0, k - 1)
        # Reverse the remaining n-k elements
        reverse_sublist(arr, k, n - 1)
        # Reverse the entire array
        reverse_sublist(arr, 0, n - 1)

        output_lines.append(" ".join(map(str, arr)))

    sys.stdout.write("\n".join(output_lines))

if __name__ == "__main__":
    main()
```

---

All three approaches have a linear time complexity $O(n)$ per test case. The first approach (modular indexing) is very simple and ideal for reading and printing the modified array. The second approach (slicing) is highly intuitive in languages like Python and can be mimicked in C++ using vectors. The third approach uses the reversal algorithm to perform an in-place rotation with constant extra space.

These methods are fundamental tools in array manipulation problems and are frequently asked in technical interviews. Understanding these strategies improves your problem-solving skills and boosts your preparation for coding interviews.

Happy Coding!

</details>
