## Description

You are given an array `words`. Every element is a word made only from lowercase English letters.

You are also given an integer array `weights` containing 26 entries. Entry `weights[i]` is the weight assigned to the $i$th lowercase English letter.

The **weight** of one word is the **sum** of the weights assigned to all of its characters.

For each word, reduce its weight modulo 26 and convert that residue to a lowercase letter in reverse alphabetical order: `0 -> 'z'`, `1 -> 'y'`, through `25 -> 'a'`.

Return the string obtained by concatenating the mapped letters for the words in their original order.
