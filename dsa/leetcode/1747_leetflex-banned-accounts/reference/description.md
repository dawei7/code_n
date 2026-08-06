## Description

The `LogInfo` table records account sessions. Each row gives an account identifier, the IP address used, and the session's login and logout timestamps. The combination `(account_id, ip_address, login)` uniquely identifies a row.

An account must be banned when it has two sessions from different IP addresses that overlap in time, meaning the account is simultaneously logged in from both addresses. Return every banned `account_id` once. Sessions from the same address do not create a violation, and nonoverlapping sessions from different addresses are allowed.
