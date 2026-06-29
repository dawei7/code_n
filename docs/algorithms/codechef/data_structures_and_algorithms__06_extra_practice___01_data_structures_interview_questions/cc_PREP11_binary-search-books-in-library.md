# Binary Search - Books in Library

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP11 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Binary Search |
| Official Link | [PREP11](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_06/problems/PREP11) |

---

## Problem Statement

Chef has $N$ books in the library where the number of pages in the $i^{th}$ book is $B_i$. These numbers, $B_1, B_2, \dots,B_N$, are given to you. Chef will allocate all these $N$ books to $A$ students in contiguous order, which means that the $i^{th}$ student will be allocated a contiguous set of books (ie. $B_j, B_{j+1}, \dots,B_{j+k}$, for some $j$ and $k$). Every student should be allocated at least one book. **Minimize** the **maximum** sum of pages allocated to a student. Find that **minimum** value.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first line of each test case contains two space-separated integers $N$, $A$ — the number books and students.
- The second line of each test case contains $N$ space-separated integers $B_1,B_2,\ldots,B_N$.

---

## Output Format

For each test case, output on a new line the answer.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 10^5$
- $1 \leq A \leq N$
- $1 \leq B_i \leq 10^5$
- The sum of $N$ over all test cases won't exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
2
5 2
4 8 2 6 10
5 5
10 5 10 12 18
```

**Output**

```text
16
18
```

**Explanation**

**Test case $1$**: First student will be allocated books $[4, 8]$, other student will be allocated books $[2, 6, 10]$. So sum of pages will be $12$, $16$ and maximum of them will be $16$. No other optimal way possible to allocate books.

**Test case $2$**: Each student will be allocated one book and maximum of them will be $18$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 2
4 8 2 6 10
```

**Output for this case**

```text
16
```



#### Test case 2

**Input for this case**

```text
5 5
10 5 10 12 18
```

**Output for this case**

```text
18
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial: Minimizing Maximum Sum of Pages – Book Allocation Problem

In this problem, you are given $N$ books with an array of page numbers $B_1, B_2, \dots, B_N$, and you must allocate them to $A$ students. The twist is that the books must be assigned in contiguous segments, and every student must receive at least one book. Your goal is to **minimize the maximum** number of pages any student reads.

There are multiple ways to approach this problem. Below, we discuss the widely used **Approach 1: Greedy Partitioning with Binary Search** along with a brief mention of an alternative method.

---

## Approach 1: Greedy Partitioning with Binary Search

### Intuition
This approach uses binary search combined with a greedy check. The idea is to set a candidate value $M$, which represents the maximum pages a student can be assigned, and then verify if it is possible to partition the books into contiguous segments such that no segment has a total greater than $M$.

1. **Setting the Binary Search Range:**
   - The minimum candidate value $L$ is the number of pages in the largest book:
     $$ L = \max(B_1, B_2, \dots, B_N) $$
   - The maximum candidate value $H$ is the sum of all pages:
     $$ H = \sum_{i=1}^{N} B_i $$

2. **Greedy Feasibility Check:**
   For any candidate $M$, iterate over the books and accumulate pages for the current student. When adding the next book would exceed $M$, move on to the next student. If more than $A$ students are needed, then $M$ is too low.

3. **Optimizing via Binary Search:**
   Adjust the candidate $M$ using binary search based on the feasibility check until you pinpoint the minimum value that works.

### Complexity
The binary search executes in $O(\log(\sum B_i))$ iterations, and the feasibility check operates in $O(N)$ time. Consequently, the overall complexity is $O(N \log(\sum B_i))$, making it efficient for large inputs.

### Code Implementation

Below is the **C++** implementation:

```cpp
#include
using namespace std;

bool isPossible(vector& books, int students, long long maxPages) {
    int count = 1;
    long long currentPages = 0;
    for (int pages : books) {
        if (pages > maxPages) return false;
        if (currentPages + pages > maxPages) {
            count++;
            currentPages = pages;
        } else {
            currentPages += pages;
        }
    }
    return count <= students;
}

long long allocateBooks(vector& books, int students) {
    long long low = *max_element(books.begin(), books.end());
    long long high = accumulate(books.begin(), books.end(), 0LL);
    long long result = high;

    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (isPossible(books, students, mid)) {
            result = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    return result;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;
    while (t--) {
        int n, a;
        cin >> n >> a;
        vector books(n);
        for (int i = 0; i < n; i++) {
            cin >> books[i];
        }
        cout << allocateBooks(books, a) << "\n";
    }
    return 0;
}
```

And here is the **Python** implementation:

```python
def is_possible(books, students, max_pages):
    count = 1
    current_pages = 0
    for pages in books:
        if pages > max_pages:
            return False
        if current_pages + pages > max_pages:
            count += 1
            current_pages = pages
        else:
            current_pages += pages
    return count <= students

def allocate_books(books, students):
    low, high = max(books), sum(books)
    result = high
    while low <= high:
        mid = (low + high) // 2
        if is_possible(books, students, mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    return result

if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read().split()
    t = int(input_data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(input_data[index])
        students = int(input_data[index + 1])
        index += 2
        books = list(map(int, input_data[index:index + n]))
        index += n
        results.append(allocate_books(books, students))
    print("\n".join(map(str, results)))
```

---

## Approach 3: Recursive Backtracking (Not Recommended)

An alternative method involves recursively exploring all possible ways to partition the books and choosing the allocation that minimizes the maximum sum. Although this approach will eventually find the correct answer, its exponential time complexity makes it impractical for large input sizes. This method is mentioned here solely for educational purposes.

---

### Conclusion

For practical applications, especially given the problem constraints, **Approach 1 (Greedy Partitioning with Binary Search)** is the most efficient and straightforward solution. The recursive backtracking approach is included only for completeness and is not recommended for real-world use.

Happy Coding and Best of Luck with your DSA Interviews!

</details>
