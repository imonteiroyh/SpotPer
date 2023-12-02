from database.query import Query

def get_playlists():
    query = '''
        SELECT
            *
        FROM
            playlist
    '''

    response = Query(query).response
    
    return response 


def get_available_playlist_code():
    query = '''
        DECLARE @NextCode INT

        SELECT
            @NextCode = MAX(code) + 1
        FROM
            playlist

        IF @NextCode IS NULL
            SET @NextCode = 1

        SELECT @NextCode AS next_code
    '''

    response = Query(query, get=True).response
    
    code = response['result'][0]['next_code']
    
    return code


def get_playlist(playlist_code):
    query = '''
        SELECT
            p.name AS playlist_name,
            p.creation_date,
            p.total_execution_time,
            a.description AS album_description,
            t.description AS track_description,
            t.execution_time AS track_execution_time,
            t.album_code,
            t.album_media_number,
            t.number AS track_number
        FROM
            playlist p
        LEFT JOIN
            track_playlist tp
        ON
            p.code = tp.playlist_code
        LEFT JOIN
            track t
        ON
            tp.album_code = t.album_code
            AND tp.album_media_number = t.album_media_number
            AND tp.track_number = t.number
        LEFT JOIN
            album a
        ON
            t.album_code = a.code
            AND t.album_media_number = a.media_number
        WHERE
            p.code = ?
    '''

    response = Query(query, playlist_code).response
    
    return response


def get_albums():
    query = '''
        SELECT
            a.code AS album_code,
            a.media_number AS album_media_number,
            a.description AS album_description,
            t.description AS track_description,
            t.execution_time AS track_execution_time
        FROM
            album a
        LEFT JOIN
            track t
        ON
            a.code = t.album_code
            AND a.media_number = t.album_media_number
    '''

    response = Query(query).response
    
    return response


def populate_playlist(playlist_code, tracks, create=False):
    query = '''
        INSERT INTO track_playlist(
            album_code, album_media_number, track_number, playlist_code, last_played, times_played
        )
        VALUES
            (?, ?, ?, ?, NULL, 0)
    '''
    
    album_code=tracks[0]
    album_media_number=tracks[1]
    track_number=tracks[2]

    for album_code, album_media_number, track_number in tracks:
        response = Query(query, album_code, album_media_number, track_number, playlist_code).response

        if response['message'] == 'no changes':
            return {
                'error': f'Error inserting track {track_number} in the playlist'
            }
    
    if create:
        return {
            'message': 'Playlist created'
        }
    else:
        return {
            'message': 'Tracks inserted into the playlist'
        }


def create_playlist(playlist_name, tracks):
    query = '''
        INSERT INTO playlist(code, name, creation_date) 
        VALUES
            (?, ?, CONVERT(VARCHAR, GETDATE(), 105))
    '''

    playlist_code = get_available_playlist_code()
    create_playlist_response = Query(query, playlist_code, playlist_name).response

    if create_playlist_response['message'] == 'no changes':
        return {
            'error': 'Error creating playlist'
        }
    
    populate_playlist_response = populate_playlist(playlist_code, tracks, create=True)

    return populate_playlist_response


def delete_playlist(playlist_code):
    query = '''
        DELETE FROM
            playlist
        WHERE
            playlist.code = ?
    '''

    response = Query(query, playlist_code).response

    return response


def remove_track(playlist_code, album_code, album_media_number, track_number):
    query = '''
        DELETE FROM
            track_playlist
        WHERE
            playlist_code = ? AND album_code = ? AND album_media_number = ? AND track_number = ?
    '''

    response = Query(query, playlist_code, album_code, album_media_number, track_number).response

    return response

def add_track_test(album_code, album_media_number, track_number, playlist_code):
    query = '''
        INSERT INTO track_playlist(
            album_code, album_media_number, track_number, playlist_code, last_played, times_played
        )
        VALUES
            (?, ?, ?, ?, NULL, 0)
    '''

    response = Query(query, playlist_code, album_code, album_media_number, track_number).response

    return response

