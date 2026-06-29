# Palindromic substrings

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | STRPALIN |
| Difficulty Rating | 1238 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [STRPALIN](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/STRPALIN) |

---

## Problem Statement

Chef likes strings a lot but he likes palindromic strings more. Today, Chef has two strings **A** and **B**, each consisting of lower case alphabets.

Chef is eager to know whether it is possible to choose some **non empty** strings **s1** and **s2** where **s1** is a substring of **A**, **s2** is a substring of **B** such that **s1 + s2** is a palindromic string. Here **'+'** denotes the concatenation between the strings.

**Note:**

A string is a palindromic string if it can be read same both forward as well as backward. To know more about palindromes click [here](https://en.wikipedia.org/wiki/Palindrome).

### Input

- First line of input contains a single integer **T** denoting the number of test cases.

- For each test case:

- First line contains the string **A**

- Second line contains the string **B**.

### Output

For each test case, Print **"Yes"** (without quotes) if it possible to choose such strings **s1 & s2**. Print **"No"** (without quotes) otherwise.

### Constraints

- **1 ≤ T ≤ 10 **

- **1 ≤ |A|, |B| ≤ 1000 **

### Subtasks

-  **Subtask 1:** **1 ≤ |A|, |B| ≤ 10** : ( 40 pts )

-  **Subtask 2:** **1 ≤ |A|, |B| ≤ 1000** : ( 60 pts )

---

## Examples

**Example 1**

**Input**

```text
3
abc
abc
a
b
abba
baab
```

**Output**

```text
Yes
No
Yes
```

**Explanation**

- **Test 1:** One possible way of choosing **s1 & s2** is **s1 = "ab"**, **s2 = "a"** such that **s1 + s2** i.e **"aba"** is a palindrome.

- **Test 2:** There is no possible way to choose **s1 & s2** such that **s1 + s2** is a palindrome.

- **Test 3:** You can figure it out yourself.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
abc
abc
```

**Output for this case**

```text
Yes
```



#### Test case 2

**Input for this case**

```text
a
b
```

**Output for this case**

```text
No
```



#### Test case 3

**Input for this case**

```text
abba
baab
```

**Output for this case**

```text
Yes
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Contest](http://www.codechef.com/MARCH16/problems/STRPALIN)

[Practice](http://www.codechef.com/problems/STRPALIN)

**Author:** [Sunny Aggarwal](http://www.codechef.com/users/ma5termind)

**Tester:** [Kevin Atienza](http://www.codechef.com/users/kevinsogo)

**Translators:** [Vasya Antoniuk](http://www.codechef.com/users/antoniuk1) (Russian), [Team VNOI](http://www.codechef.com/users/vnoi) (Vietnamese) and [Hu Zecong](http://www.codechef.com/users/huzecong) (Mandarin)

**Editorialist:** [Kevin Atienza](http://www.codechef.com/users/kevinsogo)

### DIFFICULTY:

Cakewalk

### PREREQUISITES:

String processing

### PROBLEM:

Given two strings A and B, is it possible to choose some non empty strings s_1 and s_2 such that s_1 is a substring of A, s_2 is a substring of B, and s_1 + s_2 is a palindromic string?

### QUICK EXPLANATION:

If A and B share a common letter, output `Yes`. Otherwise, output `No`.

### EXPLANATION:

This problem can be solved with a few simple observations.

First, what is the simplest palindrome you can think of? Surely, a single letter word is a palindrome. However, such a palindrome cannot be obtained as s_1 + s_2 because s_1 and s_2 must be nonempty (which means the length of s_1 + s_2 is at least two). So the next best thing is a two-letter palindrome, which is just a letter repeated two times. The only way we can form such a palindrome as s_1 + s_2 is when s_1 and s_2 are the same single-letter word. Thus, if A and B share a common letter, then the answer must be `Yes`.

But what if A and B don’t have a common letter? Well, it turns out that the answer is `No`. This is because in any palindrome, the first and last letter must be the same. So suppose we can form the palindrome s_1 + s_2. Since the first letter belongs to s_1 (and thus to A) and the last letter belongs to s_2 (and thus to B), it means that A and B must have a letter in common!

(The arguments above show that A and B sharing a common letter is both **necessary** and **sufficient** for the palindrome s_1 + s_2 to exist.)

Thus, our solution is really simple: The answer is `Yes` if A and B share a common letter, otherwise, the answer is `No`.

In the following, we will describe a few methods on how to compute the answer.

# Finding a common letter: Method 1

The easiest way is to simply find two indices i and j such that A[i] = B[j]. The following C code demonstrates it:

``#include <stdio.h>

char A[1111];
char B[1111];
int main() {
    int cases, cas, i, j, good;
    scanf("%d", &cases);
    for (cas = 1; cas <= cases; cas++) {
        scanf("%s%s", A, B);
        int good = 0;
        for (i = 0; A[i]; i++) {
            for (j = 0; B[j]; j++) {
                if (A[i] == B[j]) {
                    good = 1;
                    break;
                }
            }
            if (good) {
                break;
            }
        }
        puts(good ? "Yes" : "No");
    }
}
``

Each `for` loop iterates through every character of every string. If a common letter is found (`A[i] == B[j]`), then we mark `good` as `1` and break out of both loops (using two `break` statements).

*C/C++ note*: Even though the problem says A and B are only up to 1000 in length, you may need to make the char arrays `A` and `B` at least 1001 in length, because you need to allocate space for the [null terminator](https://en.wikipedia.org/wiki/Null-terminated_string).

# Finding a common letter: Method 2

The code above isn’t actually the fastest way to compute the answer, because it checks all pairs of indices, and there can be up to 1000000 such pairs. To compute the answer faster, we can use the fact that all letters are lowercase letters.

One way would be to check which of the 26 lowercase letters appear in A, and which ones appear in B, and find a letter that appears in both. The following Java code shows one way to do it:

``import java.util.Scanner;
public class Main {
    public static void main (String args[]) {
        Scanner sc = new Scanner(System.in);
        int cases = sc.nextInt();
        boolean aHas[] = new boolean[256];
        boolean bHas[] = new boolean[256];
        for (int cas = 1; cas <= cases; cas++) {
            String a = sc.next();
            String b = sc.next();
            boolean good = false;
            for (char c = 'a'; c <= 'z'; c++) {
                aHas[c] = bHas[c] = false;
            }
            for (int i = 0; i < a.length(); i++) aHas[a.charAt(i)] = true;
            for (int i = 0; i < b.length(); i++) bHas[b.charAt(i)] = true;
            for (char c = 'a'; c <= 'z'; c++) {
                if (aHas[c] && bHas[c]) {
                    good = true;
                    break;
                }
            }
            System.out.println(good ? "Yes" : "No");
        }
    }
}
``

It uses the `aHas` and `bHas` boolean arrays to store which letters appear in which string. The final loop finds a letter “`c`” such that `aHas[c]` and `bHas[c]` are simultaneously `true`.

A fancier way of doing the above would be to use a [bitmask](https://en.wikipedia.org/wiki/Mask_(computing)), or using an integer’s bits as a boolean array. The i th bit will be *on* if and only if the i th lowercase letter is present in the string. Since there are only 26 characters, only 26 bits are needed, so our mask would be a value between 0 and 2^{26} - 1. The following C++ code shows how to do it:

``#include <iostream>
using namespace std;

int main() {
    int cases;
    cin >> cases;
    while (cases--) {
        string a, b;
        cin >> a >> b;
        int a_mask = 0, b_mask = 0;
        for (int i = 0; i < a.size(); i++) a_mask |= 1 << a[i] - 'a';
        for (int i = 0; i < b.size(); i++) b_mask |= 1 << b[i] - 'a';
        cout << (a_mask & b_mask ? "Yes" : "No") << endl;
    }
}
``

It uses the [*bitwise AND*](https://en.wikipedia.org/wiki/Bitwise_operation) operator to check if the two masks have a common *on* bit, which only happens if A and B share a common letter.

Finally, we can use [sets](https://en.wikipedia.org/wiki/Set_(abstract_data_type)) to represent the set of letters of A and B. This way, A and B share a common letter if and only if the *intersection* of their letter sets is nonempty. The following Python code shows one way to do it:

``cases = int(raw_input())
for cas in xrange(cases):
    a_set = set(raw_input().strip())
    b_set = set(raw_input().strip())
    print "Yes" if a_set & b_set else "No"
``

It uses the fact that Python sets use the operator `&` for set intersection. Another bonus with this solution is that it also works even if letters are not restricted to lowercase letters! Also, such solutions can be reduced to just one line (in Python at least):

``for cas in xrange(input()): print "Yes" if set(raw_input()) & set(raw_input()) else "No"
``

### Time Complexity:

O(|A||B|) or O(|A| + |B|)

### AUTHOR’S AND TESTER’S SOLUTIONS:

[setter](https://www.codechef.com/download/Solutions/MARCH16/Setter/STRPALIN.cpp)

[tester](https://www.codechef.com/download/Solutions/MARCH16/Tester/STRPALIN.py)

</details>
