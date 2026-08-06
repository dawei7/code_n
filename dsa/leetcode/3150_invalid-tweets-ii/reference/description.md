## Description

The `Tweets` table stores the identifier and text of every tweet in a social-media application. A tweet is invalid when at least one of three independent limits is exceeded: its content contains more than 140 characters, it contains more than three mentions, or it contains more than three hashtags.

Find every invalid tweet and return its identifier only. A row satisfying several invalidity rules must still appear once. Sort the resulting rows by `tweet_id` in ascending order.
