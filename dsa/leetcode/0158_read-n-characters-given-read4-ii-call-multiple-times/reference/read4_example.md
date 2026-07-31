## How read4 works

For a file containing `"abcde"`, the internal pointer advances as follows:

```text
Call     Unread file before call     buf4 after call     Return
1        "abcde"                     "abcd"              4
2        "e"                         "e"                 1
3+       end of file                 ""                  0
```

Once a call reaches end of file, all subsequent `read4` calls also return `0`.
