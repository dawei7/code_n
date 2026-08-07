### 1. Description

Given a string `s` containing an out-of-order English representation of digits `0-9`, return *the digits in **ascending** order*.

### 2. Function Contract

**Inputs**

- `s`: A valid shuffled collection of letters from English digit names.

**Return value**

Return a string containing every reconstructed digit in ascending order, preserving multiplicity.

### 3. Examples

#### Example 1

- **Input:** `s = "owoztneoer"`
- **Output:** `"012"`
#### Example 2

- **Input:** `s = "fviefuro"`
- **Output:** `"45"`

### 4. Constraints

- $1 \le \text{s.length} \le 10^{5}$

- $s[i]$ is one of the characters `["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"]`.

- `s` is **guaranteed** to be valid.