CREATE FUNCTION GetAlbumsComposedBy(@songwriter_name NVARCHAR(100))
RETURNS TABLE
AS
RETURN
(
	SELECT
		DISTINCT a.*
	FROM
		album a
	LEFT JOIN	
		track t
	ON
		a.code = t.album_code AND a.media_number = t.album_media_number
	LEFT JOIN
		track_songwriter ts
	ON
		t.album_code = ts.album_code AND t.album_media_number = ts.album_media_number AND t.number = ts.track_number
	LEFT JOIN
		songwriter s
	ON
		ts.songwriter_code = s.code
	WHERE
		s.name LIKE '%' + @songwriter_name + '%'
)