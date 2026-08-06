## Function Contract

**Inputs**

`Events(business_id, event_type, occurrences)` contains $R$ rows at the unique business-event grain. For each event type, compute its average only from rows recorded for that event type.

**Return value**

- Return exactly one column named `business_id`.
- Include a business when it is strictly above the matching event-type average for at least two distinct event types.
- Exclude equality and businesses that qualify for only one event type.
- Result row order is unrestricted.
