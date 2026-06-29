# Genes

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | GENE01 |
| Difficulty Rating | 826 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [GENE01](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/GENE01) |

---

## Problem Statement

People in Chefland have three different eye colors, namely `brown`, `blue`, and `green`. **`green` is the rarest of the eye colors whereas `brown` is most common.**

The eye color of the child of two people is **most likely** to be the **most common** eye color between them.

You are given two characters denoting the eye colors of two people in Chefland. The character `R` denotes `bRown` color, `B` denotes `Blue` color, and `G` denotes `Green` color.

Determine the **most likely** eye color of their child. (Print `R`, `B` or `G` denoting `bRown`, `Blue` or `Green` respectively).

Please see the sample test cases below for explained examples.

---

## Input Format

- The first (and only) line of input contains two space-separated characters, the eye colors of the parents.

---

## Output Format

Print a single character denoting the most likely eye color of the child. (Print `R`, `B` or `G` denoting `brown`, `blue` or `green` respectively).

---

## Constraints

- The input contains two space-separated characters
- Each character in the input is one among {`R`, `B`, `G`}.

---

## Examples

**Example 1**

**Input**

```text
R B
```

**Output**

```text
R
```

**Explanation**

The two people have brown and blue eyes and brown is the most common. Therefore, their child  will most likely have brown eyes.

**Example 2**

**Input**

```text
B B
```

**Output**

```text
B
```

**Explanation**

Both parents have blue eyes, therefore their child will most likely have blue eyes

**Example 3**

**Input**

```text
G B
```

**Output**

```text
B
```

**Explanation**

The parents have green and blue eyes, out of which blue is more common than green, therefore the child will most likely have blue eyes.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

##
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/GENE01)

[Div1](https://www.codechef.com/START20A/problems/GENE01)

[Div2](https://www.codechef.com/START20B/problems/GENE01)

[Div3](https://www.codechef.com/START20C/problems/GENE01)

**Setter:**  [ Srikkanth R](https://www.codechef.com/users/srikkanth_adm)

**Tester:**  [ Aryan Choudhary](https://www.codechef.com/users/aryanc403)

**Editorialist:**  [Ajit Sharma Kasturi](https://www.codechef.com/users/ajit123q)

###
[](#difficulty-2)DIFFICULTY:

CAKEWALK

###
[](#prerequisites-3)PREREQUISITES:

None

###
[](#problem-4)PROBLEM:

We are given two characters denoting the eye colors of two people in Chefland. The character R denotes Brown color, B denotes Blue color, and G denotes Green color. Green is the rarest of colors and Brown is the most common. The eye color of the child of two people is **most likely** to be the **most common** eye color between them. We need to determine the **most likely** eye color of the child of those two people given.

###
[](#explanation-5)EXPLANATION:

-

Actually to the given problem statement, the order of most likely color of the child is R \gt B \gt G.

-

Therefore, if the two colors are R and B, we output R, if the two colors are B and G, we output B, if the two colors are G and R, we output R.

-

In case of both the given characters in the input are same, we obviously output that character itself.

###
[](#time-complexity-6)TIME COMPLEXITY:

O(1) for each testcase.

###
[](#solution-7)SOLUTION:

Editorialist's solution
``#include <iostream>
using namespace std;

int main() {

    char ch1, ch2;
    cin >> ch1 >> ch2;

    if ((ch1 == 'R' && ch2 == 'B') || (ch1 == 'B' && ch2 == 'R')) {
        cout << 'R' << endl;
    }
    else if ((ch1 == 'B' && ch2 == 'G') || (ch1 == 'G' && ch2 == 'B')) {
        cout << 'B' << endl;
    }
    else if ((ch1 == 'G' && ch2 == 'R') || (ch1 == 'R' && ch2 == 'G')) {
        cout << 'R' << endl;
    }
    else {
        cout << ch1 << endl;
    }

	return 0;
}

``

Setter's solution
``a = input()

if a == "R R" or a == "R B" or a == "R G" or a == "B R" or a == "G R":
    print("R")

elif a == "B B" or a == "B G" or a == "G B":
    print("B")

elif a == "G G":
    print("G")

``

Tester's solution
``def main():
    s=input()
    for x in "RBG":
        if x in s:
            print(x)
            break

main()

``

Please comment below if you have any questions, alternate solutions, or suggestions.

</details>
