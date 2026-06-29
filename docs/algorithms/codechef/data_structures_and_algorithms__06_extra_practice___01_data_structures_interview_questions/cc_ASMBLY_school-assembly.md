# School Assembly

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ASMBLY |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Basic programming - 2 |
| Official Link | [ASMBLY](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_02/problems/ASMBLY) |

---

## Problem Statement

During the assembly, a teacher lines up $N$ students in a line in front of her. She can see the first student and all the students taller than the students before them ( i.e a teacher can see the student $i$  if  $h_i \gt h_j$   for all $j$ ,$j \le i $ ). How many students will the teacher be able to see?

---

## Input Format

- The first line will have 1 integer $N$.
- The second line will contain the heights of the students which would be integers  in the order of them getting farther from the teacher. (will be separated by a space)

---

## Output Format

Output a single integer which is the amount of students the teacher will be able to see.

---

## Constraints

- $1 \leq N \leq 10^5$
- $2 \leq h_i \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
9
1 2 3 4 5 6 7 8 9
```

**Output**

```text
9
```

**Explanation**

The teacher will be able to see all the students.

**Example 2**

**Input**

```text
4
1 2 4 3
```

**Output**

```text
3
```

**Explanation**

The teacher will not be able to see the 4th student as the height of the 3rd student has height higher than him.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial: Counting Visible Students

In this lesson, we need to determine how many students a teacher can see in a line. The teacher can see the first student and any student who is taller than all the students before them. Formally, if $h_i$ represents the height of the $i^{th}$ student, the teacher can see student $i$ if

$$
h_i > \max_{1 \leq j < i} \{h_j\}.
$$

Below, we discuss two approaches to solving this problem along with code in both C++ and Python for each approach.

---

## Approach 1: Simple Iteration

### Idea:
Traverse the list of student heights once while keeping track of the maximum height encountered so far. The teacher is able to see a student if that student's height is greater than the current maximum height.

### Explanation:
- **Initialize:** Set a counter `count` to 1 (since the first student is always visible) and `max_height` to the height of the first student.
- **Iterate:** For each subsequent student (from index 1 to $N-1$), if the current student's height is greater than `max_height`, increment the counter and update `max_height` to the current student's height.
- **Complexity:** This method runs in $O(N)$ time.

### Code Implementation:
#### C++:
```cpp
#include
#include
using namespace std;

int main(){
    int N;
    cin >> N;
    vector heights(N);
    for (int i = 0; i < N; i++){
        cin >> heights[i];
    }
    int count = 1;  // First student is always visible
    int maxHeight = heights[0];
    for (int i = 1; i < N; i++){
        if (heights[i] > maxHeight){
            count++;
            maxHeight = heights[i];
        }
    }
    cout << count << endl;
    return 0;
}
```

#### Python:
```python
N = int(input())
heights = list(map(int, input().split()))
visible_students = 1  # First student is always visible
max_height = heights[0]
for height in heights[1:]:
    if height > max_height:
        visible_students += 1
        max_height = height
print(visible_students)
```

---

## Approach 2: Using a Monotonic Stack

### Idea:
We can simulate the teacher’s view using a monotonic stack that stores the heights of the visible students in order. For each student, if the stack is empty or the student's height is greater than the top of the stack, then the student is visible and can be added to the stack.

### Explanation:
- **Stack Initialization:** Start with an empty stack.
- **Process Each Student:** For each student, check if the stack is empty or if the current student’s height exceeds the height on the top of the stack. If yes, increment the visible counter and push their height onto the stack.
- **Complexity:** This runs in $O(N)$ time.

### Code Implementation:
#### C++:
```cpp
#include
#include
#include
using namespace std;

int main(){
    int n;
    cin >> n;
    vector heights(n);
    for (int i = 0; i < n; i++){
        cin >> heights[i];
    }
    int visible = 0;
    stack st;
    for (int i = 0; i < n; i++){
        if (st.empty() || heights[i] > st.top()){
            visible++;
            st.push(heights[i]);
        }
    }
    cout << visible << endl;
    return 0;
}
```

#### Python:
```python
n = int(input())
heights = list(map(int, input().split()))
visible = 0
stack = []
for height in heights:
    if not stack or height > stack[-1]:
        visible += 1
        stack.append(height)
print(visible)
```

</details>
