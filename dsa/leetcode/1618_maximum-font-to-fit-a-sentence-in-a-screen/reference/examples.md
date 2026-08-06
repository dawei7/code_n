## Examples

**Example 1**

- **Input:** `text = "helloworld", w = 80, h = 20, fonts = [6,8,10,12,14,16,18,24,36]`
- **Output:** `6`
- **Explanation:** Font 6 fits within width 80 and height 20. Font 8 exceeds width/height limits.

**Example 2**

- **Input:** `text = "leetcode", w = 1000, h = 50, fonts = [1,2,4]`
- **Output:** `4`
- **Explanation:** Font 4 fits comfortably within width 1000 and height 50.

**Example 3**

- **Input:** `text = "easyquestion", w = 100, h = 100, fonts = [10,15,20,25]`
- **Output:** `-1`
- **Explanation:** Even the smallest font (10) exceeds the screen dimensions.
