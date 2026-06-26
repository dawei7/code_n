from typing import List

def solve(transactions: List[List[int]]) -> int:
    """
    Calculates the minimum initial money required to complete all transactions.
    
    Strategy:
    1. Transactions with cost > cashback are 'losses'. We must perform these
       carefully. To minimize the peak requirement, we sort them by cashback 
       descending.
    2. Transactions with cost <= cashback are 'gains'. We should perform these
       as early as possible to increase our available balance.
    """
    total_loss = 0
    max_needed = 0
    
    # Separate transactions into those that result in a net loss and those that don't
    losses = []
    for cost, cashback in transactions:
        if cost > cashback:
            losses.append((cost, cashback))
            total_loss += (cost - cashback)
        else:
            # For net gains, we want to perform them when we have the least money
            # but still enough to cover the cost.
            max_needed = max(max_needed, cost)
            
    # Sort losses by cashback descending to minimize the peak requirement
    losses.sort(key=lambda x: x[1], reverse=True)
    
    # Calculate the peak requirement for the loss transactions
    current_loss_sum = 0
    for cost, cashback in losses:
        # To perform this transaction, we need:
        # (current_loss_sum + cost)
        max_needed = max(max_needed, current_loss_sum + cost)
        current_loss_sum += (cost - cashback)
        
    return max_needed + total_loss
