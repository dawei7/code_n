## Description

You are given airline tickets in which `tickets[i] = [from_i,to_i]` identifies one flight from its departure airport to its arrival airport. Reconstruct the flights as an ordered itinerary and return its airport sequence.

Every ticket belongs to a traveler whose journey begins at `"JFK"`, so the first airport must be `"JFK"`. Each supplied ticket must be used once and only once, and at least one complete itinerary is guaranteed to exist.

If several complete itineraries are possible, choose the one with the smallest lexical order when each itinerary is read as one string. For instance, `["JFK","LGA"]` is lexically smaller than `["JFK","LGB"]`.
