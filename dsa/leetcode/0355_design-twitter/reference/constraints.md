## Constraints

- $1 \le \texttt{userId},\texttt{followerId},\texttt{followeeId} \le 500$
- $0 \le \texttt{tweetId} \le 10^4$
- Every tweet has a unique ID.
- At most $3 \times 10^4$ total calls are made to `postTweet`, `getNewsFeed`, `follow`, and `unfollow`.
- A user cannot follow themself.
