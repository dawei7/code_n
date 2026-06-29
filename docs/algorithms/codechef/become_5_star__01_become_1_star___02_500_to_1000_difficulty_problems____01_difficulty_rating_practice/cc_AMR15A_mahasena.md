# Mahasena

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | AMR15A |
| Difficulty Rating | 533 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [AMR15A](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/AMR15A) |

---

## Problem Statement

Kattapa, as you all know was one of the greatest warriors of his time. The kingdom of Maahishmati had never lost a battle under him (as army-chief), and the reason for that was their really powerful army, also called as **Mahasena**.

Kattapa was known to be a very superstitious person. He believed that a soldier is "lucky" if the soldier is holding an **even number** of weapons, and "unlucky" otherwise. He considered the army as "READY FOR BATTLE" if the count of "lucky" soldiers is strictly greater than the count of "unlucky" soldiers, and "NOT READY" otherwise.

Given the number of weapons each soldier is holding, your task is to determine whether the army formed by all these soldiers is "READY FOR BATTLE" or "NOT READY".

**Note**: You can find the definition of an even number [here](https://simple.wikipedia.org/wiki/Even_number).

---

## Input Format

The first line of input consists of a single integer **N** denoting the number of soldiers. The second line of input consists of **N** space separated integers **A1**, **A2**, ..., **AN**, where **Ai** denotes the number of weapons that the **i**th soldier is holding.

---

## Output Format

Generate one line output saying "READY FOR BATTLE", if the army satisfies the conditions that Kattapa requires or "NOT READY" otherwise (quotes for clarity).

---

## Constraints

- **1** ≤ **N** ≤ **100**

- **1** ≤ **Ai** ≤ **100**

---

## Examples

**Example 1**

**Input**

```text
1
1
```

**Output**

```text
NOT READY
```

**Explanation**

- **Example 1**: For the first example, **N = 1** and the array **A = [1]**. There is only 1 soldier and he is holding 1 weapon, which is odd. The number of soldiers holding an even number of weapons = 0, and number of soldiers holding an odd number of weapons = 1. Hence, the answer is "NOT READY" since the number of soldiers holding an even number of weapons is not greater than the number of soldiers holding an odd number of weapons.

**Example 2**

**Input**

```text
1
2
```

**Output**

```text
READY FOR BATTLE
```

**Explanation**

**Example 2**: For the second example, **N = 1** and the array **A = [2]**. There is only 1 soldier and he is holding 2 weapons, which is even. The number of soldiers holding an even number of weapons = 1, and number of soldiers holding an odd number of weapons = 0. Hence, the answer is "READY FOR BATTLE" since the number of soldiers holding an even number of weapons is greater than the number of soldiers holding an odd number of weapons.

**Example 3**

**Input**

```text
4
11 12 13 14
```

**Output**

```text
NOT READY
```

**Explanation**

**Example 3**: For the third example, **N = 4** and the array **A = [11, 12, 13, 14]**. The 1st soldier is holding 11 weapons (which is odd), the 2nd soldier is holding 12 weapons (which is even), the 3rd soldier is holding 13 weapons (which is odd), and the 4th soldier is holding 14 weapons (which is even). The number of soldiers holding an even number of weapons = 2, and number of soldiers holding an odd number of weapons = 2. Notice that we have an **equal** number of people holding even number of weapons and odd number of weapons. The answer here is "NOT READY" since the number of soldiers holding an even number of weapons is **not strictly greater than** the number of soldiers holding an odd number of weapons.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK

[Practice](https://www.codechef.com/problems/AMR15A)

[Contest](https://www.codechef.com/ACMAMR15/problems/AMR15A)

### Panel Members

**Problem Setter:** [Suhash](https://www.codechef.com/users/suh_ash2008)

**Problem Tester:**

**Editorialist:** [Sunny Aggarwal](https://www.codechef.com/users/ma5termind)

**Contest Admin:**

**Russian Translator:**

**Mandarin Translator:**

**Vietnamese Translator:**

**Language Verifier:**

### DIFFICULTY:

Cakewalk

### PREREQUISITES:

Simple, Input processing, Basic Maths.

### PROBLEM:

Given a list of integers. We are asked to report whether the number of even integers is more than the number of odd integers or not.

### EXPLANATION

This is a simple problem and can be solved by simply counting the number of even/odd integers.

**Basic C++ Code:**

`
int main() {
	int n; cin >> n;
	int cnt = 0;
	for(int i=1; i<=n; i++) {
		int x; cin >> x;
		if( x % 2 == 0 ) cnt ++;
	}
	puts( cnt > n - cnt ? "READY FOR BATTLE" : "NOT READY" );
	return 0;
}
`

**Basic Java Code:**

`
public static void main (String[] args) throws java.lang.Exception
{
	Scanner sc = new Scanner(System.in);
	int n = sc.nextInt();
	int cnt = 0;
	for(int i=1; i<=n; i++) {
		int x;
		x = sc.nextInt();
		if( x % 2 == 0 ) {
			cnt ++;
		}
	}
	System.out.println( cnt > n - cnt ? "READY FOR BATTLE" : "NOT READY" );
}
`

**Basic Python Code:**

`
import sys
f = sys.stdin
n = int(f.readline())
cnt = 0
A = [int(x) for x in f.readline().split()]
for i in range(0, n):
	if A[i] % 2 == 0:
		cnt += 1
if cnt > n - cnt:
	print "READY FOR BATTLE"
else:
	print "NOT READY"
`

### TIME COMPLEXITY

O(N)

### SPACE COMPLEXITY

O(1)

### SIMILAR PROBLEMS

[ Distinct Codes ](https://www.codechef.com/problems/DISTCODE)

[Black And White Cells](https://www.codechef.com/LTIME30/problems/BWCELL)

[ Chef And Easy Problem ](https://www.codechef.com/LTIME16/problems/CHEFA/)

</details>
