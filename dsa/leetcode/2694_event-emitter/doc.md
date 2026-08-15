# Event Emitter

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2694 |
| Difficulty | Medium |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| LeetCode | [Open problem](https://leetcode.com/problems/event-emitter/) |

## Problem Description

### Goal

Design an `EventEmitter` class that lets callers subscribe callback functions to named events and later emit those events. Its interface resembles event systems in Node.js and the DOM, but the required behavior is limited to the two methods described here.

`subscribe` associates a callback with an event name. Several callbacks may listen to the same event, and they must run in subscription order whenever that event is emitted. No two subscribed callbacks are referentially identical. Each subscription returns an object whose `unsubscribe` method removes that particular callback and returns `undefined`.

`emit` selects one event name and optionally receives an array of arguments. It calls every callback still subscribed to that event with those arguments and returns their results in subscription order. If the event has no current listeners, it returns an empty array. Listeners registered under other names are unaffected.

### Function Contract

**Inputs**

- `eventName`: The string identifying the event for a subscription or emission.
- `callback`: The unique function registered by `subscribe`.
- `args`: The optional array whose values are forwarded to every callback selected by `emit`.

The test trace contains from $1$ through $10$ actions. Valid actions are construction, subscription, emission, and unsubscription. Every unsubscription refers to a subscription created earlier in the trace.

**Return value**

`subscribe(eventName, callback)` returns an object containing `unsubscribe()`. Calling that method removes the corresponding callback and returns `undefined`. `emit(eventName, args)` returns an array containing one result per active listener, in subscription order, or `[]` when none are active.

### Examples

#### Example 1

- **Input:** Emit `"firstEvent"` before subscribing, then subscribe callbacks returning `5` and `6`, and emit again.
- **Output:** The first emission returns `[]`; the second returns `[5,6]`.

#### Example 2

- **Input:** Subscribe `(...args) => args.join(',')` to `"firstEvent"`, then emit with `[1,2,3]` and later `[3,4,6]`.
- **Output:** `["1,2,3"]` and `["3,4,6"]`.

#### Example 3

- **Input:** Subscribe a callback to `"firstEvent"`, emit once, unsubscribe it, and emit again.
- **Output:** The first emission contains the callback result; the second returns `[]`.

#### Example 4

- **Input:** Subscribe `x => x + 1` and then `x => x + 2`, unsubscribe the first subscription, and emit with `[5]`.
- **Output:** `[7]`.
