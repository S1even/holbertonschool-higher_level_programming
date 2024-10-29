-- Import Database Dump
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show.id
LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre.id
ORDER BY tv_shows.title, tv_genres.name
