## Description

A binary watch uses four LEDs for the hour, from `0` through `11`, and six LEDs for the minutes, from `0` through `59`. Each LED represents one binary bit, with the least significant bit on the right.

The source watch image shows the value `4:51`; its lit positions can be represented as follows:

```text
hours:    8  4  2  1       lit: 4          -> 4
minutes: 32 16  8  4  2  1 lit: 32+16+2+1 -> 51
display: 4:51
```

Given `turnedOn`, the total number of lit LEDs, return every time the watch could display, in any order. Ignore whether the time is AM or PM.

Hours must not have a leading zero: use `"1:00"`, not `"01:00"`. Minutes always use exactly two digits and may begin with zero: use `"10:02"`, not `"10:2"`.
