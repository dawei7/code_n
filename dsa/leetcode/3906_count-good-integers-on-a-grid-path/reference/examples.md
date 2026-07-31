## Examples

**Example 1**

- Input: `l = 8, r = 10, directions = "DDDRRR"`
- Output: `2`
- Explanation:

  For `x = 8`, the padded grid is:

  | 0 | 0 | 0 | 0 |
  |---:|---:|---:|---:|
  | 0 | 0 | 0 | 0 |
  | 0 | 0 | 0 | 0 |
  | 0 | 0 | 0 | 8 |

  The path is `(0,0) -> (1,0) -> (2,0) -> (3,0) -> (3,1) -> (3,2) -> (3,3)`. It records `[0, 0, 0, 0, 0, 0, 8]`, which is non-decreasing, so `8` is good.

  For `x = 9`, the padded grid is:

  | 0 | 0 | 0 | 0 |
  |---:|---:|---:|---:|
  | 0 | 0 | 0 | 0 |
  | 0 | 0 | 0 | 0 |
  | 0 | 0 | 0 | 9 |

  The same path records `[0, 0, 0, 0, 0, 0, 9]`, so `9` is also good.

  For `x = 10`, the grid is:

  | 0 | 0 | 0 | 0 |
  |---:|---:|---:|---:|
  | 0 | 0 | 0 | 0 |
  | 0 | 0 | 0 | 0 |
  | 0 | 0 | 1 | 0 |

  Its path digits are `[0, 0, 0, 0, 0, 1, 0]`. The final decrease makes `10` not good. Thus only `8` and `9` qualify, for a total of `2`.

**Example 2**

- Input: `l = 123456789, r = 123456790, directions = "DDRRDR"`
- Output: `1`
- Explanation:

  For `x = 123456789`, the grid is:

  | 0 | 0 | 0 | 0 |
  |---:|---:|---:|---:|
  | 0 | 0 | 0 | 1 |
  | 2 | 3 | 4 | 5 |
  | 6 | 7 | 8 | 9 |

  The path `(0,0) -> (1,0) -> (2,0) -> (2,1) -> (2,2) -> (3,2) -> (3,3)` records `[0, 0, 2, 3, 4, 8, 9]`. This sequence is non-decreasing, so `123456789` is good.

  For `x = 123456790`, the grid is:

  | 0 | 0 | 0 | 0 |
  |---:|---:|---:|---:|
  | 0 | 0 | 0 | 1 |
  | 2 | 3 | 4 | 5 |
  | 6 | 7 | 9 | 0 |

  The path digits become `[0, 0, 2, 3, 4, 9, 0]`, which decrease at the end. Therefore only the first integer is good, and the answer is `1`.

**Example 3**

- Input: `l = 1288561398769758, r = 1288561398769758, directions = "RRRDDD"`
- Output: `0`
- Explanation:

  The only candidate produces this grid:

  | 1 | 2 | 8 | 8 |
  |---:|---:|---:|---:|
  | 5 | 6 | 1 | 3 |
  | 9 | 8 | 7 | 6 |
  | 9 | 7 | 5 | 8 |

  The path `(0,0) -> (0,1) -> (0,2) -> (0,3) -> (1,3) -> (2,3) -> (3,3)` records `[1, 2, 8, 8, 3, 6, 8]`. The drop from `8` to `3` violates non-decreasing order, so no integer in the singleton range is good.
