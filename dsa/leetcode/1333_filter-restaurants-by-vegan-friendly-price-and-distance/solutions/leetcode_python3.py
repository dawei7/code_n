from typing import List


class Solution:
    def filterRestaurants(
        self,
        restaurants: List[List[int]],
        veganFriendly: int,
        maxPrice: int,
        maxDistance: int,
    ) -> List[int]:
        eligible = []

        for restaurant_id, rating, is_vegan, price, distance in restaurants:
            if veganFriendly and not is_vegan:
                continue
            if price <= maxPrice and distance <= maxDistance:
                eligible.append((rating, restaurant_id))

        eligible.sort(reverse=True)
        return [restaurant_id for _, restaurant_id in eligible]
