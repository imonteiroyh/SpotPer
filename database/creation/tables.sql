CREATE TABLE record_label (
	code INT UNIQUE NOT NULL,
	name NVARCHAR(100) NOT NULL,
	address NVARCHAR(50),
	homepage_address NVARCHAR(50),
	CONSTRAINT record_label_PK PRIMARY KEY (code)
) ON spotper_fg_01;


CREATE TABLE record_label_phones (
	phone NVARCHAR(50) UNIQUE NOT NULL,
	record_label_code INT NOT NULL,
	CONSTRAINT record_label_phones_PK PRIMARY KEY (phone),
	CONSTRAINT record_label_phones_FK_record_label_code FOREIGN KEY (record_label_code)
		REFERENCES record_label (code)
		ON DELETE NO ACTION
		ON UPDATE CASCADE
) ON spotper_fg_01;


CREATE TABLE album (
	code INT NOT NULL,
	media_number INT NOT NULL DEFAULT 1,
	description NVARCHAR(50),
	record_label_code INT NOT NULL,
	record_date DATETIME NOT NULL,
	purchase_date DATETIME,
	purchase_price DECIMAL(10, 2),
	purchase_type NVARCHAR(50),
	physical_media NVARCHAR(20) NOT NULL,
	CONSTRAINT album_PK PRIMARY KEY (code, media_number),
	CONSTRAINT album_UQ UNIQUE (code, media_number),
	CONSTRAINT album_CK_record_date CHECK (record_date > CONVERT(datetime, '2000-01-01')),
	CONSTRAINT album_CK_physical_media_media_number CHECK (
		physical_media IN ('cd', 'vinyl')
		OR (physical_media = 'download' AND media_number = 1)
	),
	CONSTRAINT album_CK_price CHECK (purchase_price <= 3 * dbo.GetDDDAlbumPurchasePrice()),
	CONSTRAINT album_FK_record_label_code FOREIGN KEY (record_label_code)
		REFERENCES record_label (code)
		ON DELETE CASCADE
		ON UPDATE CASCADE
) ON spotper_fg_01;


CREATE TABLE composition_type (
	code INT UNIQUE NOT NULL,
	description NVARCHAR(50),
	CONSTRAINT composition_type_PK PRIMARY KEY (code)
) ON spotper_fg_01;


CREATE TABLE interpreter (
	code INT UNIQUE NOT NULL,
	name NVARCHAR(100),
	type NVARCHAR(50),
	CONSTRAINT interpreter_PK PRIMARY KEY (code)
) ON spotper_fg_01;


CREATE TABLE musical_period (
	code INT UNIQUE NOT NULL,
	description NVARCHAR(50),
	active_start NVARCHAR(10) NOT NULL,
	active_end NVARCHAR(10),
	CONSTRAINT musical_period_PK PRIMARY KEY (code)
) ON spotper_fg_01;


CREATE TABLE songwriter (
	code INT UNIQUE NOT NULL,
	name NVARCHAR(100) NOT NULL,
	birth_city NVARCHAR(50),
	birth_country NVARCHAR(50),
	birth_date DATETIME NOT NULL,
	death_date DATETIME,
	musical_period_code INT NOT NULL,
	CONSTRAINT songwriter_PK PRIMARY KEY (code),
	CONSTRAINT songwriter_FK_musical_period_code FOREIGN KEY (musical_period_code)
		REFERENCES musical_period (code)
		ON DELETE NO ACTION
		ON UPDATE CASCADE
) ON spotper_fg_01;


