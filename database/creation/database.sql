CREATE DATABASE	BDSpotPer
ON
	PRIMARY
	(
	NAME = 'spotper',
	FILENAME = 'C:\FBD\spotper.mdf',
	SIZE = 50MB,
	MAXSIZE = 100MB,
	FILEGROWTH = 1MB
	),

	FILEGROUP spotper_fg_01
	(
	NAME = 'spotper_1',
	FILENAME = 'C:\FBD\spotper_01.ndf',
	SIZE = 30MB,
	MAXSIZE = 100MB,
	FILEGROWTH = 15%
	),
	(
	NAME = 'spotper_2',
	FILENAME = 'C:\FBD\spotper_02.ndf',
	SIZE = 30MB,
	MAXSIZE = 100MB,
	FILEGROWTH = 15%
	),

	FILEGROUP spotper_fg_02
	(
	NAME= 'spotper_3',
	FILENAME = 'C:\FBD\spotper_03.ndf',
	SIZE = 30MB,
	MAXSIZE = 100MB,
	FILEGROWTH = 15%
	)

LOG ON
(
NAME = 'spotper_log',
FILENAME = 'C:\FBD\spotper_log.ldf',
SIZE = 30MB,
MAXSIZE = 100MB,
FILEGROWTH = 10%
)