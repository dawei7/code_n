## Description

Given the array `restaurants` where  `restaurants[i] = [id_i, rating_i, veganFriendly_i, price_i, distance_i]`. You have to filter the restaurants using three filters.

The `veganFriendly` filter will be either *true* (meaning you should only include restaurants with `veganFriendly_i` set to true) or *false* (meaning you can include any restaurant). In addition, you have the filters `maxPrice` and `maxDistance` which are the maximum value for price and distance of restaurants you should consider respectively.

Return the array of restaurant ***IDs*** after filtering, ordered by **rating** from highest to lowest. For restaurants with the same rating, order them by ***id*** from highest to lowest. For simplicity `veganFriendly_i` and `veganFriendly` take value *1* when it is *true*, and *0* when it is *false*.
