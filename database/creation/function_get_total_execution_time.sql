CREATE FUNCTION GetTotalExecutionTime(@playlist_code INT)
RETURNS INT
AS
BEGIN
	DECLARE @total_execution_time INT

	SELECT
		@total_execution_time = SUM(execution_time)
	FROM
		track_playlist tp
	LEFT JOIN
		track t
	ON
		tp.album_code = t.album_code AND tp.album_media_number = t.album_media_number AND tp.track_number = t.number
	WHERE
		tp.playlist_code = @playlist_code

	RETURN @total_execution_time
END