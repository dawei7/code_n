# Flight Occupancy and Waitlist Analysis

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2783 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/flight-occupancy-and-waitlist-analysis/) |

## Problem Description

### Goal

The `Flights` table lists each flight and its seat capacity. The `Passengers` table records the flight requested by each passenger. A request is booked when a seat remains; requests beyond that flight's capacity are placed on its waitlist.

For every row in `Flights`, report how many requesting passengers receive seats and how many remain on the waitlist. A flight must still appear when nobody requested it. Passenger rows whose `flight_id` has no matching flight do not correspond to a reportable flight and therefore contribute to no output row.

Return one row per flight in ascending `flight_id` order.

### Function Contract

**Inputs**

- `Flights`: a table with unique integer `flight_id` and integer `capacity`.
- `Passengers`: a table with unique integer `passenger_id` and integer `flight_id`.

Let $F$ be the number of rows in `Flights` and $P$ the number of rows in `Passengers`.

**Return value**

Return a relation with columns `flight_id`, `booked_cnt`, and `waitlist_cnt`. For a flight with capacity $c$ and $r$ matching passenger requests,

$$
\texttt{booked_cnt}=\min(c,r),
\qquad
\texttt{waitlist_cnt}=\max(r-c,0).
$$

Rows must be ordered by `flight_id` ascending.

### Examples

**Example 1**

- Input: flights `(1,2)`, `(2,2)`, and `(3,1)`; passenger requests `[1,1,1,2,2,3,3]`.
- Output: `[[1,2,1], [2,2,0], [3,1,1]]`.
- Explanation: flight 1 has one request beyond capacity, flight 2 is exactly full, and flight 3 has one passenger waiting.

**Example 2**

- Input: flights `(4,3)` and `(9,2)`, with one passenger requesting flight 4 and none requesting flight 9.
- Output: `[[4,1,0], [9,0,0]]`.
- Explanation: the left join keeps the empty flight, whose booked and waitlist counts are both zero.

**Example 3**

- Input: flight `(7,1)`; two valid requests for flight 7 and one request for nonexistent flight 99.
- Output: `[[7,1,1]]`.
- Explanation: only requests joining an existing flight are counted.
