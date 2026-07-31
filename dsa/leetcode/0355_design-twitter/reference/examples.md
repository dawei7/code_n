## Examples

**Example 1**

- Input: `operations = ["Twitter","postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed"], arguments = [[],[1,5],[1],[1,2],[2,6],[1],[1,2],[1]]`
- Output: `[null,null,[5],null,null,[6,5],null,[5]]`
- Explanation:
  - Construct a new `Twitter` object.
  - User `1` posts tweet `5`.
  - User `1`'s feed is `[5]`.
  - User `1` follows user `2`.
  - User `2` posts tweet `6`.
  - User `1`'s feed becomes `[6,5]`; tweet `6` precedes tweet `5` because it was posted later.
  - User `1` unfollows user `2`.
  - User `1`'s feed returns to `[5]` because tweets from user `2` are no longer eligible.
