## Description

Given an array `functions` whose elements are zero-argument functions returning promises, invoke every function so that their asynchronous work runs in parallel. Return one promise that waits until every produced promise has settled, whether by fulfillment or rejection.

For a fulfilled promise, place an object of the form `{ status: "fulfilled", value: resolvedValue }` in the output. For a rejected promise, place `{ status: "rejected", reason: rejectionReason }` instead. The returned promise itself resolves with the complete array; an individual rejection must be captured as a result record rather than rejecting the aggregate.

Each output object must occupy the index of its originating function even when the promises settle in a different order. Implement this behavior without calling `Promise.allSettled()`.
