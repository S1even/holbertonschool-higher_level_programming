-- Import Database Dump
SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_show.id = tv_show_genres.show.id
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_show.title
