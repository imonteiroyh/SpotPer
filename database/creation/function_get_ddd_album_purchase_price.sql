CREATE FUNCTION GetDDDAlbumPurchasePrice()
RETURNS DECIMAL(10, 2)
AS
BEGIN
	DECLARE @price INT

	SELECT
		@price = AVG(purchase_price)
	FROM
		album
	INNER JOIN
		(
			SELECT
				a.code,
				a.media_number
			FROM
				album a
			LEFT JOIN	
				track t
			ON
				a.code = t.album_code AND a.media_number = t.album_media_number
			GROUP BY
				a.code, a.media_number
			HAVING
				COUNT(*) = COUNT(CASE WHEN t.recording_type = 'DDD' THEN 1 ELSE NULL END)
		) AS all_ddd
	ON
		album.code = all_ddd.code AND album.media_number = all_ddd.media_number

	RETURN @price
END