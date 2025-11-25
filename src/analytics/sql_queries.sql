-- TOP_GENRES_BY_COUNT:
SELECT 
    g.genre_id AS genre_id,
    g.name AS genre_name,
    COUNT(mg.movie_id) AS movie_count
FROM `{{PROJECT}}.{{DATASET}}.movie_genres` mg
JOIN `{{PROJECT}}.{{DATASET}}.genres` g
    ON mg.genre_id = g.genre_id
GROUP BY genre_id, genre_name
ORDER BY movie_count DESC;


-- POPULARITY_BY_GENRE:
SELECT 
    g.name AS genre,
    AVG(m.popularity) AS avg_popularity
FROM `{{PROJECT}}.{{DATASET}}.movies` m
JOIN `{{PROJECT}}.{{DATASET}}.movie_genres` mg
    ON m.movie_id = mg.movie_id
JOIN `{{PROJECT}}.{{DATASET}}.genres` g
    ON mg.genre_id = g.genre_id
GROUP BY genre
ORDER BY avg_popularity DESC;


-- POPULARITY_TREND:
SELECT
    EXTRACT(YEAR FROM m.release_date) AS year,
    AVG(m.popularity) AS avg_popularity
FROM `{{PROJECT}}.{{DATASET}}.movies` m
WHERE m.release_date IS NOT NULL
GROUP BY year
ORDER BY year;


-- ENGAGEMENT_SCORE:
SELECT
    movie_id,
    title,
    vote_count,
    popularity,
    vote_count * popularity AS engagement_score
FROM `{{PROJECT}}.{{DATASET}}.movies`
ORDER BY engagement_score DESC
LIMIT 50;


-- CATALOG_MATURITY:
SELECT
    EXTRACT(YEAR FROM release_date) AS year,
    COUNT(*) AS total_movies
FROM `{{PROJECT}}.{{DATASET}}.movies`
WHERE release_date IS NOT NULL
GROUP BY year
ORDER BY year;


-- GENRE_STABILITY:
SELECT 
    g.name AS genre,
    STDDEV(m.popularity) AS popularity_variance
FROM `{{PROJECT}}.{{DATASET}}.movies` m
JOIN `{{PROJECT}}.{{DATASET}}.movie_genres` mg
    ON m.movie_id = mg.movie_id
JOIN `{{PROJECT}}.{{DATASET}}.genres` g
    ON mg.genre_id = g.genre_id
GROUP BY genre
ORDER BY popularity_variance ASC;
