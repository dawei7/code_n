SELECT DISTINCT first_session.account_id
FROM LogInfo AS first_session
JOIN LogInfo AS second_session
    ON second_session.account_id = first_session.account_id
    AND second_session.ip_address <> first_session.ip_address
    AND first_session.login <= second_session.logout
    AND second_session.login <= first_session.logout
ORDER BY first_session.account_id ASC;
