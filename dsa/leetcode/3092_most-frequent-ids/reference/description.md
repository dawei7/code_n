## Description

The problem involves tracking the frequency of IDs in a collection that changes over time. You have two integer arrays, `nums` and `freq`, of equal length `n`. Each element in `nums` represents an ID, and the corresponding element in `freq` indicates how many times that ID should be added to or removed from the collection at each step.

- **Addition of IDs:** If $\text{freq}[i]$ is positive, it means $\text{freq}[i]$ IDs with the value $\text{nums}[i]$ are added to the collection at step `i`.

- **Removal of IDs:** If $\text{freq}[i]$ is negative, it means $-\text{freq}[i]$ IDs with the value $\text{nums}[i]$ are removed from the collection at step `i`.

Return an array `ans` of length `n`, where $\text{ans}[i]$ represents the **count** of the *most frequent ID* in the collection after the $$i^{\text{th}}$$ step. If the collection is empty at any step, $\text{ans}[i]$ should be 0 for that step.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [2,3,2,1], freq = [3,2,-3,1]

**Output:** [3,3,2,2]

**Explanation:**

After step 0, we have 3 IDs with the value of 2. So $\text{ans}[0] = 3$.

After step 1, we have 3 IDs with the value of 2 and 2 IDs with the value of 3. So $\text{ans}[1] = 3$.

After step 2, we have 2 IDs with the value of 3. So $\text{ans}[2] = 2$.

After step 3, we have 2 IDs with the value of 3 and 1 ID with the value of 1. So $\text{ans}[3] = 2$.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [5,5,3], freq = [2,-2,1]

**Output:** [2,0,1]

**Explanation:**

After step 0, we have 2 IDs with the value of 5. So $\text{ans}[0] = 2$.

After step 1, there are no IDs. So $\text{ans}[1] = 0$.

After step 2, we have 1 ID with the value of 3. So $\text{ans}[2] = 1$.

</div>
### Constraints

- $1 \le \text{nums.length} = \text{freq.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{5}$

- $-10^{5} \le \text{freq}[i] \le 10^{5}$

- $\text{freq}[i] \neq 0$

- The input is generated<!-- notionvc: a136b55a-f319-4fa6-9247-11be9f3b1db8 --> such that the occurrences of an ID will not be negative in any step.