# definindo iii. a)
def avg_album():
    query = '''
        SELECT
	        *
        FROM
	        album
        WHERE
	        purchase_price > (
		        SELECT
			        AVG(purchase_price)
		        FROM
			album
	    )
    '''
    response = Query(query).response

    return response

#definindo iii. b)
def label_Dvorack():
    query = '''
        SELECT
	        TOP 1 record_label.name
        FROM
	        record_label
        LEFT JOIN
	        (
		        SELECT
			        rl.code AS record_label_code,
			        COUNT(DISTINCT tp.playlist_code) AS number_of_playlists
		        FROM
			        record_label rl
		        LEFT JOIN
			        album a
		        ON
			        rl.code = a.record_label_code
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
		        LEFT JOIN
			        track_playlist tp
		        ON
			        t.album_code = tp.album_code AND t.album_media_number = tp.album_media_number AND t.number = tp.track_number
		        WHERE
			        s.name = 'Dvorack'
		        GROUP BY
			        rl.code
	        ) count_playlists
        ON
	        record_label.code = count_playlists.record_label_code
        ORDER BY
	        count_playlists.number_of_playlists DESC
    '''
    response = Query(query).response

    return response

#definindo iii. c)
def max_songwriter():
    query = '''
        SELECT
	        TOP 1 songwriter.name
        FROM
	        songwriter
        LEFT JOIN 
	        (
		        SELECT
			        s.code AS songwriter_code,
			        COUNT(playlist_code) AS number_of_tracks
		        FROM
			        songwriter s
		        LEFT JOIN
			        track_songwriter ts
		        ON
			        s.code = ts.songwriter_code
		        LEFT JOIN
			        track_playlist tp
		        ON
			        ts.album_code = tp.album_code AND ts.album_media_number = tp.album_media_number	AND ts.track_number = tp.track_number
		        GROUP BY
			        s.code
	        ) count_tracks
        ON
	        songwriter.code = count_tracks.songwriter_code
        ORDER BY
	        count_tracks.number_of_tracks DESC
    '''
    response = Query(query).response

    return response

#definindo iii. d)
def concert_barroque_playlist():
    query = '''
        SELECT
	        playlist.*
        FROM
	        playlist
        INNER JOIN
        (
	        SELECT
		        tp.playlist_code
	        FROM
		        track_playlist tp
	        WHERE NOT EXISTS (
		        SELECT
			        1
		        FROM
			        track t
		        WHERE
			        tp.album_code = t.album_code 
			        AND tp.album_media_number = t.album_media_number 
			        AND tp.track_number = t.number
			        AND (
			            -- SE NÃO FOR CONCERTO OU NÃO TIVER COMPOSITORES BARROCOS PASSA
				        NOT EXISTS(
					        SELECT	
						        1
					        FROM
						        composition_type ct
					        WHERE	
						        t.composition_type_code = ct.code
						        AND ct.description = 'Concerto'
				        ) OR NOT EXISTS (
					    SELECT
						    1
					    FROM
						    track_songwriter ts
					    LEFT JOIN
						    songwriter s
					    ON
						    ts.songwriter_code = s.code
					    LEFT JOIN
						    musical_period mp
					    ON
						    s.musical_period_code = mp.code
					    WHERE
						    ts.album_code = t.album_code 
						    AND ts.album_media_number = t.album_media_number 
						    AND ts.track_number = t.number
						    AND mp.description = 'Barroco'
				        )
			        )
	        )
        ) playlist_baroque_concert
    ON
	    playlist.code = playlist_baroque_concert.playlist_code
    '''
    response = Query(query).response

    return response

# resgatando faixas
def get_tracks():
    query = '''
        SELECT
            a.code AS album_code,
            a.media_number AS album_media_number,
            a.description AS album_description,
            COALESCE(t.number, -1) AS track_code,
            COALESCE(t.description, 'N/A') AS track_description
        FROM
            album a
        LEFT JOIN
            track t
        ON
            a.code = t.album_code
            AND a.media_number = t.album_media_number
    '''

    response = Query(query).response
    
    return response