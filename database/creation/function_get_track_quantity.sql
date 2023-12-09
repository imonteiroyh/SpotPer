CREATE FUNCTION GetTrackQuantity(@album_code INT, @album_media_number INT)
RETURNS INT
AS
BEGIN
	DECLARE @track_quantity INT

	SELECT
		@track_quantity = COUNT(number)
	FROM
		track
	WHERE
		album_code = @album_code AND album_media_number = @album_media_number

	RETURN @track_quantity
END