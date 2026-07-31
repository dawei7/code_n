## Note

- The file is accessible through `read4` only; `read` cannot manipulate it directly.
- The same reader's `read` method may be called multiple times.
- Reset instance or class state between separate test cases because static or class variables may otherwise persist.
- The destination `buf` always has enough capacity for `n` characters.
- Within one test case, every call uses the same `buf` object.
