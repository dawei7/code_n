"""Optimal app-local solution for LeetCode 1333."""


def solve(restaurants, vegan_friendly, max_price, max_distance):
    eligible = []

    for restaurant_id, rating, is_vegan, price, distance in restaurants:
        if vegan_friendly and not is_vegan:
            continue
        if price <= max_price and distance <= max_distance:
            eligible.append((rating, restaurant_id))

    eligible.sort(reverse=True)
    return [restaurant_id for _, restaurant_id in eligible]
