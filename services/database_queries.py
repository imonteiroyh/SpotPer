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
    
    for track in tracks:
        album_code, album_media_number, track_number = track
        response = Query(query, album_code, album_media_number, track_number, playlist_code).response

        if response['message'] == 'no changes':
            return {
                'error': f'Error inserting track {track} in the playlist'
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