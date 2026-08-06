## Description

The `Products` table identifies every product, its category, and its price. The `Discounts` table optionally assigns a percentage discount from 0 through 100 to a category. Each product ID is unique, and each discounted category appears at most once.

Report every product with its price after applying the matching category discount. A product whose category has no row in `Discounts` keeps its original price. Include `product_id`, the calculated `final_price`, and `category`, and order the result by `product_id` in ascending order.
