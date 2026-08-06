## Description

For an `event_type`, its average activity is the average `occurrences` among all businesses that have a row for that event. A business without that event does not participate in the event's average.

A business is active when more than one of its event types has an `occurrences` value strictly greater than the corresponding event's average activity. Find every active business and report its identifier. Equality with the average does not qualify, and the result rows may be returned in any order.
