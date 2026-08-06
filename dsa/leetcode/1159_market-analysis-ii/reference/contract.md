## Function Contract

**Input tables**

- `Users`: The marketplace users and each user's favorite brand.
- `Orders`: Item transactions, including their dates, items, buyers, and sellers.
- `Items`: The brand associated with each item.

The report uses `seller_id`, not `buyer_id`, to build each user's sale history. Let $r$ denote the total number of rows across the three input tables.

**Return value**

Return a relation with one row per user and these columns:

- `seller_id`: The user's `user_id`.
- `2nd_item_fav_brand`: `yes` exactly when the user's second chronological sale exists and its item brand equals `favorite_brand`; otherwise, `no`.

Output row order is unrestricted.
