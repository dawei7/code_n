# RestroPay

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SHARE |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Basic programming - 2 |
| Official Link | [SHARE](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_02/problems/SHARE) |

---

## Problem Statement

Tanny and Purgi are two very good friends. They went to a nice restaurant for some good dinner after a long taxing week. Tanny has n banknotes of value $a_1,a_2,a_3,a_4,......,a_n$ dollars. Similarly Purgi has m banknotes of values $b_1,b_2,b_3,b_4,........,b_m$ dollars.

Their bill came out to be $C$ dollars. Is it possible for them to pay the bill if both of them can just pay with exactly 1 banknote?

---

## Input Format

- The first line will have 3 integers $n,m,c$ separated by a space.
- The second and third line will contain the values of the banknotes Tanny and Purgi (separated by a space) respectively.

---

## Output Format

Output $YES$ if it is possible to pay the bill using just 2 banknotes ( one from Purgi and one from Tanny).
Else output $NO$.

---

## Constraints

- $1 \leq n \leq 10^5$
- $1 \leq m \leq 10^5$
- $1 \leq c \leq 2*10^9$
- $0 \leq a_i,b_i \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
4 5 34
1 2 3 4
12 43 23 33 44
```

**Output**

```text
YES
```

**Explanation**

If Tanny pays a 1 dollar banknote and Purgi pays the 33 dollar banknote, they can pay the bill of 34 dollars.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this tutorial, we explore different methods to determine if Tanny and Purgi can pay their bill of $C$ dollars using exactly one banknote from each. Recall that Tanny has $n$ banknotes with values $a_1,a_2,\dots,a_n$, and Purgi has $m$ banknotes with values $b_1,b_2,\dots,b_m$. We need to determine if there exists a pair $(a_i, b_j)$ such that

$$
a_i + b_j = c.
$$

Below, we discuss three approaches, complete with code in both C++ and Python.

---

### Approach 1: Hash Set (Dictionary) Method

**Idea:**
- Create a hash set (or dictionary) for one of the lists (we choose Purgi's list).
- For each banknote in Tanny's list, check if $(c - \text{banknote})$ exists in the set.

This approach has an average time complexity of $O(n + m)$ and is efficient given the constraints.

**C++ Code:**
```cpp
#include
#include
#include
using namespace std;

bool canPayBill(const vector& tanny, const vector& purgi, int c) {
    unordered_set purgiSet;
    for (int note : purgi) {
        purgiSet.insert(note);
    }
    for (int note : tanny) {
        if (note <= c && purgiSet.count(c - note)) {
            return true;
        }
    }
    return false;
}

int main() {
    int n, m, c;
    cin >> n >> m >> c;
    vector tanny(n), purgi(m);
    for (int i = 0; i < n; i++) {
        cin >> tanny[i];
    }
    for (int j = 0; j < m; j++) {
        cin >> purgi[j];
    }
    cout << (canPayBill(tanny, purgi, c) ? "YES" : "NO") << endl;
    return 0;
}
```

**Python Code:**
```python
def can_pay_bill(tanny, purgi, c):
    purgi_set = set(purgi)
    for note in tanny:
        if note <= c and (c - note) in purgi_set:
            return True
    return False

def main():
    import sys
    data = sys.stdin.read().split()
    n, m, c = map(int, data[:3])
    tanny = list(map(int, data[3:3+n]))
    purgi = list(map(int, data[3+n:3+n+m]))
    print("YES" if can_pay_bill(tanny, purgi, c) else "NO")

if __name__ == "__main__":
    main()
```

---

### Approach 2: Two-Pointer Technique After Sorting

**Idea:**
- Sort both lists.
- Use two pointers: one starting at the beginning of Tanny’s list and the other starting at the end of Purgi’s list.
- If the sum of the pointed elements is equal to $c$, the answer is "YES".
- If the sum is less than $c$, move the pointer in Tanny’s list forward; if greater, move the pointer in Purgi’s list backward.

This method takes $O(n \log n + m \log m)$ due to sorting, followed by a linear scan.

**C++ Code:**
```cpp
#include
#include
#include
using namespace std;

