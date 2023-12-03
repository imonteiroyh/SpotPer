from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from services import database_queries

routing = Blueprint('routing', __name__)

@routing.route('/', methods=['GET'])
def home():

    if request.method == 'GET':
        response = database_queries.get_playlists()
        playlists = response['result']

        return render_template('index.html', playlists=playlists)


@routing.route('/playlist/<int:playlist_code>', methods=['GET', 'DELETE'])
def playlist(playlist_code):
    
    if request.method == 'GET':
        response = database_queries.get_playlist(playlist_code)
        playlist = response['result']

        response = database_queries.get_tracks()
        tracks = response['result']
        
        return render_template('playlist.html', playlist=playlist, playlist_code=playlist_code, tracks=tracks)

    if request.method == 'DELETE':
        response = database_queries.delete_playlist(playlist_code)
        message = response['message']

        if message == 'success': 
            return jsonify({'message': 'Playlist deleted', 'reload': True})
        
        elif message == 'no changes':
            return jsonify({'message': 'No changes'})
    
        return jsonify({'error': 'Error deleting playlist'})
    

@routing.route('/playlist/<int:playlist_code>/removeTrack', methods=['DELETE'])
def remove_track(playlist_code):

    if request.method == 'DELETE':
        data = request.get_json()

        album_code = int(data.get('album_code'))
        album_media_number = int(data.get('album_media_number'))
        track_number = int(data.get('track_number'))

        if album_code is None or album_media_number is None or track_number is None:
            return jsonify({'error': 'Missing required parameters'})

        response = database_queries.remove_track(playlist_code, album_code, album_media_number, track_number)

        return jsonify(response)
    

@routing.route('/playlist/<int:playlist_code>/addTrack', methods=['POST'])
def add_track(playlist_code):

    if request.method == 'POST':
        data = request.get_json()

        album_code = int(data.get('album_code'))
        album_media_number = int(data.get('album_media_number'))
        track_number = int(data.get('track_number'))

        if album_code is None or album_media_number is None or track_number is None:
            return jsonify({'error': 'Missing required parameters'})

        response = database_queries.add_track(album_code, album_media_number, track_number, playlist_code)

        return jsonify(response)

    
@routing.route('/createPlaylist', methods=['GET', 'POST'])
def create_playlist():

    if request.method == 'POST':
        playlist_name = request.form.get('playlistName')
        selected_tracks = request.form.getlist('tracks')  

        tracks = [tuple(map(int, track.split(','))) for track in selected_tracks]

        response = database_queries.create_playlist(playlist_name, tracks)

        if response.get('error'):
            return jsonify({'error': response['error']})

        return redirect(url_for('routing.home'))
    

@routing.route('/get_queries', methods=['GET'])
def get_queries():

    if request.method == 'GET':
        response = database_queries.get_albums_above_average_price()
        albums = response['result']

        response = database_queries.get_label_with_most_playlists_with_dvorack()
        label = response['result']

        response = database_queries.get_songwriter_with_most_tracks_in_playlist()
        songwriter = response['result']

        response = database_queries.get_playlists_with_all_tracks_concert_baroque()
        concert_baroque_playlist = response['result']

        return render_template(
            'queries.html',
            albums=albums,
            label=label,
            songwriter=songwriter,
            cb_playlist=concert_baroque_playlist
            )