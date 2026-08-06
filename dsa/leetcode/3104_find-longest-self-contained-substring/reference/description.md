## Description

Given a lowercase string `s`, choose a substring `t` whose characters are isolated from the rest of the string. More precisely, `t` is **self-contained** when it is not the whole string and every character that occurs in `t` occurs nowhere outside `t` in `s`.

The substring must be contiguous. Characters that do not appear in the chosen interval impose no restriction, while every occurrence in `s` of each character used by the interval must lie inside it.

Return the length of the longest self-contained substring. If no proper substring satisfies the condition, return `-1`.
