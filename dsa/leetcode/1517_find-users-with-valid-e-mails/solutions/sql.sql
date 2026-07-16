SELECT user_id, name, mail
FROM Users
WHERE mail GLOB '[A-Za-z]*@leetcode.com'
  AND substr(mail, 1, length(mail) - 13) NOT GLOB '*[^A-Za-z0-9_.-]*'
ORDER BY user_id;
