## Examples

**Example 1**

- Input: `n = 6`
- Output: `true`
- Explanation: Rotating `6` produces the valid number `9`. Because $9 \ne 6$, the input is confusing.

The source illustration shows the same single-digit transformation:

```mermaid
flowchart LR
    accTitle: Rotating 6 produces 9
    accDescr: A number 6 points to the number 9 under a 180-degree rotation.

    six["6"] -->|rotate 180 degrees| nine["9"]
```

**Example 2**

- Input: `n = 89`
- Output: `true`
- Explanation: The rotated value is the valid number `68`. Since $68 \ne 89$, the input is confusing.

The source illustration depicts this two-digit transformation:

```mermaid
flowchart LR
    accTitle: Rotating 89 produces 68
    accDescr: The number 89 points to the number 68 under a 180-degree rotation because positions reverse and 9 maps to 6 while 8 stays 8.

    original["89"] -->|rotate 180 degrees| rotated["68"]
```

**Example 3**

- Input: `n = 11`
- Output: `false`
- Explanation: Rotating `11` produces the valid number `11`, but its value is unchanged. Therefore, the input is not confusing.

The source illustration emphasizes that the rotation leaves this value unchanged:

```mermaid
flowchart LR
    accTitle: Rotating 11 leaves 11 unchanged
    accDescr: The number 11 points to the same number 11 under a 180-degree rotation, so it is not confusing.

    original["11"] -->|rotate 180 degrees| unchanged["11"]
```
