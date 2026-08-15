### 1. Description

Alice and Bob are playing a game. Initially, Alice has a string $word = "a"$.

You are given a **positive** integer `k`. You are also given an integer array `operations`, where $\text{operations}[i]$ represents the **type** of the $$i^{\text{th}}$$ operation.

Now Bob will ask Alice to perform **all** operations in sequence:

- If $\text{operations}[i] = 0$, **append** a copy of `word` to itself.

- If $\text{operations}[i] = 1$, generate a new string by **changing** each character in `word` to its **next** character in the English alphabet, and **append** it to the *original* `word`. For example, performing the operation on `"c"` generates `"cd"` and performing the operation on `"zb"` generates `"zbac"`.

Return the value of the $$k^{\text{th}}$$ character in `word` after performing all the operations.

### 2. Function Contract

**Inputs**

- `k`: Input parameter (`int`).
- `operations`: Input parameter (`List[int]`).

**Return value**

- Returns `str`.

### 3. Note

that the character `'z'` can be changed to `'a'` in the second type of operation.

### 4. Examples

#### Example 1

- **Input:** k = 5, operations = [0,0,0]

- **Output:** "a"

- **Explanation:** Initially, $word = "a"$. Alice performs the three operations as follows:

- Appends `"a"` to `"a"`, `word` becomes `"aa"`.

- Appends `"aa"` to `"aa"`, `word` becomes `"aaaa"`.

- Appends `"aaaa"` to `"aaaa"`, `word` becomes `"aaaaaaaa"`.

#### Example 2

- **Input:** k = 10, operations = [0,1,0,1]

- **Output:** "b"

- **Explanation:** Initially, $word = "a"$. Alice performs the four operations as follows:

- Appends `"a"` to `"a"`, `word` becomes `"aa"`.

- Appends `"bb"` to `"aa"`, `word` becomes `"aabb"`.

- Appends `"aabb"` to `"aabb"`, `word` becomes `"aabbaabb"`.

- Appends `"bbccbbcc"` to `"aabbaabb"`, `word` becomes `"aabbaabbbbccbbcc"`.

### 5. Constraints

- $1 \le k \le 10^{14}$

- $1 \le \text{operations.length} \le 100$

- $\text{operations}[i]$ is either 0 or 1.

- The input is generated such that `word` has **at least** `k` characters after all operations.
