# Making a Meal

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CFMM |
| Difficulty Rating | 1214 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [CFMM](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/CFMM) |

---

## Problem Statement

Today, Chef decided to cook some delicious meals from the ingredients in his kitchen. There are $N$ ingredients, represented by strings $S_1, S_2, \ldots, S_N$. Chef took all the ingredients, put them into a cauldron and mixed them up.

In the cauldron, the letters of the strings representing the ingredients completely mixed, so each letter appears in the cauldron as many times as it appeared in all the strings in total; now, any number of times, Chef can take one letter out of the cauldron (if this letter appears in the cauldron multiple times, it can be taken out that many times) and use it in a meal. A complete meal is the string "codechef". Help Chef find the maximum number of complete meals he can make!

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- $N$ lines follow. For each $i$ ($1 \le i \le N$), the $i$-th of these lines contains a single string $S_i$.

### Output
For each test case, print a single line containing one integer — the maximum number of complete meals Chef can create.

### Constraints
- $1 \le T \le 100$
- $1 \le N \le 100$
- $|S_1| + |S_2| + \ldots + |S_N| \le 1,000$
- each string contains only lowercase English letters

---

## Examples

**Example 1**

**Input**

```text
3
6
cplusplus
oscar
deck
fee
hat
near
5
code
hacker
chef
chaby
dumbofe
5
codechef
chefcode
fehcedoc
cceeohfd
codechef
```

**Output**

```text
1
2
5
```

**Explanation**

**Example case 1:** After mixing, the cauldron contains the letter 'c' 3 times, the letter 'e' 4 times, and each of the letters 'o', 'd', 'h' and 'f' once. Clearly, this is only enough for one "codechef" meal.

**Example case 2:** After mixing, the cauldron contains the letter 'c' 4 times, 'o' 2 times, 'd' 2 times, 'e' 4 times, 'h' 3 times and 'f' 2 times, which is enough to make 2 meals.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**PROBLEM LINK**:

[Practice](https://www.codechef.com/problems/CFMM)

[Contest, div. 1](https://www.codechef.com/COOK105A/problems/CFMM)

[Contest, div. 2](https://www.codechef.com/COOK105B/problems/CFMM)

**Author:** [Kerim Kochekov](http://www.codechef.com/users/mrkerim)

**Tester:** [Teja Vardhan Reddy](http://www.codechef.com/users/teja349)

**Editorialist:** [Oleksandr Kulkov](http://www.codechef.com/users/melfice)

**DIFFICULTY**:

CAKEWALK

**PREREQUISITES**:

None

**PROBLEM**:

You have N strings S_1, \dots, S_N. Their letters are all mixed up. What is the maximum amount of words `codechef` that you may make up of these letters?

**EXPLANATION**:

To complete the word `codechef` you need two letters `e`, two letters `c`, one letter `o`, one letter `h`, one letter `d` and one letter `f`. Let’s denote number of letter x in the set as \#_x. Under such notion the answer can be written as ans=\min(\left\lfloor\#_e/2\right\rfloor,\left\lfloor\#_c/2\right\rfloor, \#_h, \#_f,\#_o,\#_d). Indeed, each of arguments here make an upper bound on number of possible words `codechef` and on the other hand you always may take all needed letters to get exactly ans `codechef`'s. Possible code:

``int N;
cin >> N;
vector<string> S(N);
string s;
for(int i = 0; i < N; i++) {
	cin >> S[i];
	s += S[i];
}
int nc = count(begin(s), end(s), 'c');
int no = count(begin(s), end(s), 'o');
int nd = count(begin(s), end(s), 'd');
int ne = count(begin(s), end(s), 'e');
int nh = count(begin(s), end(s), 'h');
int nf = count(begin(s), end(s), 'f');
cout << min({ne / 2, nc / 2, nh, nf, no, nd}) << endl;
``

**AUTHOR’S AND TESTER’S SOLUTIONS**:

Author’s solution can be found [here](https://ideone.com/MDGVqG).

Tester’s solution can be found [here](https://ideone.com/3vluoV).

Editorialist’s solution can be found [here](https://ideone.com/nOWFV0).

</details>
