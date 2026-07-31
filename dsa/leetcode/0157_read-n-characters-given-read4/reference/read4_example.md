## How read4 works

For a file containing `"abcde"`, the advancing pointer produces this sequence:

```text
Call     Unread file before call     buf4 after call     Return
1        "abcde"                     "abcd"              4
2        "e"                         "e"                 1
3+       end of file                 ""                  0
```

The first call consumes four characters and leaves `e`. The second consumes that final character. Every later call remains at end of file and returns `0`.
