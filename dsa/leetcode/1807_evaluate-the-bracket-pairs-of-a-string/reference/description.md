### 1. Description

You are given a string `s` that contains some bracket pairs, with each pair containing a **non-empty** key.

- For example, in the string `"(name)is(age)yearsold"`, there are **two** bracket pairs that contain the keys `"name"` and `"age"`.

You know the values of a wide range of keys. This is represented by a 2D string array `knowledge` where each $\text{knowledge}[i] = [\text{key}_{i}, \text{value}_{i}]$ indicates that key $\text{key}_{i}$ has a value of $\text{value}_{i}$.

You are tasked to evaluate **all** of the bracket pairs. When you evaluate a bracket pair that contains some key $\text{key}_{i}$, you will:

- Replace $\text{key}_{i}$ and the bracket pair with the key's corresponding $\text{value}_{i}$.

- If you do not know the value of the key, you will replace $\text{key}_{i}$ and the bracket pair with a question mark `"?"` (without the quotation marks).

Each key will appear at most once in your `knowledge`. There will not be any nested brackets in `s`.

Return *the resulting string after evaluating **all** of the bracket pairs.*

### 2. Function Contract

**Inputs**

- `s`: Input parameter (`str`).
- `knowledge`: Input parameter (`List[List[str]]`).

**Return value**

- Returns `str`.

### 3. Examples

#### Example 1

- **Input:** `s = "(name)is(age)yearsold", knowledge = [["name","bob"],["age","two"]]`
- **Output:** `"bobistwoyearsold"`
- **Explanation:** The key "name" has a value of "bob", so replace "(name)" with "bob".
The key "age" has a value of "two", so replace "(age)" with "two".

#### Example 2

- **Input:** `s = "hi(name)", knowledge = [["a","b"]]`
- **Output:** `"hi?"`
- **Explanation:** As you do not know the value of the key "name", replace "(name)" with "?".

#### Example 3

- **Input:** `s = "(a)(a)(a)aaa", knowledge = [["a","yes"]]`
- **Output:** `"yesyesyesaaa"`
- **Explanation:** The same key can appear multiple times.
The key "a" has a value of "yes", so replace all occurrences of "(a)" with "yes".
Notice that the "a"s not in a bracket pair are not evaluated.

### 4. Constraints

- $1 \le \text{s.length} \le 10^{5}$

- $0 \le \text{knowledge.length} \le 10^{5}$

- $\text{knowledge}[i].length = 2$

- $1 \le \text{key}_{i}.length, \text{value}_{i}.length \le 10$

- `s` consists of lowercase English letters and round brackets `'('` and `')'`.

- Every open bracket `'('` in `s` will have a corresponding close bracket `')'`.

- The key in each bracket pair of `s` will be non-empty.

- There will not be any nested bracket pairs in `s`.

- $\text{key}_{i}$ and $\text{value}_{i}$ consist of lowercase English letters.

- Each $\text{key}_{i}$ in `knowledge` is unique.
