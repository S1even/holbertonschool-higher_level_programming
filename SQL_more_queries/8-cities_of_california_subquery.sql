-- Lists all cities
SELECT id, name
FROM CITIES
WHERE state_id = (SELECT id FROM states WHERE name = 'California');
