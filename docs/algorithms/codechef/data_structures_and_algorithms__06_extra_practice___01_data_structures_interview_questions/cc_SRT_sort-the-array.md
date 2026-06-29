# Sort the array

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SRT |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Sorting |
| Official Link | [SRT](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_04/problems/SRT) |

---

## Problem Statement

Chef gave you an array $A$ of length $N$ which contains pairwise **distinct** elements. You can perform the following operations on the array:
- Select two distinct indices $i,j$ and swap $A_i,A_j$

He then asked you to find the **minimum** number of operations to sort the array.

---

## Input Format

- First-line will contain $T$, the number of test cases. Then the test cases follow.
- Each test case contains two lines of input.
- The first line of every test case contains an integer $N$ - the length of array.
- The second line of every test case contains $N$ integers - $ A_1,A_2,..,A_N$ denoting the integers in the array.

---

## Output Format

For each test case, output in a single line- the answer to the $i$-th test case.

---

## Constraints

- $1 \leq T \leq 1500$
- $1 \leq N \leq 2 \cdot 10^5$
- $1 \leq A_i \leq 10^9$
- $\sum N \leq 5\cdot10^5$

---

## Examples

**Example 1**

**Input**

```text
4
2
2 1
4
2 4 3 1
5
7 1 3 10 2
2
1 2
```

**Output**

```text
1
2
3
0
```

**Explanation**

**Test Case 1:** We can sort the array by swapping $A_1 and A_2$ in $1$ swap.

**Test Case 2:** We can first swap $A_1,A_4$ and then swap $A_2,A_4$ to obtain a sorted array.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
2 1
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
4
2 4 3 1
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
5
7 1 3 10 2
```

**Output for this case**

```text
3
```



#### Test case 4

**Input for this case**

```text
2
1 2
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial: Minimum Number of Swaps to Sort an Array

In this lesson, we will learn how to determine the minimum number of swap operations required to sort an array of $N$ distinct integers. You are allowed to swap any two elements in the array. Our goal is to sort the array in as few swaps as possible.

The key observation for this problem is that since the elements are pairwise distinct, the current ordering can be mapped to a permutation of the sorted order. This permutation can be decomposed into one or more **cycles**. For any cycle of size $k$, it takes exactly $k - 1$ swaps to put every element in its correct position. Thus, the total minimum number of swaps required to sort the array is the sum of $(\text{cycle size} - 1)$ over all cycles.

Below, we discuss two important approaches to solving this problem.

---

## Approach 1: Cycle Decomposition Method

### Intuition:

1. **Pair and Sort:**
   First, we create a list of pairs where each pair consists of an element and its original index. We then sort this list according to the array values. The sorted list tells us where each element should be in the sorted array.

2. **Cycle Identification:**
   Once we have the sorted positions, we can iterate over the array and identify cycles. For an element that is not yet in the correct position, we can follow the chain of placements until we return to the starting index.
   If the cycle has a length $k$, then it requires $k - 1$ swaps to arrange the elements correctly.

### Mathematical Explanation:

Suppose a cycle has elements at positions $i_1, i_2, i_3, \dots, i_k$. The correct swap operations required to arrange them are:

$$
\text{swaps} = k - 1
$$

Thus, summing over all cycles gives the minimum swaps.

### Code Implementations:

#### C++ Code for Approach 1:
```cpp
#include
#include
#include
using namespace std;

int minSwapsToSort(vector& arr) {
    int n = arr.size();
    vector> pairs(n);

    for (int i = 0; i < n; i++) {
        pairs[i] = {arr[i], i};
    }

    sort(pairs.begin(), pairs.end());

    vector visited(n, false);
    int swaps = 0;

    for (int i = 0; i < n; i++) {
        // If already visited or element is in the correct position, skip it.
        if (visited[i] || pairs[i].second == i)
            continue;

        int cycle_size = 0;
        int j = i;
        while (!visited[j]) {
            visited[j] = true;
            j = pairs[j].second;
            cycle_size++;
        }

        // For a cycle of size k, you need k-1 swaps.
        swaps += (cycle_size - 1);
    }

    return swaps;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        vector arr(n);
        for (int i = 0; i < n; i++) {
            cin >> arr[i];
        }

        cout << minSwapsToSort(arr) << "\n";
    }

    return 0;
}
```

