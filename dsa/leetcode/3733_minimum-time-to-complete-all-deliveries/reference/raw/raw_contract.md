## Function Contract

**Inputs**

- `d`: A length-two array where `d[i]` is drone `i`'s required delivery count.
- `r`: A length-two array where `r[i]` is drone `i`'s recharge interval.

Hours are numbered from `1`. A drone is unavailable at hours divisible by its recharge interval. The drones may recharge simultaneously, but the single-delivery-per-hour rule applies whenever either could deliver.

**Return value**

Return the smallest final hour by which both delivery quotas can be assigned legally.
