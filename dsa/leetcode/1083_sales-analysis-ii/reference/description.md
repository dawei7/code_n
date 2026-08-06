## Description

Report the buyers who have purchased a product named `S8` but have never purchased a product named `iPhone`. The two names refer to products represented in the `Product` table, so a sale's product name is determined through its `product_id` relationship.

A buyer needs at least one `S8` purchase to qualify. Any `iPhone` purchase disqualifies that buyer, while purchases of products with other names have no effect. Return each qualifying buyer once, in any order.
