## Description

You are given two arrays, `instructions` and `values`, both of size `n`.

You need to simulate a process based on the following rules:

- You start at the first instruction at index $i = 0$ with an initial score of 0.

- If $\text{instructions}[i]$ is `"add"`:

		<li>Add $\text{values}[i]$ to your score.

- Move to the next instruction $(i + 1)$.

	</li>
- If $\text{instructions}[i]$ is `"jump"`:

		<li>Move to the instruction at index $(i + \text{values}[i])$ without modifying your score.

	</li>

The process ends when you either:

- Go out of bounds (i.e., $i < 0 or i \ge n$), or

- Attempt to revisit an instruction that has been previously executed. The revisited instruction is not executed.

Return your score at the end of the process.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** instructions = ["jump","add","add","jump","add","jump"], values = [2,1,3,1,-2,-3]

**Output:** 1

**Explanation:**

Simulate the process starting at instruction 0:

- At index 0: Instruction is `"jump"`, move to index $0 + 2 = 2$.

- At index 2: Instruction is `"add"`, add $\text{values}[2] = 3$ to your score and move to index 3. Your score becomes 3.

- At index 3: Instruction is `"jump"`, move to index $3 + 1 = 4$.

- At index 4: Instruction is `"add"`, add $\text{values}[4] = -2$ to your score and move to index 5. Your score becomes 1.

- At index 5: Instruction is `"jump"`, move to index $5 + (-3) = 2$.

- At index 2: Already visited. The process ends.

</div>
#### Example 2

<div class="example-block">
**Input:** instructions = ["jump","add","add"], values = [3,1,1]

**Output:** 0

**Explanation:**

Simulate the process starting at instruction 0:

- At index 0: Instruction is `"jump"`, move to index $0 + 3 = 3$.

- At index 3: Out of bounds. The process ends.

</div>
#### Example 3

<div class="example-block">
**Input:** instructions = ["jump"], values = [0]

**Output:** 0

**Explanation:**

Simulate the process starting at instruction 0:

- At index 0: Instruction is `"jump"`, move to index $0 + 0 = 0$.

- At index 0: Already visited. The process ends.

</div>
### Constraints

- $n = \text{instructions.length} = \text{values.length}$

- $1 \le n \le 10^{5}$

- $\text{instructions}[i]$ is either `"add"` or `"jump"`.

- $-10^{5} \le \text{values}[i] \le 10^{5}$