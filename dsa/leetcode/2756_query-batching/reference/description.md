## Description

Implement a JavaScript class `QueryBatcher` that groups closely timed single-key requests into calls to a supplied asynchronous bulk query.

The constructor receives `queryMultiple`, an async function that accepts an array of string keys and fulfills with an equally long value array whose indices correspond to those keys, plus a throttle interval `t` in milliseconds. The bulk query is guaranteed not to reject.

Calling `getValue(key)` must return a promise for that key's individual string value. The first request after an idle interval triggers `queryMultiple` immediately with its key. Any requests arriving before another bulk query may legally start are queued together. Exactly when $t$ milliseconds have elapsed since the previous bulk-query start, dispatch all queued keys in one batch and resolve each waiting promise with its corresponding result.

Throttle query start times, not completion times. A slow earlier bulk query may remain in flight while a later legal batch starts. Every input key is unique. The throttle satisfies $0 \le t \le 1000$, and a schedule contains at most ten calls.
