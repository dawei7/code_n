# Next Smaller Element

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | STACK14 |
| Difficulty Band | Stacks and Queues |
| Path | Data Structures and Algorithms |
| Lesson | Stacks |
| Official Link | [STACK14](https://www.codechef.com/learn/course/stacks-and-queues/LSTACKS02/problems/STACK14) |

---

## Problem Statement

Find the next smaller element for each element in an array. For each element, you need to find the next element to the right that is smaller than the current element.

Let's look at an example to understand it better. Consider an array A of integers:

A = [4, 2, 14, 7, 1, 9]

For each element, we want to find the immediate next smallest element. If there is no smaller element, we can use some kind of sentinel value, like -1 or None, to indicate that. Here's how we would solve this for array A:

1. The next smallest element after 4 is 2.
2. The next smallest element after 2 is 1.
3. For 14, the next smallest element is 7.
4. For 7, the next smallest element is 1.
5. For 1, there is no smaller element, so we might say -1 or None.
6. Likewise, for 9, the next smaller element is also -1 or None because there is no element after it, and thus no smaller element.

Thus, after solving the problem for array A, we'd have the result:

[2, 1, 7, 1, -1, -1]

### Task
- Given an integer n, the length of an array
- In the next line you are given n integers, elements of the array.
- Print the next smallest value for each element of the array. If there does not exist a next smaller element, print -1.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $M$ — the number of vertices and edges of the graph, respectively.
    - The next $M$ lines describe the edges. The $i$-th of these $M$ lines contains two space-separated integers $u_i$ and $v_i$, denoting an edge between $u_i$ and $v_i$.

---

## Output Format

For each test case, output on a new line the number of good subgraphs of $G$, modulo $10^9 + 7$.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 100$
- $1 \leq M \leq N\cdot(N-1)/2$
- $1 \leq u_i, v_i \leq N$
- $u_i \neq v_i$ for each $1 \leq i \leq M$.
- The sum of $N$ over all test cases won't exceed $100$.

---

## Examples

**Example 1**

**Input**

```text
5
1 3 5 1 3
```

**Output**

```text
-1 1 1 -1 -1
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### [](#explanation-1)Explanation

This problem can be solved using a stack data structure. The stack will assist in keeping track of elements that have the possibility of becoming the next smallest element for the upcoming position while traversing from right to left in the array.

When traversing the array from right to left to find the next smaller element for each position, we need to adapt the stack usage slightly. This time the stack will keep track of elements for which we are yet to find a smaller element that appears before them (to their left). Since we’re processing elements from right to left, the next smaller element is guaranteed to appear later in the original list order but earlier in our traversal.

Here’s the updated step-by-step algorithm:

- Initialize an empty stack s to maintain indices.

- Traverse the input array from right to left (i.e., start from the last element and

move towards the first).

- For each element at index i, do the following:

- While the stack is not empty and the value at the current top of the stack is greater than or equal to the current element, pop from the stack.

- If the stack is now empty, it implies there is no smaller element to the left; otherwise, the element at the current top of the stack is the next smaller element for arr[i].

- Push the index i of the current element onto the stack.

- Print out the contents for each position immediately or store them in an array and print after the loop based on the requirement.

### [](#c-solution-2)C++ Solution
``#include <iostream>
#include <stack>
#include <vector>
#include <bits/stdc++.h>
using namespace std;

std::vector<int> nextSmallestElement(const std::vector<int>& arr) {
    int n = arr.size();
    std::vector<int> result(n, -1); // Initialize result with -1 for elements with no smaller element
    std::stack<int> s; // Stack to store indices

    for (int i = n - 1; i >= 0; --i) { // Iterate from right to left
        while (!s.empty() && arr[i] <= arr[s.top()]) {
            s.pop();
        }
        if(s.size()!=0) {
            result[i] = arr[s.top()];
        }
        s.push(i);
    }

    return result;
}

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    vector<int> result = nextSmallestElement(arr);
    for (auto e : result) {
        cout << e << " ";
    }
    return 0;
}
``

### [](#python-solution-3)Python Solution
``def next_smallest_element(arr):
    n = len(arr)
    result = [-1] * n  # Initialize result with -1 for elements with no smaller element
    stack = []  # Stack to store indices

    for i in range(n - 1, -1, -1):  # Iterate from right to left
        while stack and arr[i] <= arr[stack[-1]]:
            stack.pop()
        if stack:
            result[i] = arr[stack[-1]]
        stack.append(i)

    return result

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = next_smallest_element(arr)
    for e in result:
        print(e, end=" ")

if __name__ == "__main__":
    main()
``

### [](#java-solution-4)Java Solution
``import java.util.Scanner;
import java.util.Stack;

class NextSmallestElement {

    public static int[] nextSmallestElement(int[] arr) {
        int n = arr.length;
        int[] result = new int[n];
        Stack<Integer> stack = new Stack<>();

        for (int i = n - 1; i >= 0; i--) { // Iterate from right to left
            while (!stack.isEmpty() && arr[i] <= arr[stack.peek()]) {
                stack.pop();
            }
            if (!stack.isEmpty()) {
                result[i] = arr[stack.peek()];
            } else {
                result[i] = -1;
            }
            stack.push(i);
        }

        return result;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt();
        }
        int[] result = nextSmallestElement(arr);
        for (int e : result) {
            System.out.print(e + " ");
        }
    }
}
``

</details>
