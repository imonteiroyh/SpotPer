CREATE NONCLUSTERED INDEX IX_track_album
ON track (album_code, album_media_number)
WITH FILLFACTOR = 100