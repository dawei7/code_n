def solve(numberOfUsers, events):
    # Sort events by timestamp. If timestamps are equal, process MESSAGE before OFFLINE.
    # We represent MESSAGE as type 0 and OFFLINE as type 1 for sorting.
    processed_events = []
    for e in events:
        type_val = 0 if e[0] == "MESSAGE" else 1
        processed_events.append((int(e[1]), type_val, e[2]))
    
    processed_events.sort()
    
    mentions = [0] * numberOfUsers
    offline_until = [0] * numberOfUsers
    
    for time, type_val, target in processed_events:
        if type_val == 0:  # MESSAGE
            if target == "ALL":
                for i in range(numberOfUsers):
                    mentions[i] += 1
            elif target == "HERE":
                for i in range(numberOfUsers):
                    if offline_until[i] <= time:
                        mentions[i] += 1
            else:
                # Target is "idX"
                user_id = int(target[2:])
                mentions[user_id] += 1
        else:  # OFFLINE
            user_id = int(target)
            # The problem states the user is offline for 60 units of time
            offline_until[user_id] = time + 60
            
    return mentions
