## Description

Given a `file` and assume that you can only read the file using a given method `read4`, implement a method `read` to read `n` characters. Your method `read` may be **called multiple times**.

**Method read4:**

The API `read4` reads **four consecutive characters** from `file`, then writes those characters into the buffer array `buf4`.

The return value is the number of actual characters read.

Note that `read4()` has its own file pointer, much like `FILE *fp` in C.

**Definition of read4:**

    Parameter:  char[] buf4
    Returns:    int

`buf4[]` is a destination, not a source. The results from `read4` will be copied to `buf4[]`.

Below is a high-level example of how `read4` works:

