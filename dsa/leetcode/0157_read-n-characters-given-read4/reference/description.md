## Description

Given a `file` and an integer `n`, read `n` characters from `file` and store them in the buffer array `buf`.

The return value is the number of actual characters read.

The `read4` API is defined as such:

```python
def read4(buf4: List[str]) -> int
```

- `@param buf4`: Destination buffer of length 4 where characters read will be stored (`List[str]`).
- `@return`: The number of actual characters read (`int`).

Note that `read4()` has its own file pointer, much like `FILE *fp` in C.

Method `read`:

By using the `read4` API, implement the function `read` that reads `n` characters from `file` and stores them in the buffer array `buf`. Consider that you cannot manipulate `file` directly.

The return value is the number of actual characters read.

Definition of `read`:

```python
def read(buf: List[str], n: int) -> int
```

- `buf`: Destination buffer (`List[str]`).
- `n`: Number of characters to read (`int`).
- `@return`: The number of actual characters read (`int`).

**Note:** `buf` is passed by reference in Python (and similar in C++/Java), meaning modifying `buf` in-place is reflected in the caller.
