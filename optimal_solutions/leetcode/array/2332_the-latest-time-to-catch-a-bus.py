def solve(buses: list[int], passengers: list[int], capacity: int) -> int:
    # Sort both buses and passengers by their respective times.
    # This is crucial for simulating the boarding process correctly.
    buses.sort()
    passengers.sort()

    # Create a set of all passenger arrival times for O(1) average-time lookups.
    # This is used to ensure 'you' do not arrive at the same time as an existing passenger.
    occupied_times = set(passengers)

    p_idx = 0  # Pointer for iterating through the sorted passengers array
    
    # This variable will store the latest possible time 'you' can arrive.
    # Initialize to 0, as arrival times are non-negative.
    latest_you_arrival_time = 0 

    # Iterate through each bus to simulate passenger boarding.
    # The final answer will be determined by the situation of the *last* bus.
    for i in range(len(buses)):
        bus_time = buses[i]
        passengers_boarded_on_this_bus = 0
        # Tracks the latest arrival time of a passenger who successfully boarded *this* bus.
        last_passenger_on_this_bus_arrival_time = -1 

        # Fill the current bus with passengers who arrive on time and within capacity.
        while p_idx < len(passengers) and \
              passengers_boarded_on_this_bus < capacity and \
              passengers[p_idx] <= bus_time:
            
            last_passenger_on_this_bus_arrival_time = passengers[p_idx]
            p_idx += 1
            passengers_boarded_on_this_bus += 1
        
        # We only care about the last bus's situation to determine the latest arrival time for 'you'.
        if i == len(buses) - 1:
            if passengers_boarded_on_this_bus < capacity:
                # Case 1: The last bus is not full.
                # 'You' can potentially arrive at the bus's departure time (`bus_time`).
                # However, 'you' cannot arrive at a time already taken by an existing passenger.
                candidate_time = bus_time
                while candidate_time in occupied_times:
                    candidate_time -= 1
                latest_you_arrival_time = candidate_time
            else:
                # Case 2: The last bus is full.
                # 'You' must arrive strictly before the last passenger who boarded this bus.
                # The latest 'you' can arrive for *this specific bus* is one minute before that last passenger.
                # Again, 'you' cannot arrive at a time already taken by an existing passenger.
                candidate_time = last_passenger_on_this_bus_arrival_time - 1
                while candidate_time in occupied_times:
                    candidate_time -= 1
                latest_you_arrival_time = candidate_time
                
    return latest_you_arrival_time
