## Description

`Friendship` records pairs of users who are friends, while `Likes` records the pages liked by each user. A friendship with user `1` may place that user in either friendship column, because both identifiers participate in the same relation.

Recommend pages to user `1` from the pages liked by any of that user's friends. A page must be excluded when user `1` already likes it, even if one or several friends also like it.

Return every eligible page exactly once. The result rows may appear in any order.
