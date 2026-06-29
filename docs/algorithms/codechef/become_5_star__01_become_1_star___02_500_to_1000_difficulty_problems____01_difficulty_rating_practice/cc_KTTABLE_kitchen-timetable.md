# Kitchen Timetable

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | KTTABLE |
| Difficulty Rating | 997 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [KTTABLE](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/KTTABLE) |

---

## Problem Statement

There are **N** students living in the dormitory of Berland State University. Each of them sometimes wants to use the kitchen, so the head of the dormitory came up with a timetable for kitchen's usage in order to avoid the conflicts:

- The first student starts to use the kitchen at the time **0** and should finish the cooking not later than at the time **A1**.

- The second student starts to use the kitchen at the time **A1** and should finish the cooking not later than at the time **A2**.

- And so on.

- The **N**-th student starts to use the kitchen at the time **AN-1** and should finish the cooking not later than at the time **AN**

The holidays in Berland are approaching, so today each of these **N** students wants to cook some pancakes. The **i**-th student needs **Bi** units of time to cook.

The students have understood that probably not all of them will be able to cook everything they want. How many students will be able to cook without violating the schedule?

---

## Input Format

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows. \
Each test case contains 3 lines of input
- The first line of each test case contains a single integer **N** denoting the number of students.
- The second line contains **N** space-separated integers **A1**, **A2**, ..., **AN** denoting the moments of time by when the corresponding student should finish cooking.
- The third line contains **N** space-separated integers **B1**, **B2**, ..., **BN** denoting the time required for each of the students to cook.

---

## Output Format

For each test case, output a single line containing the number of students that will be able to finish the cooking.

---

## Constraints

**1** ≤ **T** ≤ **10** \
**1** ≤ **N** ≤ **104** \
**0** < **A1** <  **A2** < ... < **AN** < **109** \
**1** ≤ **Bi** ≤ **109**

---

## Examples

**Example 1**

**Input**

```text
2
3
1 10 15
1 10 3
3
10 20 30
15 5 20
```

**Output**

```text
2
1
```

**Explanation**

**Example case 1.** The first student has **1** unit of time - the moment **0**. It will be enough for her to cook. The second student has **9** units of time, but wants to cook for **10** units of time, and won't fit in time. The third student has **5** units of time and will fit in time, because needs to cook only for **3** units of time.

**Example case 2.** Each of students has **10** units of time, but only the second one will be able to fit in time.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
1 10 15
1 10 3
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
3
10 20 30
15 5 20
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Contest](http://www.codechef.com/SNCKQL16/problems/KTTABLE)

[Practice](http://www.codechef.com/problems/KTTABLE)

**Author:** [Sergey Kulik](http://www.codechef.com/users/xcwgf666)

**Testers:** [Kevin Atienza](http://www.codechef.com/users/kevinsogo) and [Vasya Antoniuk](http://www.codechef.com/users/antoniuk1)

**Translators:** [Sergey Kulik](http://www.codechef.com/users/xcwgf666) (Russian), [Team VNOI](http://www.codechef.com/users/vnoi) (Vietnamese) and [Hu Zecong](http://www.codechef.com/users/huzecong) (Mandarin)

**Editorialist:** [Kevin Atienza](http://www.codechef.com/users/kevinsogo)

### DIFFICULTY:

Cakewalk

### PREREQUISITES:

Loops, Arrays

### PROBLEM:

There are N students. Only one student can use the dormitory kitchen at at time. The head came up with a timetable for the kitchen’s usage to avoid conflicts:

- The first student starts to use the kitchen at the time 0 and should finish the cooking not later than at the time A_1.

- The second student starts to use the kitchen at the time A_1 and should finish the cooking not later than at the time A_2.

- And so on.

The i th student needs B_i units of time to cook. How many students will be able to cook without violating the schedule?

### EXPLANATION:

The i th student has at most A_i - A_{i-1} units of time to cook, so he/she can cook if and only if B_i \le A_i - A_{i-1}. So the answer is simply the number of indices i such that B_i \le A_i - A_{i-1}. For simplicity of implementation, we can just define A_0 = 0.

The following are implementations in some popular languages.

C++:

``#include <iostream>
using namespace std;

int a[10011];

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        a[0] = 0;
        for (int i = 1; i <= n; i++) {
            cin >> a[i];
        }
        int ans = 0;
        for (int i = 1; i <= n; i++) {
            int bi;
            cin >> bi;
            if (bi <= a[i] - a[i-1]) {
                ans++;
            }
        }
        cout << ans << endl;
    }
}
``

Java:

``import java.util.Scanner;

public class Main {
    public static void main (String args[]) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        int a[] = new int[10011];
        for (int cas = 0; cas < t; cas++) {
            int n = sc.nextInt();
            for (int i = 1; i <= n; i++) {
                a[i] = sc.nextInt();
            }
            int ans = 0;
            for (int i = 1; i <= n; i++) {
                int bi = sc.nextInt();
                if (bi <= a[i] - a[i-1]) {
                    ans++;
                }
            }
            System.out.println(ans);
        }
    }
}
``

Python:

``for cas in xrange(input()):
    n = input()
    a = [0] + map(int, raw_input().strip().split())
    b = map(int, raw_input().strip().split())
    print sum(b[i] <= a[i+1] - a[i] for i in xrange(n))
``

*Implementation notes*:

- In C++ and Java, the array A was allocated before processing any test case. This allows us to reuse the same array for multiple test cases which is faster than allocating new arrays every time. And actually, we allocated more than necessary. This is to preempt out-of-bounds errors.

- In C++ and Java, we didn’t collect the B values in an array. We just computed them on the fly and then threw them away immediately. Even though we saved some memory by not needing another array, there’s no big need in doing this. But in some problems, you’ll occasionally find yourself nearing the memory limit, so keep in mind such techniques because they are useful.

- In Java, we used `java.util.Scanner`, but take note that `Scanner` is slow, so in some problems with really large input, this approach will exceed the time limit just from taking the input. In those cases, use `java.io.BufferedReader` instead.

- Similarly, in C++, `cin` and `cout` is slow. The recommended way is to use `printf` and `scanf`, i.e., the “C way”.

- In Python, we used the *list comprehension* `sum(b[i] <= a[i+1] - a[i] for i in xrange(n))` to compute the answer in one line. This takes advantage of the fact that in Python, `True == 1` and `False == 0`. A much intuitive version would be `sum(1 for i in xrange(n) if b[i] <= a[i+1] - a[i])`.

### Time Complexity:

O(N)

### AUTHOR’S AND TESTER’S SOLUTIONS:

[Setter](https://codechef.com/download/Solutions/SNCKQL16/Setter/KTTABLE.cpp)

[Tester](https://codechef.com/download/Solutions/SNCKQL16/Tester/KTTABLE.cpp)

[Editorialist](https://codechef.com/download/Solutions/SNCKQL16/Editorialists/KTTABLE.py)

</details>
