## Examples

**Example 1**

- Input: `buckets = 4, minutesToDie = 15, minutesToTest = 15`
- Output: `2`
- **Explanation:** At time `0`, give buckets `1` and `2` to the first pig, and buckets `2` and `3` to the second pig. At time `15`, the four possible observations identify the poison:
  - If only the first pig dies, bucket `1` is poisonous.
  - If only the second pig dies, bucket `3` is poisonous.
  - If both pigs die, bucket `2` is poisonous.
  - If neither pig dies, bucket `4` is poisonous.

**Example 2**

- Input: `buckets = 4, minutesToDie = 15, minutesToTest = 30`
- Output: `2`
- **Explanation:** At time `0`, give bucket `1` to the first pig and bucket `2` to the second. At time `15`, a death immediately identifies the corresponding bucket. If both survive, give bucket `3` to the first pig and bucket `4` to the second. At time `30`, one pig must die, identifying the bucket it drank from.
