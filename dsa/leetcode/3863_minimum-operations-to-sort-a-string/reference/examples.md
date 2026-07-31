## Examples

**Example 1**

- Input: `s = "dog"`
- Output: `1`
- Explanation:
  1. Sort the substring `"og"` into `"go"`.
  2. The resulting string is `"dgo"`, which is in ascending order, so one
     operation is sufficient.

**Example 2**

- Input: `s = "card"`
- Output: `2`
- Explanation:
  1. Sort `"car"` into `"acr"`, changing the full string to `"acrd"`.
  2. Then sort `"rd"` into `"dr"`. The string becomes `"acdr"`, which is in
     ascending order, so the answer is `2`.

**Example 3**

- Input: `s = "gf"`
- Output: `-1`
- Explanation: Neither permitted proper substring can change this two-letter
  string, so it cannot be sorted under the operation restriction. The result
  is therefore `-1`.
