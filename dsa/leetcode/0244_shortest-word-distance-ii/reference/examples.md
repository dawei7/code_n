## Examples

**Example 1:**

- Input: `["WordDistance", "shortest", "shortest"]`, `[[["practice", "makes", "perfect", "coding", "makes"]], ["coding", "practice"], ["makes", "coding"]]`
- Output: `[null, 3, 1]`
- Explanation:
  WordDistance wordDistance = new WordDistance(["practice", "makes", "perfect", "coding", "makes"]);
  wordDistance.shortest("coding", "practice"); // return 3
  wordDistance.shortest("makes", "coding");    // return 1

