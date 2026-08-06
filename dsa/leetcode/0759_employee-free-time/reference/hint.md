## Hint

Treat every interval endpoint as a sweep-line event. An opening event at position `x` increases the active-interval count, while a closing event decreases it. Process the events from left to right; a stretch with no active interval is common free time.
