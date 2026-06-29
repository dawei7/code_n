# Bit Manipulation - Single Number

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP45 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Bit Manipulation |
| Official Link | [PREP45](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_15/problems/PREP45) |

---

## Problem Statement

You are given an array $A_1, A_2, \dots, A_N$ of length $N$. Each distinct element appears twice except for one. Find that single one.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first line of each test case contains an integer $N$ - the length of the array $A$.
- The second line of each test case contains $N$ space-separated integers $A_1,A_2,\ldots,A_N$.

---

## Output Format

For each test case, output on a new line the single one.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ over all test cases won't exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
1
5
5
2 5 2 10 10
5
1 1 10 10 15
5
6 8 10 6 8
```

**Output**

```text
5
5
15
10
```

**Explanation**

**Test case $1$**: Distinct elements will be $5$. The single element will be $5$.

**Test case $2$**: Distinct elements will be $2$, $5$, $10$. The single element will be $5$.

**Test case $3$**: Distinct elements will be $1$, $10$, $15$. The single element will be $15$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
5
```

**Output for this case**

```text
5
```



#### Test case 2

**Input for this case**

```text
5
2 5 2 10 10
```

**Output for this case**

```text
5
```



#### Test case 3

**Input for this case**

```text
5
1 1 10 10 15
```

**Output for this case**

```text
15
```



#### Test case 4

**Input for this case**

```text
5
6 8 10 6 8
```

**Output for this case**

```text
10
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this lesson, we will explore three different approaches to solve the problem of finding the unique element in an array where every element appears twice except one. Each approach has its own trade-offs in terms of time and space complexity. Let’s go through them one by one.

---

### Approach 1: Bitwise XOR

The XOR operation has very useful properties for this problem. In particular, the properties:
- $a \oplus a = 0$
- $0 \oplus a = a$

allow us to cancel out the duplicate numbers. If we initialize a result to $0$ and XOR every element in the array with it, the duplicate elements will cancel out and we will be left with the unique element. This solution runs in $O(n)$ time and requires $O(1)$ extra space, making it the most efficient.

**C++ Code:**
```cpp
#include
#include
using namespace std;

int main(){
    int T;
    cin >> T;
    while(T--){
        int N;
        cin >> N;
        int result = 0;
        for (int i = 0; i < N; i++){
            int num;
            cin >> num;
            result ^= num;
        }
        cout << result << "\n";
    }
    return 0;
}
```

**Python Code:**
```python
T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 0
    for num in arr:
        result ^= num
    print(result)
```

---

### Approach 2: Using a Frequency Counter (Hash Table)

In this approach, we create a frequency counter (or hash table) to store the occurrence count of each number. Since every number except one appears twice, the number with a count of $1$ is our answer. Although this approach also runs in $O(n)$ time, it uses extra space proportional to the number of unique elements. This method is intuitive and helps reinforce the idea of frequency mapping.

**C++ Code:**
```cpp
#include
#include
#include
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while(T--){
        int N;
        cin >> N;
        unordered_map freq;
        vector arr(N);
        for (int i = 0; i < N; i++){
            cin >> arr[i];
            freq[arr[i]]++;
        }
        for (auto &p : freq){
            if(p.second == 1){
                cout << p.first << "\n";
                break;
            }
        }
    }
    return 0;
}
```

**Python Code:**
```python
T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    for key, value in freq.items():
        if value == 1:
            print(key)
            break
```

---

### Approach 3: Sorting

The sorting approach involves sorting the array and then checking adjacent elements. Since duplicate elements will appear next to each other in a sorted array, a unique element will be the one that does not have an identical neighbor. Special care is taken to check the beginning and the end of the array. This approach has a time complexity of $O(n \log n)$ due to sorting, but requires $O(1)$ extra space (depending on the sorting algorithm used).

**C++ Code:**
```cpp
#include
#include
#include
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while(T--){
        int N;
        cin >> N;
        vector arr(N);
        for(int i = 0; i < N; i++){
            cin >> arr[i];
        }
        sort(arr.begin(), arr.end());
        int unique = 0;
        bool found = false;
        for (int i = 0; i < N - 1; i += 2){
            if(arr[i] != arr[i+1]){
                unique = arr[i];
                found = true;
                break;
            }
        }
        if(!found)
            unique = arr[N-1];
        cout << unique << "\n";
    }
    return 0;
}
```

**Python Code:**
```python
T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    unique = None
    i = 0
    while i < N - 1:
        if arr[i] != arr[i+1]:
            unique = arr[i]
            break
        i += 2
    if unique is None:
        unique = arr[-1]
    print(unique)
```

---

In summary, the XOR approach is optimal for this problem due to its simplicity and efficiency with constant space. The frequency counter approach, while requiring additional space, is straightforward and intuitive. The sorting approach offers an alternative by leveraging the order of elements but generally performs slightly slower due to the sorting step.

Each method provides valuable insights into problem-solving techniques, and understanding all three improves your mastery over different algorithmic strategies.

</details>
