## Examples

**Example 1**

- Input: `slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8`
- Output: `[60,68]`

**Example 2**

- Input: `slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12`
- Output: `[]`

### Additional Examples

**Exact fit**

- Input: `slots1 = [[5,10]], slots2 = [[7,12]], duration = 3`
- Output: `[7,10]`

The common range ends exactly when the three-unit meeting finishes.

**Touching endpoints only**

- Input: `slots1 = [[0,5]], slots2 = [[5,10]], duration = 1`
- Output: `[]`

The two ranges share the timestamp `5`, but their elapsed overlap has length zero and cannot host a positive-duration meeting.
