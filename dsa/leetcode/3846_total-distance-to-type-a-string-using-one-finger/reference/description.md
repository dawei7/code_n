### 1. Description

There is a special keyboard where keys are arranged in a rectangular grid as follows.
<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<td style="border: 1px solid black;">q</td>
			<td style="border: 1px solid black;">w</td>
			<td style="border: 1px solid black;">e</td>
			<td style="border: 1px solid black;">r</td>
			<td style="border: 1px solid black;">t</td>
			<td style="border: 1px solid black;">y</td>
			<td style="border: 1px solid black;">u</td>
			<td style="border: 1px solid black;">i</td>
			<td style="border: 1px solid black;">o</td>
			<td style="border: 1px solid black;">p</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">a</td>
			<td style="border: 1px solid black;">s</td>
			<td style="border: 1px solid black;">d</td>
			<td style="border: 1px solid black;">f</td>
			<td style="border: 1px solid black;">g</td>
			<td style="border: 1px solid black;">h</td>
			<td style="border: 1px solid black;">j</td>
			<td style="border: 1px solid black;">k</td>
			<td style="border: 1px solid black;">l</td>
			<td style="border: 1px solid black;"> </td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">z</td>
			<td style="border: 1px solid black;">x</td>
			<td style="border: 1px solid black;">c</td>
			<td style="border: 1px solid black;">v</td>
			<td style="border: 1px solid black;">b</td>
			<td style="border: 1px solid black;">n</td>
			<td style="border: 1px solid black;">m</td>
			<td style="border: 1px solid black;"> </td>
			<td style="border: 1px solid black;"> </td>
			<td style="border: 1px solid black;"> </td>
		</tr>
	</tbody>
</table>

You are given a string `s` that consists of lowercase English letters only. Return an integer denoting the total **distance** to type `s` using only one finger. Your finger starts on the key `'a'`.

The **distance** between two keys at `(r1, c1)` and `(r2, c2)` is $|r1 - r2| + |c1 - c2|$.

### 2. Function Contract

**Inputs**

- `s`: A nonempty string containing only lowercase English letters, to be typed from left to right.

Let $P(x)=(r_x,c_x)$ be the coordinate of letter $x$ in the keyboard table. For $N=\lvert\texttt{s}\rvert$, define $p_0=P(\texttt{a})$ and $p_i=P(\texttt{s[i - 1]})$ for $1\le i\le N$. The distance paid for character $i$ is

$d_i=\lvert p_i.r-p_{i-1}.r\rvert+\lvert p_i.c-p_{i-1}.c\rvert.$

After a character is typed, the finger remains on that character's key and becomes the starting position for the next move.

**Return value**

Return the integer total

$\sum_{i=1}^{N}d_i.$

Typing a character already under the finger contributes zero distance.

### 3. Examples

#### Example 1

- **Input:** s = "hello"

- **Output:** 17

- **Explanation:** 

- Your finger starts at `'a'`, which is at `(1, 0)`.

- Move to `'h'`, which is at `(1, 5)`. The distance is $|1 - 1| + |0 - 5| = 5$.

- Move to `'e'`, which is at `(0, 2)`. The distance is $|1 - 0| + |5 - 2| = 4$.

- Move to `'l'`, which is at `(1, 8)`. The distance is $|0 - 1| + |2 - 8| = 7$.

- Move to `'l'`, which is at `(1, 8)`. The distance is $|1 - 1| + |8 - 8| = 0$.

- Move to `'o'`, which is at `(0, 8)`. The distance is $|1 - 0| + |8 - 8| = 1$.

- Total distance is $5 + 4 + 7 + 0 + 1 = 17$.

#### Example 2

- **Input:** s = "a"

- **Output:** 0

- **Explanation:** 

- Your finger starts at `'a'`, which is at `(1, 0)`.

- Move to `'a'`, which is at `(1, 0)`. The distance is $|1 - 1| + |0 - 0| = 0$.

- Total distance is 0.

### 4. Constraints

- $1 \le \text{s.length} \le 10^{4}$

- `s` consists of lowercase English letters only.
