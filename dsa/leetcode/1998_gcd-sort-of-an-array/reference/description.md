## Description

You are given an integer array `nums`, and you can perform the following operation **any** number of times on `nums`:

- Swap the positions of two elements $\text{nums}[i]$ and $\text{nums}[j]$ if $gcd(\text{nums}[i], \text{nums}[j]) > 1$ where $gcd(\text{nums}[i], \text{nums}[j])$ is the **greatest common divisor** of $\text{nums}[i]$ and $\text{nums}[j]$.

Return `true` *if it is possible to sort *`nums`* in **non-decreasing** order using the above swap method, or *`false`* otherwise.*
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

- **Input:** `nums = [7,21,3]`
- **Output:** `true`
- **Explanation:** We can sort [7,21,3] by performing the following operations:
- Swap 7 and 21 because gcd(7,21) = 7. nums = [<u>**21**</u>,<u>**7**</u>,3]
- Swap 21 and 3 because gcd(21,3) = 3. nums = [<u>**3**</u>,7,<u>**21**</u>]
#### Example 2

- **Input:** `nums = [5,2,6,2]`
- **Output:** `false`
- **Explanation:** It is impossible to sort the array because 5 cannot be swapped with any other element.
#### Example 3

- **Input:** `nums = [10,5,9,3,15]`
- **Output:** `true`
We can sort [10,5,9,3,15] by performing the following operations:
- Swap 10 and 15 because gcd(10,15) = 5. nums = [<u>**15**</u>,5,9,3,<u>**10**</u>]
- Swap 15 and 3 because gcd(15,3) = 3. nums = [<u>**3**</u>,5,9,<u>**15**</u>,10]
- Swap 10 and 15 because gcd(10,15) = 5. nums = [3,5,9,<u>**10**</u>,<u>**15**</u>]
### Constraints

- $1 \le \text{nums.length} \le 3 * 10^{4}$

- $2 \le \text{nums}[i] \le 10^{5}$