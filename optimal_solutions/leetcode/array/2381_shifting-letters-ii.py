def solve(s: str, shifts: list[list[int]]) -> str:
    n = len(s)
    # diff array to store the net shift at each index
    # size n + 1 to handle the end boundary easily
    diff = [0] * (n + 1)
    
    for start, end, direction in shifts:
        val = 1 if direction == 1 else -1
        diff[start] += val
        if end + 1 < n:
            diff[end + 1] -= val
            
    # Compute prefix sums to get the actual shift for each character
    current_shift = 0
    result = []
    for i in range(n):
        current_shift += diff[i]
        
        # Calculate the new character
        # ord(s[i]) - ord('a') gives 0-25 index
        # Apply shift and use modulo 26 to handle wrapping
        original_pos = ord(s[i]) - ord('a')
        new_pos = (original_pos + current_shift) % 26
        result.append(chr(ord('a') + new_pos))
        
    return "".join(result)
