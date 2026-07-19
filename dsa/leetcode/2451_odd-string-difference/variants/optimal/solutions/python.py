def solve(words: list[str]) -> str:
    def get_diff(s: str) -> tuple:
        diffs = []
        for i in range(len(s) - 1):
            diffs.append(ord(s[i+1]) - ord(s[i]))
        return tuple(diffs)

    # Map difference patterns to the list of words that share that pattern
    diff_map = {}
    
    for word in words:
        pattern = get_diff(word)
        if pattern not in diff_map:
            diff_map[pattern] = []
        diff_map[pattern].append(word)
        
    # The odd string is the one whose pattern appears only once
    for pattern in diff_map:
        if len(diff_map[pattern]) == 1:
            return diff_map[pattern][0]
            
    return ""
