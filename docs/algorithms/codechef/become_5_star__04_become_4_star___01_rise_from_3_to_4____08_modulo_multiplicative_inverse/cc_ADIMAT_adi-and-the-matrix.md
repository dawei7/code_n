# Adi and the Matrix

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ADIMAT |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Modulo Multiplicative Inverse |
| Official Link | [ADIMAT](https://www.codechef.com/practice/course/3to4stars/LP3TO408/problems/ADIMAT) |

---

## Problem Statement

Adi likes binary matrices, i.e. matrices containing only elements $0$ and $1$. Adi is wondering how many binary matrices with $N$ rows and $M$ columns there are. Everyone knows the answer to this question - it is just $2^{N \cdot M}$. What most people do not know, however, is that Adi considers two matrices identical if and only if one of them can be turned into the other by first suitably permuting the $N$ rows of this matrix and then suitably permuting the $M$ columns of the resulting matrix.

The problem is much harder now and Adi does not know how to solve it anymore! Help Adi by finding the number of binary $N \times M$ matrices which are distinct according to his definition. Since the answer may be quite large, compute it modulo $10^9 + 7$.

### Input
The first and only line of the input contains two space-separated integers $N$ and $M$.

### Output
Print a single line containing one integer — the number of matrices modulo $10^9 + 7$.

### Constraints
- $1 \le N, M, N \cdot M \le 550$

### Example Input
```
1 5
```

### Example Output
```
6
```

### Explanation
According to Adi's definition, there are $6$ different binary matrices. This is because the number of $1$-s uniquely identifies a $1 \times 5$ matrix and the number of $1$-s can take any value between $0$ and $5$ inclusive.

### Example Input
```
10 10
```

### Example Output
```
508361223
```
