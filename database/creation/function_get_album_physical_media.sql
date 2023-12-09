CREATE FUNCTION GetAlbumPhysicalMedia(@album_code INT, @album_media_number INT)
RETURNS NVARCHAR(20)
AS
BEGIN
	DECLARE @physical_media NVARCHAR(20)

	SELECT 
		@physical_media = physical_media
	FROM
		album
	WHERE
		code = @album_code AND media_number = @album_media_number

	RETURN @physical_media
END