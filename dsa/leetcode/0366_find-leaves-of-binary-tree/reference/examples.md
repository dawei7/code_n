## Examples

**Example 1**

- Input: `root = [1,2,3,4,5]`
- Output: `[[4,5,3],[2],[1]]`
- Explanation: The first round removes leaves `4`, `5`, and `3`; node `2` is then a leaf and is removed in the second round; finally, root `1` is removed. Within a round, other orders such as `[3,5,4]` or `[3,4,5]` are also valid.

The source's three-stage tree illustration is represented here with braces identifying each collected round:

```text
       1                 1                  {1}
      / \               /
     2   {3}     ->    {2}       ->
    / \
  {4} {5}

round 1: {4,5,3}    round 2: {2}    round 3: {1}
```

**Example 2**

- Input: `root = [1]`
- Output: `[[1]]`
