## Note

- An accepted pair does not have to appear in `FriendRequest`. Count every distinct pair in `RequestAccepted` in the numerator regardless of whether a matching original request is present.
- Repeated requests from the same sender to the same receiver count once. Repeated acceptances for the same requester and accepter also count once.
- When there are no request pairs, report `0.00` rather than a null value or a division error.
