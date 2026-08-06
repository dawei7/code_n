## Description

A promotion targets customers whose order history contains both product `"A"` and product `"B"`, but contains no purchase of product `"C"`. Buying either required product several times has the same qualifying effect as buying it once, while any single `"C"` purchase disqualifies the customer. Orders for other product names do not affect the decision.

Report the `customer_id` and `customer_name` of every qualifying customer so product `"C"` can be recommended to them. Order the result by `customer_id`.
