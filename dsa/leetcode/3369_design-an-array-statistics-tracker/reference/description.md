## Description

Design a `StatisticsTracker` that begins empty and receives positive integers over time. An update may append a number or remove the earliest number that is still present, so removals follow insertion order. At any valid point, the tracker must answer the floored arithmetic mean, the median, and the mode of its current contents.

For a sorted collection of odd size, the median is its middle value. For an even size, use the larger of the two central values. The mode is the most frequent value; if several values share the greatest frequency, return the smallest. Removal and every statistical query are guaranteed to occur only while at least one number is present.
