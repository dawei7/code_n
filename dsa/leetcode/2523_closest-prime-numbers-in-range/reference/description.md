### 1. Description

Given two positive integers `left` and `right`, find the two integers `num1` and `num2` such that:

- $left \le num1 < num2 \le right$.

- Both `num1` and `num2` are prime numbers.

- $num2 - num1$ is the **minimum** amongst all other pairs satisfying the above conditions.

Return the positive integer array $ans = [num1, num2]$. If there are multiple pairs satisfying these conditions, return the one with the **smallest** `num1` value. If no such numbers exist, return `[-1, -1]`*.*

### 2. Function Contract

**Inputs**

- `left`: Input parameter (`int`).
- `right`: Input parameter (`int`).

**Return value**

- Returns `List[int]`.

### 3. Examples

#### Example 1

- **Input:** $left = 10, right = 19$
- **Output:** `[11,13]`
- **Explanation:** The prime numbers between 10 and 19 are 11, 13, 17, and 19.
The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
Since 11 is smaller than 17, we return the first pair.

#### Example 2

- **Input:** $left = 4, right = 6$
- **Output:** `[-1,-1]`
- **Explanation:** There exists only one prime number in the given range, so the conditions cannot be satisfied.

### 4. Constraints

- $1 \le left \le right \le 10^{6}$

.spoilerbutton {display:block; border:dashed; padding: 0px 0px; margin:10px 0px; font-size:150%; font-weight: bold; color:#000000; background-color:cyan; outline:0;
}
.spoiler {overflow:hidden;}
.spoiler > div {-webkit-transition: all 0s ease;-moz-transition: margin 0s ease;-o-transition: all 0s ease;transition: margin 0s ease;}
.spoilerbutton[value="Show Message"] + .spoiler > div {margin-top:-500%;}
.spoilerbutton[value="Hide Message"] + .spoiler {padding:5px;}
