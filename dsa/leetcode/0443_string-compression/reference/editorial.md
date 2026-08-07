[TOC]

## Solution

---

#### Intuition

First, we make the following observation. Consider a group `t` of consecutive repeating characters. The length of compressed `t` is less than or equal to the length of `t`. For example, `d` tranforms into `d`, `cc` into `c2`, `aaaa` into `a4`, `bbbbbbbbbbbb` into `b12`.

This observation allows processing groups in the array `chars` from left to right.

!?!../Documents/443/slideshow.json:960,540!?!

In the slideshow above, we compress the array $chars = ["c","c","b","a","a","a","a","a","a","a","a","a","a"]$. First, we process the group `cc`, then `b`, and finally `aaaaaaaaaa`.

Unprocessed characters are in white cells.

Processed characters that we may overwrite in the future are in blue cells.

Characters that belong to the answer and will not change are in green cells.

When processing a group, we first find its size `groupLength` and paint its cells blue. Then we append the character of the group to the answer. If `groupLength` is greater than $1$, we also append the string representation of `groupLength` to the answer. Because the problem wants us to form the answer in place, instead of "appending" to the answer we will overwrite the corresponding blue cells by repainting them green.

White cells will eventually become blue and blue ones may become green. Since the compressed group takes up fewer cells than the uncompressed, the white cell cannot immediately become green.

#### Algorithm

1. Declare the variables `i` – the first index of the current group, and `res` – the length of the answer (of the compressed string). Initialize $i = 0$, $res = 0$.
2. While `i` is less than the length of `chars`:
* Find the length of the current group of consecutive repeating characters `groupLength`.
* Add $\text{chars}[i]$ to the answer ($chars[res++] = \text{chars}[i]$).
* If `groupLength > 1`, add the string representation of `groupLength` to the answer and increase `res` accordingly.
* Increase `i` by `groupLength` and proceed to the next group.
3. Return `res`.

#### Implementation

```python
class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        res = 0
        while i < len(chars):
            group_length = 1
            while (i + group_length < len(chars)
                   and chars[i + group_length] == chars[i]):
                group_length += 1
            chars[res] = chars[i]
            res += 1
            if group_length > 1:
                str_repr = str(group_length)
                chars[res:res+len(str_repr)] = list(str_repr)
                res += len(str_repr)
            i += group_length
        return res
```

#### Complexity Analysis

Let $n$ be the length of `chars`.

* Time complexity: $O(n)$.

	All cells are initially white. We will repaint each white cell blue, and we may repaint some blue cells green. Thus each cell will be repainted at most twice. Since there are $n$ cells, the total number of repaintings is $O(n)$.

* Space complexity: $O(1)$.

	We store only a few integer variables and the string representation of `groupLength` which takes up $O(1)$ space.