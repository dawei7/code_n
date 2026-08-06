## Description

You are given a string `s` of lowercase English letters and a 2D integer array `shifts` where `shifts[i] = [start_i, end_i, direction_i]`. For every `i`, **shift** the characters in `s` from the index `start_i` to the index `end_i` (**inclusive**) forward if `direction_i = 1`, or shift the characters backward if `direction_i = 0`.

Shifting a character **forward** means replacing it with the **next** letter in the alphabet (wrapping around so that `'z'` becomes `'a'`). Similarly, shifting a character **backward** means replacing it with the **previous** letter in the alphabet (wrapping around so that `'a'` becomes `'z'`).

Return *the final string after all such shifts to *`s`* are applied*.
