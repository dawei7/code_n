def solve(positions, healths, directions):
    n = len(positions)
    # Store robots as (position, health, direction, original_index)
    robots = []
    for i in range(n):
        robots.append((positions[i], healths[i], directions[i], i))
    
    # Sort robots by position to simulate movement along the line
    robots.sort()
    
    stack = []
    survivors = []
    
    for pos, health, direction, idx in robots:
        if direction == 'R':
            stack.append([pos, health, direction, idx])
        else:
            # Robot is moving 'L', check for collisions with 'R' robots in stack
            while stack and stack[-1][2] == 'R':
                if stack[-1][1] < health:
                    # 'R' robot is destroyed
                    stack.pop()
                    health -= 1
                elif stack[-1][1] > health:
                    # 'L' robot is destroyed
                    stack[-1][1] -= 1
                    health = 0
                    break
                else:
                    # Both destroyed
                    stack.pop()
                    health = 0
                    break
            
            if health > 0:
                survivors.append((idx, health))
                
    # Add remaining robots in stack to survivors
    while stack:
        r = stack.pop()
        survivors.append((r[3], r[1]))
        
    # Sort by original index to return in correct order
    survivors.sort()
    return [s[1] for s in survivors]
