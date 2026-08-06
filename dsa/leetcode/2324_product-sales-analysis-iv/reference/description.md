## Description

The `Sales` table records product purchases, including the buyer and quantity. The `Product` table supplies the unit price of every referenced product. A user may have multiple sale rows for the same product, so that user's total spending on the product is the sum of `quantity * price` across all such rows.

For every user, report the product or products on which that user spent the greatest total amount. If multiple products tie for a user's maximum, include every tied product. Return only the user and product identifiers; the result rows may appear in any order.
