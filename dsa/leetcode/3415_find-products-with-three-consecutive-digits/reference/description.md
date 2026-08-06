## Description

The `Products` table contains one row per product, identified by `product_id`, together with its `name`. Find every product whose name contains a run of exactly three consecutive digit characters.

The three digits must form a complete run: neither adjacent character, when present, may also be a digit. A name can contain more than one qualifying run, but each returned product appears only once. Return `product_id` and `name`, ordered by `product_id` in ascending order.
