def solve(restaurants, vegan_friendly, max_price, max_distance):
    filtered = []
    for rid, rating, vegan, price, distance in restaurants:
        if vegan_friendly and not vegan:
            continue
        if price <= max_price and distance <= max_distance:
            filtered.append((rating, rid))
    filtered.sort(reverse=True)
    return [rid for _, rid in filtered]
