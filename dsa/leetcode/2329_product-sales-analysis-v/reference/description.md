## Description

The `Sales` table records which product a user purchased and in what quantity. The `Product` table gives the unit price for each referenced product. The money represented by one sale row is its quantity multiplied by that product's price.

Compute each user's total spending across all of their sale rows. Return one row per user with the columns `user_id` and `spending`. Sort users by spending from greatest to least; when two users have equal totals, place the smaller `user_id` first.
