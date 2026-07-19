from collections import defaultdict, deque

def solve(initialCurrency, pairs1, rates1, pairs2, rates2):
    def get_max_rates(pairs, rates, start_node):
        graph = defaultdict(list)
        for (u, v), r in zip(pairs, rates):
            graph[u].append((v, r))
            graph[v].append((u, 1.0 / r))
        
        max_rates = {start_node: 1.0}
        queue = deque([start_node])
        
        while queue:
            curr = queue.popleft()
            for neighbor, rate in graph[curr]:
                if max_rates.get(neighbor, 0) < max_rates[curr] * rate:
                    max_rates[neighbor] = max_rates[curr] * rate
                    queue.append(neighbor)
        return max_rates

    # Day 1: Find max conversion from initialCurrency to all others
    day1_rates = get_max_rates(pairs1, rates1, initialCurrency)
    
    # Day 2: For every currency reached in Day 1, find max conversion back to initialCurrency
    max_final_amount = 1.0
    
    # We need to check all currencies reachable from initialCurrency in Day 1
    # and see how much they can convert back to initialCurrency in Day 2
    for intermediate_currency, amount_after_day1 in day1_rates.items():
        day2_rates = get_max_rates(pairs2, rates2, intermediate_currency)
        if initialCurrency in day2_rates:
            final_amount = amount_after_day1 * day2_rates[initialCurrency]
            if final_amount > max_final_amount:
                max_final_amount = final_amount
                
    return float(max_final_amount)
