from collections import defaultdict

def solve(creators: list[str], ids: list[str], views: list[int]) -> list[list[str]]:
    # total_views[creator] = sum of views
    total_views = defaultdict(int)
    # best_video[creator] = (max_views, -lexicographically_smallest_id)
    # We store negative ID or handle lexicographical comparison carefully
    best_video = {}
    
    for c, i, v in zip(creators, ids, views):
        total_views[c] += v
        
        if c not in best_video:
            best_video[c] = (v, i)
        else:
            curr_v, curr_id = best_video[c]
            # Update if current video has more views, 
            # or same views but lexicographically smaller ID
            if v > curr_v or (v == curr_v and i < curr_id):
                best_video[c] = (v, i)
                
    max_total = max(total_views.values())
    
    result = []
    for creator, total in total_views.items():
        if total == max_total:
            result.append([creator, best_video[creator][1]])
            
    return result
