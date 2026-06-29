# Chef and Strings

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | STRQ |
| Difficulty Rating | 1930 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Segment Trees |
| Official Link | [STRQ](https://www.codechef.com/practice/course/3to4stars/LP3TO407/problems/STRQ) |

---

## Problem Statement

Chef likes strings a lot but moreover he likes good strings. Chef calls a string **str** a good string if **str** starts and ends at different characters. For eg : strings such as **abab** , **baccba** , **abc** are all good strings whereas strings like **aba**, **baab** , **baacaab** are not good at all .

Today, Chef has a special string **P** consisting of lower case letters **"c"** , **"h"** , **"e"** and **"f"** only. Chef wants to make some queries about his string **P**.

Each of chef's query has the following form **a b L R**. For a given query, Chef wants to count the number of good strings which starts at letter **a** and ends at letter **b** such that starting index **Si** and ending index **Ei** of a chosen substring satisfies **L <= Si < Ei <= R**.

**NOTE**

Two substrings **P1** and **P2** are considered to be different if either **S1 != S2** or **E1 != E2** where **S1,E1** and **S2,E2** are the starting and ending index of string **P1** and string **P2** respectively.

Chef is not able to accomplish this task efficiently. Can you help him ?

### Input

First line of the input contains a string **P** denoting the chef's special string. Next line of the input contains a single integer **Q** denoting the number of chef's queries. Next **Q** lines of the input contains **four** space separated parameters where the first **two** parameters are characters denoting **a** and **b** respectively and rest **two** are integers denoting **L** and **R** respectively.

### Output

For each chef's query, print the required answer.

### Constraints

- **1 <= |P| <= 106**

- **1 <= Q <= 106**

- **1 <= L <= R <= |P|**

- **P,a,b** belongs to the set of lower case letters **[c,h,e,f] and a != b**.

- **All test files are strictly according to constraints.**

### Subtasks

-  Subtask #1: **1<=|P|,Q<=104 : 27 pts**

-  Subtask #2: **1<=|P|,Q<=105 : 25 pts**

-  Subtask #3: **1<=|P|,Q<=106 : 48 pts**

### Warning

Large test data set, Prefer to use faster input/output methods .

---

## Examples

**Example 1**

**Input**

```text
checfcheff
5
c h 1 10
c f 1 10
e c 1 10
c f 1 5
c f 6 10
```

**Output**

```text
4
8
2
2
2
```

**Explanation**

- Q1 : good strings are **ch** , **checfch** , **cfch** , **ch**

- Q2 : good strings are **checf** , **checfchef** , **checfcheff** , **cf** , **cfchef** , **cfcheff** , **chef** , **cheff**

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/STRQ)

[Contest](http://www.codechef.com/FEB15/problems/STRQ)

**Author:** [Sunny Aggarwal](http://www.codechef.com/users/ma5termind)

**Tester:** [Pushkar Mishra](http://www.codechef.com/users/pushkarmishra)

**Editorialist:** [Florin Chirica](http://www.codechef.com/users/elfus)

### PROBLEM

You’re given a string containing only letters c h e and f. You have to answer queries asking how many words start in a given letter and end in other letter (necessarily different by first one) considering only positions from the string between two given numbers.

### QUICK EXPLANATION

Let’s calculate ways[A][B][i] = in how many ways can we choose a word with beginning letter A, ending letter B and its ending position up to i. Also, let cnt[A][i] = how many letters A appear in the first i characters. This information is enough to answer queries in O(1): for two characters A and B and two positions i and j, the answer is ways[A][B][j] - ways[A][B][i - 1] - cntA * cntB, where cntA = number of characters equal to A from [1…i - 1] and cntB = number of characters equal to B from [i…j].

### EXPLANATION

**Number of letters is small**

A first thing we should observe is the number of letters available is 4 (c h e and f). This low number of letters will help us to solve the problem with a simple and efficient solution.

The idea with having 4 letters is that we can precalculate *something*, then we can answer all queries in constant time.

Let’s inspect how queries can look like. We start by looking how beginning and ending of a good substring can look like. There are only 12 possibilities.

- (start) c (end) h

- (start) c (end) e

- (start) c (end) f

- (start) h (end) c

- (start) h (end) e

- (start) h (end) f

- (start) e (end) c

- (start) e (end) h

- (start) e (end) f

- (start) f (end) c

- (start) f (end) h

- (start) f (end) e

Since there are only 12 possibilities, we can iterate over them and store something for each configuration. For a configuration, what we computed should be enough to solve *all* queries that correspond to that configuration.

**For a fixed start and end letter**

By now we can assume that our start and end letters are fixed (using the iteration). Let’s denote by A the start letter and by B the end letter.

What we need to do is to answer queries: for a subarray [i…j], how many indices i’, j’ exist, such as array[i’] = A and array[j’] = B, with i <= i’ <= j’ <= j.

The trick here is to solve an easier problem firstly: suppose we only had to count pairs (i’, j’) such as i’ <= j’ <= j (we erased i condition). Now the task can be solved by a simple precalculation.

Let ways[A][B][i] = number of ways to choose i’ <= j’ <= i such as array[i’] = A and array[j’] = B. We have two choices for j’.

Choice #1: Let j’ < i. All pairs (i’, j’) such as j’ < i are already calculated in ways[A][B][i - 1], so we can simply add this number and treat all case.

Choice #2: Let j’ = i. Obviously, for this to happen we’re forced to have array[i] = B. What’s left is to find positions i’ such as array[i’] = A and i’ < i. This is easily done by keeping a partial sum for each letter, something like sum[let][i] = how many times does letter let appear in positions [1…i].

Hence, the answer is in ways[A][B][j].

Now let’s consider full restrictions. In reality we have i <= i’ <= j’ <= j. Let’s see what elements are counted above, but should not be counted.

There are two cases

Case #1: i’ < j’ < i <= j

Case #2: i’ < i < j’ <= j

We have to erase from our result the results for those cases.

Case [#1](https://discuss.codechef.com/tag/1) is simple to calculate, as its answer is simply ways[A][B][i - 1].

Case #2 basically asks us to find a letter A in range [1…i - 1] and a letter B in range [i…j]. Let cntA the number of letters A in range [1…i-1] and cntB the number of letters B in range [i…j]. The answer is simply cntA * cntB. The values of cntA and cntB can be calculated by partial sums.

**Time Complexity**

The computation of ways takes O(n) time (with constant 12). Also, partial sums also take O(n) time. Then, a query is answered in O(1) as stated above.

### AUTHOR’S AND TESTER’S SOLUTIONS:

[Tester’s solution](http://www.codechef.com/download/Solutions/FEB15/Tester1/STRQ.cpp)

[Setter’s solution](http://www.codechef.com/download/Solutions/FEB15/Setter/STRQ.cpp)

</details>
