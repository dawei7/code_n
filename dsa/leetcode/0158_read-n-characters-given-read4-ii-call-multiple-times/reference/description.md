## Description

Given a `file` and assume that you can only read the file using a given method `read4`, implement a method `read` to read `n` characters. Your method `read` may be **called multiple times**.

Method `read4`:

The API `read4` reads **four consecutive characters** from `file`, then writes those characters into the buffer array `buf4`.
The return value is the number of actual characters read.
Note that `read4()` has its own file pointer, much like `FILE *fp` in C.

Definition of `read4`:

```python
def read4(buf4: List[str]) -> int
```

`buf4[]` is a destination, not a source. The results from `read4` will be copied to `buf4[]`.

Below is a high-level example of how `read4` works:

- `file = File("abcde")` # File is "abcde", initially file pointer (fp) points to 'a'
- `buf4 = [' '] * 4` # Create buffer with enough space to store characters
- `read4(buf4)` # read4 returns 4. Now buf4 = "abcd", fp points to 'e'
- `read4(buf4)` # read4 returns 1. Now buf4 = "e", fp points to end of file
- `read4(buf4)` # read4 returns 0. Now buf4 = "", fp points to end of file

Method `read`:

By using the `read4` method, implement the method `read` that reads `n` characters from `file` and stores them in the buffer array `buf`. Consider that you cannot manipulate `file` directly.
The return value is the number of actual characters read.

Definition of `read`:

```python
def read(buf: List[str], n: int) -> int
```

`buf[]` is a destination, not a source. You will need to write the results to `buf[]`.

**Note:**

- Consider that you cannot manipulate the file directly. The file is only accessible for `read4` but not for `read`.
- The `read` function may be **called multiple times**.
- Please remember to **RESET** your class variables declared in Solution, as static/class variables are persisted across multiple test cases.
- You may assume the destination buffer array, `buf`, is guaranteed to have enough space for storing `n` characters.
- It is guaranteed that in a given test case the same buffer `buf` is called by `read`.
