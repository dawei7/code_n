## Examples

**Example 1**

- Input: `operations = ["AllOne","inc","inc","getMaxKey","getMinKey","inc","getMaxKey","getMinKey"], arguments = [[],["hello"],["hello"],[],[],["leet"],[],[]]`
- Output: `[null,null,null,"hello","hello",null,"hello","leet"]`
- Explanation:
  1. Construct an empty `AllOne` instance.
  2. Increment `"hello"`, giving it count $1$.
  3. Increment `"hello"` again, giving it count $2$.
  4. The only stored key, `"hello"`, is the maximum.
  5. It is also the minimum because no other key is present.
  6. Increment `"leet"`, giving it count $1$.
  7. `"hello"` remains the maximum with count $2$.
  8. `"leet"` is the minimum with count $1$.
