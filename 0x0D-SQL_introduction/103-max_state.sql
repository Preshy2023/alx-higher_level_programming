-- Displays the max temperature of each state, ordered by state name.
SELECT `state` , MAX9`value`) AS `max_temp`
FROM `temperature`
GROUP BY `state`
ORDER BY `state`
