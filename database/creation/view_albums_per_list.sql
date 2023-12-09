CREATE VIEW dbo.albums_per_playlist 
WITH SCHEMABINDING
AS
SELECT
	playlist_code,
	COUNT_BIG(*) AS total
FROM
	(
		SELECT
			p.code AS playlist_code,
			tp.album_code,
			tp.album_media_number
		FROM
			dbo.playlist p
		LEFT JOIN
			dbo.track_playlist tp
		ON
			p.code = tp.playlist_code
		GROUP BY
			p.code, tp.album_code, tp.album_media_number
	) AS distinct_albums
GROUP BY
	playlist_code