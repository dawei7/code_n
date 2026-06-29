# Cooking Machine

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | COOKMACH |
| Difficulty Rating | 1329 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Time Complexity |
| Official Link | [COOKMACH](https://www.codechef.com/practice/course/1to2stars/LP1TO205/problems/COOKMACH) |

---

## Problem Statement

Chef is on a vacation these days, so his friend Chefza is trying to solve Chef's everyday tasks.

Today's task is to make a sweet roll. Rolls are made by a newly invented cooking machine. The machine is pretty universal - it can make lots of dishes and Chefza is thrilled about this.

To make a roll, Chefza has to set all the settings to specified integer values. There are lots of settings, each of them set to some initial value. The machine is pretty complex and there is a lot of cooking to be done today, so Chefza has decided to use only two quick ways to change the settings. In a unit of time, he can pick one setting (let's say its current value is **v**) and change it in one of the following ways.

- If **v** is even, change this setting to **v/2**. If **v** is odd, change it to **(v − 1)/2**.

- Change setting to **2 × v**

The receipt is given as a list of integer values the settings should be set to. It is guaranteed that each destination setting can be represented as an integer power of **2**.

Since Chefza has just changed his profession, he has a lot of other things to do. Please help him find the **minimum** number of operations needed to set up a particular setting of the machine. You can prove that it can be done in finite time.

### Input

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

The only line of each test case contains two integers **A** and **B** denoting the initial and desired values of the setting, respectively.

### Output

For each test case, output a single line containing minimum number of operations Chefza has to perform in order to set up the machine.

### Constraints

- **1** ≤ **T** ≤ **200**

- **1** ≤ **A** ≤ **107**

- **1** ≤ **B** ≤ **107**, and **B** is an integer power of **2**

### Subtasks

- **Subtask #1 [40 points]: A ≤ 100 and B ≤ 100**

- **Subtask #2 [60 points]: No additional constraints**

---

## Examples

**Example 1**

**Input**

```text
6
1 1
2 4
3 8
4 16
4 1
1 4
```

**Output**

```text
0
1
4
2
2
2
```

**Explanation**

- In the first test case, you don't need to do anything.

- In the second test case, you need to multiply 2 by 2 and get 4. This is done in 1 operation.

- In the third test case, you need to obtain 1 from 3 and then multiply it by 2 three times to obtain 8. A total of 4 operations.

- In the fourth test case, multiply 4 by 2 twice.

- In the fifth test case, divide 4 by 2 twice.

- In the sixth test case, multiply 1 by 2 twice.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 1
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
2 4
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
3 8
```

**Output for this case**

```text
4
```



#### Test case 4

**Input for this case**

```text
4 16
```

**Output for this case**

```text
2
```



#### Test case 5

**Input for this case**

```text
4 1
```

**Output for this case**

```text
2
```



#### Test case 6

**Input for this case**

```text
1 4
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Contest](http://www.codechef.com/AUG15/problems/COOKMACH)

[Practice](http://www.codechef.com/problems/COOKMACH)

**Author:** [Maksym Bevza](https://www.codechef.com/users/cenadar)

**Tester:** [Hiroto Sekido](http://www.codechef.com/users/laycurse)

**Editorialist:** [Kevin Atienza](http://www.codechef.com/users/kevinsogo)

### DIFFICULTY:

Cakewalk

### PREREQUISITES:

Ad hoc, bitwise operators

### PROBLEM:

You need to convert an integer A to integer B, where both are positive and B is a power of two. The allowed moves are the following (if the current number is v):

- If v is even, replace it with v/2; if v is odd, replace it with (v-1)/2.

- Replace v with 2v.

What is the minimum number of moves to do this? (it can be shown that this is always possible!)

### QUICK EXPLANATION:

The fastest way is the following:

- Use the first step repeatedly until the number becomes a power of two.

- If the current number is larger than B, use the first step even further until the number becomes B. Otherwise, use the second step repeatedly until the number becomes B.

The number of steps this takes is the answer.

### EXPLANATION:

We will make use of the fact that the target integer, B, is a power of two. First, let’s notice what the operations really do.

The first operation roughly “halves” v, and the second operation doubles v. Thus, it makes sense to consider the binary representation of v.

In fact, the operations are simply the [Bitwise logical shift](https://en.wikipedia.org/wiki/Bitwise_operation#Logical_shift) operations! In other words, the first operation is simply a single right shift, and the second operation is a single left shift.

A **shift** is simply an operation that “shifts” the binary representation of a number. For example, shifting the binary integer “1001101” left once results in “10011010”. Note that we use a “0” for new digit places. Also, when shifting right, the rightmost digit is discarded: for example, the right shift of “1001101” and “1001100” are both “100110”. It’s fairly straightforward to see why the operations described in the problem statement are simply shifts.

With this in mind, how do we quickly go from A to B? Since B is a power of two, it has exactly one 1 in its binary representation. Notice that using either operation doesn’t increase the number of 1 s in the binary representation of a number. Therefore, the first action we must do is to convert the initial number into one that contains a single 1 in its binary representation (i.e. a power of two). To do this, we shift right, until it becomes a power of two.

Now that our number is already a power of two, we can simply shift left or right repeatedly until it becomes equal to B!

The answer is simply the total number of shifts in both steps combined, and it’s quite easy and intuitive to see why this is the optimal solution.

The following is an implementation in C++:

``#include <stdio.h>
#include <stdlib.h>

int main() {
    int z;
    scanf("%d", &z);
    while (z--) {
        int a, b;
        scanf("%d%d", &a, &b);
        int steps = 0;
        while ((a & -a) != a) a >>= 1, steps++;
        while (a < b) a <<= 1, steps++;
        while (a > b) a >>= 1, steps++;
        printf("%d\n", steps);
    }
}
``

# A somewhat faster solution

We can use a few more [bitwise](https://en.wikipedia.org/wiki/Bitwise_operation) tricks to compute the answer without performing the steps themselves. Notice that there are two parts in calculating the answer:

- Use the first step repeatedly until the number becomes a power of two.

- If the current number is larger than B, use the first step even further until the number becomes B. Otherwise, use the second step repeatedly until the number becomes B.

How can we calculate the number of steps required in part one? Note that the answer is simply one more than the position from the right of the second most significant bit of A, or zero if there isn’t such a bit (i.e. A is a power of two already). We can compute this value quickly if we can perform the following operation quickly:

- Extract the position of the second largest bit of a number

It can be dissected into a series of the following operations:

- Extract the largest bit of a number.

- Remove a particular bit of a number.

- Get the place value of a particular bit, i.e. given v = 2^i, compute i.

Removing a particular bit is easy; the number `A` with the bit `b` removed is simply `A ^ b`, where `^` is the bitwise XOR operator. (This expression assumes that `b` is found in `A`. If you can’t guarantee it, use the expression `A ^ ~b` instead, where `~` is the bitwise NOT operator) The first operation (“extract the largest bit”) can be done with the following pseudocode which works for [32-bit](https://en.wikipedia.org/wiki/32-bit) integers (we invite the reader to see why this works):

``int maxbit(int v) {
    v |= v >> 1;
    v |= v >> 2;
    v |= v >> 4;
    v |= v >> 8;
    v |= v >> 16;
    return v ^ (v >> 1);
}
``

Now, how do we implement the last one? Given v = 2^i, we want to compute i. Note that i is simply **the number of 1 bits in the number v-1**! But how do we count the 1 bits in a given number? It can be done with the following pseudocode (once again, we invite the reader to see why this works):

``int bitcount(int v) {
    v = (v & 0x55555555) + ((v >>  1) & 0x55555555);
    v = (v & 0x33333333) + ((v >>  2) & 0x33333333);
    v = (v & 0x0f0f0f0f) + ((v >>  4) & 0x0f0f0f0f);
    v = (v & 0x00ff00ff) + ((v >>  8) & 0x00ff00ff);
    v = (v & 0x0000ffff) + ((v >> 16) & 0x0000ffff);
    return v;
}
``

With these, we can now extract the position of the second largest bit of a number:

``int extractsecond(int v) {
    v ^= maxbit(v);
    if (v == 0) {
        // v was originally a power of two
        return 0;
    } else {
        return bitcount(maxbit(v) - 1) + 1;
    }
}
``

Now, for the second part: assuming the current number A is a power of two, how many steps do we need to convert it to B? This is very simple: it’s just the difference between the positions of the bits of A and B, i.e. `abs(bitcount(A-1) - bitcount(B-1))`! Therefore, we now have the following (somewhat faster) solution:

``#include <stdio.h>
#include <stdlib.h>
#define ll long long

int maxbit(int v) {
    v |= v >> 1;
    v |= v >> 2;
    v |= v >> 4;
    v |= v >> 8;
    v |= v >> 16;
    return v ^ (v >> 1);
}

int bitcount(int v) {
    v = (v & 0x55555555) + ((v >>  1) & 0x55555555);
    v = (v & 0x33333333) + ((v >>  2) & 0x33333333);
    v = (v & 0x0f0f0f0f) + ((v >>  4) & 0x0f0f0f0f);
    v = (v & 0x00ff00ff) + ((v >>  8) & 0x00ff00ff);
    v = (v & 0x0000ffff) + ((v >> 16) & 0x0000ffff);
    return v;
}

int extractsecond(int v) {
    v ^= maxbit(v);
    if (v == 0) {
        // v was originally a power of two
        return 0;
    } else {
        return bitcount(maxbit(v) - 1) + 1;
    }
}

int main() {
    int z;
    scanf("%d", &z);
    while (z--) {
        int a, b;
        scanf("%d%d", &a, &b);
        int steps = extractsecond(a);
        a >>= steps;
        steps += abs(bitcount(a - 1) - bitcount(b - 1));
        printf("%d\n", steps);
    }
}
``

### Time Complexity:

O(\log A + \log B) or O(\log \log A + \log \log B)

### AUTHOR’S AND TESTER’S SOLUTIONS:

[setter](http://www.codechef.com/download/Solutions/AUG15/Setter/COOKMACH.cpp)

[tester](http://www.codechef.com/download/Solutions/AUG15/Tester/COOKMACH.cpp)

</details>