CREATE TABLE track (
	album_code INT NOT NULL,
	album_media_number INT NOT NULL,
	number INT NOT NULL,
	description NVARCHAR(50),
	composition_type_code INT NOT NULL,
	execution_time INT, --note: 'in seconds'
	recording_type NVARCHAR(50),
	CONSTRAINT track_PK PRIMARY KEY (album_code, album_media_number, number),
	CONSTRAINT track_UQ UNIQUE (album_code, album_media_number, number),
	CONSTRAINT track_CK_max_tracks CHECK (dbo.GetTrackQuantity(album_code, album_media_number) <= 64),
	CONSTRAINT track_CK_recording_type CHECK (
		(dbo.GetAlbumPhysicalMedia(album_code, album_media_number) = 'cd' AND recording_type IN ('ADD', 'DDD'))
		OR (dbo.GetAlbumPhysicalMedia(album_code, album_media_number) != 'cd' AND recording_type IS NULL) 
	),
	CONSTRAINT track_CK_baroque_DDD CHECK (
		(dbo.AlbumHasBaroque(album_code, album_media_number) = 1 AND recording_type = 'DDD')
		OR (dbo.AlbumHasBaroque(album_code, album_media_number) = 0)
	),
	CONSTRAINT track_FK_album_PK FOREIGN KEY (album_code, album_media_number)
		REFERENCES album (code, media_number)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	CONSTRAINT track_FK_composition_type_code FOREIGN KEY (composition_type_code)
		REFERENCES composition_type (code)
		ON DELETE NO ACTION
		ON UPDATE CASCADE
) ON spotper_fg_02


CREATE TABLE track_songwriter (
	album_code INT NOT NULL,
	album_media_number INT NOT NULL,
	track_number INT NOT NULL,
	songwriter_code INT NOT NULL,
	CONSTRAINT track_songwriter_PK PRIMARY KEY (album_code, album_media_number, track_number, songwriter_code),
	CONSTRAINT track_songwriter_FK_album_PK FOREIGN KEY (album_code, album_media_number, track_number)
		REFERENCES track (album_code, album_media_number, number)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	CONSTRAINT track_songwriter_FK_songwriter_code FOREIGN KEY (songwriter_code)
		REFERENCES songwriter (code)
		ON DELETE CASCADE
		ON UPDATE CASCADE
) ON spotper_fg_01;


CREATE TABLE track_interpreter (
	album_code INT NOT NULL,
	album_media_number INT NOT NULL,
	track_number INT NOT NULL,
	interpreter_code INT NOT NULL,
	CONSTRAINT track_interpreter_PK PRIMARY KEY (album_code, album_media_number, track_number, interpreter_code),
	CONSTRAINT track_interpreter_FK_album_PK FOREIGN KEY (album_code, album_media_number, track_number)
		REFERENCES track (album_code, album_media_number, number)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	CONSTRAINT track_interpreter_FK_interpreter_code FOREIGN KEY (interpreter_code)
		REFERENCES interpreter (code)
		ON DELETE CASCADE
		ON UPDATE CASCADE
) ON spotper_fg_01;


CREATE TABLE playlist (
	code INT NOT NULL UNIQUE,
	name NVARCHAR(100) NOT NULL,
	creation_date DATETIME NOT NULL,
	total_execution_time AS (dbo.GetTotalExecutionTime(code)),
	CONSTRAINT playlist_PK PRIMARY KEY (code)
) ON spotper_fg_02


CREATE TABLE track_playlist (
	album_code INT NOT NULL,
	album_media_number INT NOT NULL,
	track_number INT NOT NULL,
	playlist_code INT NOT NULL,
	last_played DATETIME,
	times_played INT NOT NULL DEFAULT 0,
	CONSTRAINT track_playlist_PK PRIMARY KEY (album_code, album_media_number, track_number, playlist_code),
	CONSTRAINT track_playlist_FK_album_PK FOREIGN KEY (album_code, album_media_number, track_number)
		REFERENCES track (album_code, album_media_number, number)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	CONSTRAINT track_playlit_FK_playlist_code FOREIGN KEY (playlist_code)
		REFERENCES playlist (code)
		ON DELETE CASCADE
		ON UPDATE CASCADE
) ON spotper_fg_02