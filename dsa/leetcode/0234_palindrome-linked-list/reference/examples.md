## Examples

**Example 1**

```text
1 -> 2 -> 2 -> 1
^              ^
|______________|   matching inward pairs
```

- Input: `head = [1,2,2,1]`
- Output: `true`

**Example 2**

```text
1 -> 2
^    ^            endpoints differ
```

- Input: `head = [1,2]`
- Output: `false`
