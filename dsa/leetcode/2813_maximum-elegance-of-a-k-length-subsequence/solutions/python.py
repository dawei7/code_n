def solve(items: list[list[int]], k: int) -> int:
    # Sort items by profit descending
    items.sort(key=lambda x: x[0], reverse=True)
    
    total_profit = 0
    seen_categories = set()
    duplicates = []
    
    # Initial selection of top k items
    for i in range(k):
        profit, category = items[i]
        total_profit += profit
        if category in seen_categories:
            duplicates.append(profit)
        else:
            seen_categories.add(category)
            
    max_elegance = total_profit + len(seen_categories) ** 2
    
    # Try to swap duplicates for new categories from the remaining items
    for i in range(k, len(items)):
        profit, category = items[i]
        # Only swap if we have a duplicate to remove and the new item is a new category
        if category not in seen_categories and duplicates:
            seen_categories.add(category)
            # Remove the smallest profit duplicate
            total_profit -= duplicates.pop()
            total_profit += profit
            max_elegance = max(max_elegance, total_profit + len(seen_categories) ** 2)
            
    return max_elegance