#### Python Code for Approach 1:
```python
def min_swaps_to_sort(arr):
    n = len(arr)
    # Pair each element with its index
    arrpos = [(value, idx) for idx, value in enumerate(arr)]
    # Sort the array based on the element values
    arrpos.sort(key=lambda x: x[0])

    visited = [False] * n
    swaps = 0

    for i in range(n):
        # If the element is already visited or it's in the correct position, skip it
        if visited[i] or arrpos[i][1] == i:
            continue

        cycle_size = 0
        j = i
        while not visited[j]:
            visited[j] = True
            j = arrpos[j][1]
            cycle_size += 1

        # Add the number of swaps for this cycle (cycle_size - 1)
        swaps += (cycle_size - 1)

    return swaps

if __name__ == "__main__":
    import sys
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index:index+n]))
        index += n
        results.append(str(min_swaps_to_sort(arr)))
    sys.stdout.write("\n".join(results))
```

---

## Approach 2: Direct Swap Simulation

### Intuition:

1. **Sorting with Swaps:**
   In this approach, instead of explicitly finding cycles, we simulate placing each element into its correct position by swapping it with the element that is currently occupying that position.

2. **Using a Mapping:**
   We create a mapping (or dictionary) from element values to their current indices. We also prepare the sorted version of the array. We then iterate over the array, and whenever we find an element that is not at its sorted position, we swap it with the element which should be at that position.
   Every successful swap places at least one element in the correct position.

3. **Counting Swaps:**
   With each swap operation, we update the mapping and count the number of swaps. This simulation yields the same answer as the cycle decomposition method.

### Code Implementations:

#### C++ Code for Approach 2:
```cpp
#include
#include
#include
#include
using namespace std;

int minSwapsSimulate(vector& arr) {
    int n = arr.size();
    vector sorted_arr = arr;
    sort(sorted_arr.begin(), sorted_arr.end());

    // Create mapping from value to index
    unordered_map index_map;
    for (int i = 0; i < n; i++) {
        index_map[arr[i]] = i;
    }

    int swaps = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] != sorted_arr[i]) {
            swaps++;
            int correct_index = index_map[sorted_arr[i]];

            // Update the mapping for the two elements that are swapped.
            index_map[arr[i]] = correct_index;
            index_map[sorted_arr[i]] = i;

            // Swap the current element with the element at its correct position.
            swap(arr[i], arr[correct_index]);
        }
    }
    return swaps;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while(t--){
        int n;
        cin >> n;
        vector arr(n);
        for (int i = 0; i < n; i++){
            cin >> arr[i];
        }
        cout << minSwapsSimulate(arr) << "\n";
    }
    return 0;
}
```

#### Python Code for Approach 2:
```python
def min_swaps_simulate(arr):
    n = len(arr)
    sorted_arr = sorted(arr)

    # Mapping from element value to its index in the current array
    index_map = {value: i for i, value in enumerate(arr)}
    swaps = 0

    for i in range(n):
        if arr[i] != sorted_arr[i]:
            swaps += 1
            correct_index = index_map[sorted_arr[i]]

            # Swap the elements
            arr[i], arr[correct_index] = arr[correct_index], arr[i]

            # Update the mapping after swap
            index_map[arr[correct_index]] = correct_index
            index_map[arr[i]] = i
    return swaps

if __name__ == "__main__":
    import sys
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        arr = list(map(int, data[idx:idx+n]))
        idx += n
        results.append(str(min_swaps_simulate(arr)))
    sys.stdout.write("\n".join(results))
```

---

### Conclusion

Both approaches yield the correct answer with a time complexity of $$ \mathcal{O}(N \log N) $$ primarily because of the sorting step. The **Cycle Decomposition Method** is conceptually elegant and leverages the permutation cycle structure. On the other hand, the **Direct Swap Simulation** method implements the process in a more straightforward simulation of the swap operations. Both strategies are highly efficient and suitable for the given constraints.

Happy Coding!

</details>
