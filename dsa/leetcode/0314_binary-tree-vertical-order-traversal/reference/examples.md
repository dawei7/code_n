## Examples

**Example 1**

- Input: `root = [3,9,20,null,null,15,7]`
- Output: `[[9],[3,15],[20],[7]]`

```text
      3
     / \
    9  20
      /  \
     15   7

columns: [9] | [3,15] | [20] | [7]
```

**Example 2**

- Input: `root = [3,9,8,4,0,1,7]`
- Output: `[[4],[9],[3,0,1],[8],[7]]`

```text
        3
       / \
      9   8
     / \ / \
    4  0 1  7

columns: [4] | [9] | [3,0,1] | [8] | [7]
```

**Example 3**

- Input: `root = [1,2,3,4,10,9,11,null,5,null,null,null,null,null,null,null,6]`
- Output: `[[4],[2,5],[1,10,9,6],[3],[11]]`

```text
          1
        /   \
       2     3
      / \   / \
     4  10 9  11
      \
       5
        \
         6

columns: [4] | [2,5] | [1,10,9,6] | [3] | [11]
```
