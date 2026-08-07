## Examples

**Example 1**

- Input: `file = "abc"`, `queries = [1,2,1]`
- Output: `[1,2,0]`
- Explanation:
  Solution sol;
  sol.read(buf, 1); // After calling your read method, buf should contain "a". We read a total of 1 character from the file, so return 1.
  sol.read(buf, 2); // Now buf should contain "bc". We read a total of 2 characters from the file, so return 2.
  sol.read(buf, 1); // We have reached the end of file, no more characters can be read. So return 0.
  Assume buf is allocated and guaranteed to have enough space for storing all characters from the file.

**Example 2**

- Input: `file = "abc"`, `queries = [4,1]`
- Output: `[3,0]`
- Explanation:
  Solution sol;
  sol.read(buf, 4); // After calling your read method, buf should contain "abc". We read a total of 3 characters from the file, so return 3.
  sol.read(buf, 1); // We have reached the end of file, no more characters can be read. So return 0.
