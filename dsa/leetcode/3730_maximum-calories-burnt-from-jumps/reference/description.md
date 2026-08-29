### 1. Description

You are given an integer array `heights` of size `n`, where $\text{heights}[i]$ represents the height of the $i^{\text{th}}$ block in an exercise routine.

You start on the ground (height 0) and **must** jump onto each block **exactly once** in any order.

- The **calories burned** for a jump from a block of height `a` to a block of height `b` is $(a - b)^2$.

- The **calories burned** for the first jump from the ground to the chosen first block $\text{heights}[i]$ is $(0 - \text{heights}[i])^2$.

Return the **maximum** total calories you can burn by selecting an optimal jumping sequence.

### 2. Function Contract

**Inputs**

- `heights`: The positive heights of all blocks that must each be visited exactly once.

The order in the input does not restrict the visiting order. The ground at height `0` supplies only the starting position and is not one of the blocks.

**Return value**

Return the greatest possible sum of squared height differences over the initial ground-to-block jump and the subsequent $n - 1$ block-to-block jumps.

### 3. Note

Once you jump onto the first block, you cannot return to the ground.

### 4. Examples

#### Example 1

- **Input:** heights = [1,7,9]

- **Output:** 181

- **Explanation:** 

The optimal sequence is `[9, 1, 7]`.

- Initial jump from the ground to $\text{heights}[2] = 9$: $(0 - 9)^2 = 81$.

- Next jump to $\text{heights}[0] = 1$: $(9 - 1)^2 = 64$.

- Final jump to $\text{heights}[1] = 7$: $(1 - 7)^2 = 36$.

Total calories burned = $81 + 64 + 36 = 181$.

#### Example 2

- **Input:** heights = [5,2,4]

- **Output:** 38

- **Explanation:** The optimal sequence is `[5, 2, 4]`.

- Initial jump from the ground to $\text{heights}[0] = 5$: $(0 - 5)^2 = 25$.

- Next jump to $\text{heights}[1] = 2$: $(5 - 2)^2 = 9$.

- Final jump to $\text{heights}[2] = 4$: $(2 - 4)^2 = 4$.

Total calories burned = $25 + 9 + 4 = 38$.

#### Example 3

- **Input:** heights = [3,3]

- **Output:** 9

- **Explanation:** The optimal sequence is `[3, 3]`.

- Initial jump from the ground to $\text{heights}[0] = 3$: $(0 - 3)^2 = 9$.

- Next jump to $\text{heights}[1] = 3$: $(3 - 3)^2 = 0$.

Total calories burned = $9 + 0 = 9$.

### 5. Constraints

- $1 \le n = \text{heights.length} \le 10^{5}$

- $1 \le \text{heights}[i] \le 10^{5}$
