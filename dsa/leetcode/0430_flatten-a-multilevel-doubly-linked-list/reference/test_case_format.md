## Test Case Format

**How the multilevel linked list is represented in test cases**

Using Example 1, the separate levels are arranged as follows:

```text
1---2---3---4---5---6---NULL
        |
        7---8---9---10---NULL
            |
            11---12---NULL
```

Serializing each level independently gives:

```text
[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]
```

To combine the levels, insert `null` entries where a position has no child connection to the level below:

```text
[1,    2,    3, 4, 5, 6, null]
             |
[null, null, 7,    8, 9, 10, null]
                   |
[            null, 11, 12, null]
```

Merge those rows and remove trailing `null` entries to obtain
`[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]`.
