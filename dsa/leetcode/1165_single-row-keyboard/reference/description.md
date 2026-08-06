## Description

A special keyboard arranges all lowercase English letters in one horizontal row. The string `keyboard` gives that layout from left to right at zero-based positions `0` through `25`, and a finger begins at position `0`.

Typing a character requires moving the finger from its current position $i$ to the character's position $j$. That move costs $\lvert i-j \rvert$ time, and the finger remains at $j$ before the next character is typed.

Given the string `word`, return the total movement time needed to type it with this one finger.
