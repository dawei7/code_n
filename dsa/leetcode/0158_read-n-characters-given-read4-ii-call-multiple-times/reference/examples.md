## Examples

**Example 1**

- **Input:** `file = "abc"`, `queries = [1,2,1]`
- **Output:** `[1,2,0]`
- **Explanation:**
  - `Solution sol;`
  - `sol.read(buf, 1);` // returns 1. `buf` contains `"a"`.
  - `sol.read(buf, 2);` // returns 2. `buf` contains `"bc"`.
  - `sol.read(buf, 1);` // returns 0. `buf` contains `""` (end of file).

**Example 2**

- **Input:** `file = "abc"`, `queries = [4,1]`
- **Output:** `[3,0]`
- **Explanation:**
  - `Solution sol;`
  - `sol.read(buf, 4);` // returns 3. `buf` contains `"abc"`.
  - `sol.read(buf, 1);` // returns 0. `buf` contains `""`.
