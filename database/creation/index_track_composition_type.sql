CREATE NONCLUSTERED INDEX IX_track_composition_type
ON track (composition_type_code)
WITH FILLFACTOR = 100