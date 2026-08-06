## Description

The `Flights` table lists each flight and its seat capacity. The `Passengers` table records the flight requested by each passenger. A request is booked when a seat remains; requests beyond that flight's capacity are placed on its waitlist.

For every row in `Flights`, report how many requesting passengers receive seats and how many remain on the waitlist. A flight must still appear when nobody requested it. Passenger rows whose `flight_id` has no matching flight do not correspond to a reportable flight and therefore contribute to no output row.

Return one row per flight in ascending `flight_id` order.
