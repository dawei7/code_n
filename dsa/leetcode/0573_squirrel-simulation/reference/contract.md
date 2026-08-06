## Function Contract

**Inputs**

- `height`: the garden's row count.
- `width`: the garden's column count.
- `tree`: the tree coordinate `[row, column]`.
- `squirrel`: the squirrel's initial coordinate `[row, column]`.
- `nuts`: the list of nut coordinates, with `nuts[i]` identifying the $i$th nut.

Let $n$ be the number of entries in `nuts`. Because movement is axis-aligned, the distance between coordinates $(r_1,c_1)$ and $(r_2,c_2)$ is $lvert r_1-r_2\rvert + \lvert c_1-c_2\rvert$.

**Return value**

Return the smallest total move count for a route that carries every nut to `tree`, never carrying more than one nut at once.