bool canPayBill(vector& tanny, vector& purgi, int c) {
    sort(tanny.begin(), tanny.end());
    sort(purgi.begin(), purgi.end());
    int i = 0, j = purgi.size() - 1;
    while(i < tanny.size() && j >= 0){
        int sum = tanny[i] + purgi[j];
        if(sum == c) return true;
        if(sum < c)
            i++;
        else
            j--;
    }
    return false;
}

int main() {
    int n, m, c;
    cin >> n >> m >> c;
    vector tanny(n), purgi(m);
    for (int i = 0; i < n; i++) {
        cin >> tanny[i];
    }
    for (int j = 0; j < m; j++) {
        cin >> purgi[j];
    }
    cout << (canPayBill(tanny, purgi, c) ? "YES" : "NO") << endl;
    return 0;
}
```

**Python Code:**
```python
def can_pay_bill(tanny, purgi, c):
    tanny.sort()
    purgi.sort()
    i, j = 0, len(purgi) - 1
    while i < len(tanny) and j >= 0:
        current_sum = tanny[i] + purgi[j]
        if current_sum == c:
            return True
        elif current_sum < c:
            i += 1
        else:
            j -= 1
    return False

def main():
    import sys
    data = sys.stdin.read().split()
    n, m, c = map(int, data[:3])
    tanny = list(map(int, data[3:3+n]))
    purgi = list(map(int, data[3+n:3+n+m]))
    print("YES" if can_pay_bill(tanny, purgi, c) else "NO")

if __name__ == "__main__":
    main()
```

---

### Approach 3: Binary Search Approach

**Idea:**
- Sort one of the lists (we choose Purgi’s list).
- For each banknote from Tanny, use binary search to find if $(c - \text{banknote})$ exists in Purgi’s sorted list.

This method has a time complexity of $O(m \log m + n \log m)$, which is efficient if one of the lists is much smaller or comparable in size.

**C++ Code:**
```cpp
#include
#include
#include
using namespace std;

bool canPayBill(const vector& tanny, vector& purgi, int c) {
    sort(purgi.begin(), purgi.end());
    for (int note : tanny) {
        int target = c - note;
        if(target < 0)
            continue;
        if (binary_search(purgi.begin(), purgi.end(), target)) {
            return true;
        }
    }
    return false;
}

int main() {
    int n, m, c;
    cin >> n >> m >> c;
    vector tanny(n), purgi(m);
    for (int i = 0; i < n; i++) {
        cin >> tanny[i];
    }
    for (int j = 0; j < m; j++) {
        cin >> purgi[j];
    }
    cout << (canPayBill(tanny, purgi, c) ? "YES" : "NO") << endl;
    return 0;
}
```

**Python Code:**
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

def can_pay_bill(tanny, purgi, c):
    purgi.sort()
    for note in tanny:
        target = c - note
        if target < 0:
            continue
        if binary_search(purgi, target):
            return True
    return False

def main():
    import sys
    data = sys.stdin.read().split()
    n, m, c = map(int, data[:3])
    tanny = list(map(int, data[3:3+n]))
    purgi = list(map(int, data[3+n:3+n+m]))
    print("YES" if can_pay_bill(tanny, purgi, c) else "NO")

if __name__ == "__main__":
    main()
```

---

### Summary

- **Approach 1:** Uses a hash set for fast look-up. It is intuitive and works in $O(n + m)$ average time.
- **Approach 2:** Sorts both lists and uses the two-pointer technique. It is efficient if sorting is affordable.
- **Approach 3:** Sorts one list and leverages binary search, giving a clear $O(n \log m)$ (or $O(m \log m + n \log m)$) solution.

Each approach has its own benefits, and understanding them gives you versatile tools to solve similar pair-sum problems. Choose the one that best fits your problem constraints and familiarity.

Happy coding!

</details>
