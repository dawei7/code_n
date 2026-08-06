## Description

For every marketplace user, inspect that user's sales in chronological order and identify the second item the user sold. Decide whether the brand of that item is the user's favorite brand.

Report `yes` when the second sold item's brand matches `favorite_brand`. Report `no` when the brands differ or when the user has sold fewer than two items. A seller never sells more than one item on the same day, so date order identifies the second sale without a tie.

Return one row for every user. The result rows may appear in any order.
