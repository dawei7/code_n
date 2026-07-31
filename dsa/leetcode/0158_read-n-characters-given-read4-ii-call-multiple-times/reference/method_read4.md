## Method read4

`read4(buf4)` reads the next four consecutive characters from the file, or all remaining characters when fewer than four are available. It writes them into the destination array `buf4` and advances its own file pointer.

The method returns the number of characters actually written, from `0` through `4`.
