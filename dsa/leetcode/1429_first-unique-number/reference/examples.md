## Examples

**Example 1**

- **Input:** `operations = ["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"], arguments = [[[2,3,5]],[],[5],[],[2],[],[3],[]]`
- **Output:** `[null,2,null,2,null,3,null,-1]`

- **Explanation:** The initial queue is `[2,3,5]`, so the first query returns `2`. Adding `5` produces `[2,3,5,5]`, where `2` remains first unique. Adding `2` produces `[2,3,5,5,2]`, making `3` the first unique value. Finally, adding `3` produces `[2,3,5,5,2,3]`; every value is then repeated, so the last query returns `-1`.

**Example 2**

- **Input:** `operations = ["FirstUnique","showFirstUnique","add","add","add","add","add","showFirstUnique"], arguments = [[[7,7,7,7,7,7]],[],[7],[3],[3],[7],[17],[]]`
- **Output:** `[null,-1,null,null,null,null,null,17]`

- **Explanation:** Six initial copies of `7` leave no unique value. Adding another `7` yields `[7,7,7,7,7,7,7]`. The next two additions produce `[7,7,7,7,7,7,7,3]` and then `[7,7,7,7,7,7,7,3,3]`, so `3` also becomes repeated. Adding `7` gives `[7,7,7,7,7,7,7,3,3,7]`. Adding `17` then gives `[7,7,7,7,7,7,7,3,3,7,17]`, whose first and only unique value is `17`.

**Example 3**

- **Input:** `operations = ["FirstUnique","showFirstUnique","add","showFirstUnique"], arguments = [[[809]],[],[809],[]]`
- **Output:** `[null,809,null,-1]`

- **Explanation:** The one-element queue `[809]` initially has `809` as its first unique value. After another `809` is added, the queue is `[809,809]`; it contains no unique value, so the final query returns `-1`.
