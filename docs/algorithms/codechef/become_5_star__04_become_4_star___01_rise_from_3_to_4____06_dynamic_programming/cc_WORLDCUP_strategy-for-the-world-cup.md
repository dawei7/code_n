# Strategy for the World Cup

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | WORLDCUP |
| Difficulty Rating | 2055 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Dynamic Programming |
| Official Link | [WORLDCUP](https://www.codechef.com/practice/course/3to4stars/LP3TO406/problems/WORLDCUP) |

---

## Problem Statement

Captain Dehatti from Bawanian village is making strategy to win the Fake Cricket World Cup organised in his village.

He want his team to score runs only in 4's and 6's because he believes that scoring any runs by running will make them tired.

He also wants that the team does not loose more than  **L** wickets.

He now wonders in how many ways his team can score exactly **R** runs in **B** balls. Ofcourse, he assumes that the opponent bowling is awesome and will not concede any extra runs.

Formally, He wonders how many ways can his team score exactly **R** runs in **B** balls, given that each ball can result in 4, 6, 0 , or W(wicket wont add anything to score). Atmost **L** wicktes are allowed [i.e. Atmost **L** 'W' can be there in B balls ].

**Note:** His batting order is fixed i.e. After each wicket , next player to come is fixed.

### Input

First line contains **T**, the number of test cases.

Each test case contains 3 space separated integers, **R, B and L**

### Output

For each test cases output the number of ways modulo 1e9+7 (i.e. 1000000007)

### Constraints

- **1 ≤ T ≤ 25000**

- **0 ≤ R ≤ 109**

- **1 ≤ B ≤ 300**

- **0 ≤ L ≤ 9**

`
Note that the answer to R = 0 , B = 2 , W =1 is 3  [ 00 , 0W , W0 ]
`

---

## Examples

**Example 1**

**Input**

```text
6
10 2 9
6 2 9
6 1 9
4 1 9
5 1 9
10 3 9
```

**Output**

```text
2
4
1
1
0
12
```

**Explanation**

Explanation for the sample input 1:

All possible ways to face 2 deliveries:

00
04
06
0W
W0
W4
W6
WW
40
44
46
4W
60
64
66
6W

Only possible ways to win the match are 46 and 64. Hence answer is 2.

You need to consider all sample space i.e. 4^B

**Separated test cases**

#### Test case 1

**Input for this case**

```text
10 2 9
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
6 2 9
```

**Output for this case**

```text
4
```



#### Test case 3

**Input for this case**

```text
6 1 9
```

**Output for this case**

```text
1
```



#### Test case 4

**Input for this case**

```text
4 1 9
```

**Output for this case**

```text
1
```



#### Test case 5

**Input for this case**

```text
5 1 9
```

**Output for this case**

```text
0
```



#### Test case 6

**Input for this case**

```text
10 3 9
```

**Output for this case**

```text
12
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/WORLDCUP)

[Contest](http://www.codechef.com/COOK55/problems/WORLDCUP)

**Author**: [Devendra Agarwal](http://www.codechef.com/users/devuy11)

**Tester**: [Anudeep Nekkanti](http://www.codechef.com/users/anudeep2011)

**Editorialist**: [Amit Pandey](http://www.codechef.com/users/amitpandeykgp)

### DIFFICULTY:

Simple.

### PREREQUISITES:

Dynamic programming or combinatorics.

### PROBLEM:

Dehatti wonders how many ways can his team score exactly R runs in B balls with L wickets. Given that each ball can result in 4, 6, 0 runs or a wicket(wicket won’t add anything to score).

### QUICK EXPLANATION:

Suppose we want to make R runs in B balls, having X number of 4's, Y number of 6's, (W \le L) number of wickets and Z number of 0's. So there will be 4X + 6Y = R and X+Y+W+Z = B. If (x,y,z,w) is a particular solution to given equations, then number of ways of arrangement will be \frac {B!}{(x!)(y!)(w!)(z!)}. We have to add all such cases, and the given time limit is sufficient for it.

### EXPLANATION:

First of all, pre-calculate the value of  ^n C_{r} which can be done using a simple dynamic programming approach. You may refer this [link](http://zobayer.blogspot.in/2009/08/calculate-ncr-using-dp.html) for the more details.

As batsman has to make R runs in B balls, if R > 6B, there will not be any way of doing it.

Suppose he makes R runs in B balls, with at-max L wickets. So, we will have the following equations.

4 \times \text{fours} + 6 \times \text{sixes}  = R \\
\text{fours} + \text{sixes} + \text{wickets}(\le L) + \text{zeros} = B

There will be many solutions to the given equations for particular values of R,B and L. We have to consider each one of them.

Let us consider that a particular solution of the equation is fours = X, sixes = Y, wickets = W and zeros = Z, or (X,Y,Z,W) is a solution to the given equations.

So, number of ways of arranging X \hspace{2 mm}4's, Y \hspace{2 mm}6's, W wickets ans Z \hspace{2 mm}0's can be calculated easily using the formula.

\text{Ways} = \frac {B!}{(X!)(Y!)(Z!)(W!)} \\
 ={B \choose X} {B-X \choose Y}  {B-X-Y \choose W}

Values can be used from initially calculated {n \choose r} values . Take care of modulus as well.

T only thing remains is to produce all the triplets (X,Y,Z,W).

We can run a loop on number of sixes varying from 0 to min(B,R/6),number of fours will be fixed i.e.

``Number of fours = (R -6*sixes)/4 if ((R - 6*sixes) % 4 == 0)
``

And we can loop over number of wickets from 0 to L.

``Number of zeros = B-sixes-fours-wickets
``

The following piece of self explanatory code will do all the calculations.

``for(int six=0; six*6 <= r && six <= b; six++) {
		int other = r - six*6;
		if(other % 4 == 0) {
			int four = other/4;
			for(int wicket=0; wicket <= l; wicket++) {
				if(six + four + wicket <= b) {
					long long cur = C[b][six];
					( cur *= C[b-six][four] ) %= 1000000007;
					( cur *= C[b-six-four][wicket] ) %= 1000000007;
					ways += cur;
				}
			}
			ways %= 1000000007;
		}
	}
``

### Solutions:

Setter’s solution can be found [here ](https://codechef_shared.s3.amazonaws.com/download/Solutions/COOK55/Setter/WORLDCUP_logic1.cpp).

Setter’s another solution can be found [here ](https://codechef_shared.s3.amazonaws.com/download/Solutions/COOK55/Setter/WORLDCUP_logic2.cpp).

Tester’s solution can be found [here](http://www.codechef.com/download/Solutions/COOK55/Tester/WORLDCUP.cpp).

</details>
