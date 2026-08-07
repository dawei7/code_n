## Description

You are given an integer array `nums`.

Start by selecting a starting position `curr` such that $\text{nums}[curr] = 0$, and choose a movement **direction** of either left or right.

After that, you repeat the following process:

- If `curr` is out of the range `[0, n - 1]`, this process ends.

- If $\text{nums}[curr] = 0$, move in the current direction by **incrementing** `curr` if you are moving right, or **decrementing** `curr` if you are moving left.

- Else if $\text{nums}[curr] > 0$:

		<li>Decrement $\text{nums}[curr]$ by 1.

- **Reverse** your movement direction (left becomes right and vice versa).

- Take a step in your new direction.

	</li>

A selection of the initial position `curr` and movement direction is considered **valid** if every element in `nums` becomes 0 by the end of the process.

Return the number of possible **valid** selections.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,0,2,0,3]

**Output:** 2

**Explanation:**

The only possible valid selections are the following:

- Choose $curr = 3$, and a movement direction to the left.

		<li>`[1,0,2,**<u>0</u>**,3] -> [1,0,**<u>2</u>**,0,3] -> [1,0,1,**<u>0</u>**,3] -> [1,0,1,0,**<u>3</u>**] -> [1,0,1,**<u>0</u>**,2] -> [1,0,**<u>1</u>**,0,2] -> [1,0,0,**<u>0</u>**,2] -> [1,0,0,0,**<u>2</u>**] -> [1,0,0,**<u>0</u>**,1] -> [1,0,**<u>0</u>**,0,1] -> [1,**<u>0</u>**,0,0,1] -> [**<u>1</u>**,0,0,0,1] -> [0,**<u>0</u>**,0,0,1] -> [0,0,**<u>0</u>**,0,1] -> [0,0,0,**<u>0</u>**,1] -> [0,0,0,0,**<u>1</u>**] -> [0,0,0,0,0]`.

	</li>
- Choose $curr = 3$, and a movement direction to the right.

		<li>$[1,0,2,**<u>0</u>**,3] -> [1,0,2,0,**<u>3</u>**] -> [1,0,2,**<u>0</u>**,2] -> [1,0,**<u>2</u>**,0,2] -> [1,0,1,**<u>0</u>**,2] -> [1,0,1,0,**<u>2</u>**] -> [1,0,1,**<u>0</u>**,1] -> [1,0,**<u>1</u>**,0,1] -> [1,0,0,**<u>0</u>**,1] -> [1,0,0,0,**<u>1</u>**] -> [1,0,0,**<u>0</u>**,0] -> [1,0,**<u>0</u>**,0,0] -> [1,**<u>0</u>**,0,0,0] -> [**<u>1</u>**,0,0,0,0] -> [0,0,0,0,0].$

	</li>

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [2,3,4,0,4,1,0]

**Output:** 0

**Explanation:**

There are no possible valid selections.

</div>
### Constraints

- $1 \le \text{nums.length} \le 100$

- $0 \le \text{nums}[i] \le 100$

- There is at least one element `i` where $\text{nums}[i] = 0$.