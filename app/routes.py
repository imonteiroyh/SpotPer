from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from services import database_queries

routing = Blueprint('routing', __name__)

@routing.route('/', methods=['GET'])
def home():
    # PRIMEIRO CARD DEVE SER PRA REDIRECIONAR PRA CRIAÇÃO DE PLAYLIST
    # QUALQUER CARD CLICADO DEVE REDIRECIONAR PARA AS INFORMAÇÕES DAS FAIXAS NA PLAYLIST

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
    

@routing.route('/playlist/<int:playlist_code>/addTrack', methods=['GET', 'POST'])
def add_track(playlist_code):
    # album_code = request.args.get('album_code')
    # album_media_number = request.args.get('album_media_number')
    # track_number = request.args.get('track_number')
    if request.method == 'POST':
        data = request.get_json()

        album_code = int(data.get('album_code'))
        album_media_number = int(data.get('album_media_number'))
        track_number = int(data.get('track_number'))

        if album_code is None or album_media_number is None or track_number is None:
            return jsonify({'error': 'Missing required parameters'})

        # Agora você pode usar album_code, album_media_number e track_number conforme necessário.
        response = database_queries.add_track_test(album_code, album_media_number, track_number, playlist_code)

        return jsonify(response)

    
@routing.route('/createPlaylist', methods=['GET', 'POST'])
def create_playlist():
    if request.method == 'GET':
        response = database_queries.get_albums()
        result = response['result']

        return jsonify(result) if result else jsonify({'error': 'Error getting albums'})
    
    if request.method == 'POST':
        playlist_name = request.form.get('playlistName')
        selected_tracks = request.form.getlist('tracks')  

        tracks = [tuple(map(int, track.split(','))) for track in selected_tracks]

        response = database_queries.create_playlist(playlist_name, tracks)

        if response.get('error'):
            return jsonify({'error': response['error']}), 400  # 400 Bad Request

        return redirect(url_for('routing.home'))  # Redirect to the home page after creating the playlist
    
@routing.route('/get_queries', methods=['GET'])
def get_queries():
    # PRIMEIRO CARD DEVE SER PRA REDIRECIONAR PRA CRIAÇÃO DE PLAYLIST
    # QUALQUER CARD CLICADO DEVE REDIRECIONAR PARA AS INFORMAÇÕES DAS FAIXAS NA PLAYLIST

    if request.method == 'GET':
        #rota iii. a)
        response = database_queries.avg_album()
        albums = response['result']

        #rota iii. b)
        response = database_queries.label_Dvorack()
        label = response['result']

        #rota iii. c) 
        response = database_queries.max_songwriter()
        songwriter = response['result']

        #rota iii. d) 
        response = database_queries.concert_barroque_playlist()
        cb_playlist = response['result']

        return render_template('queries.html', albums=albums, label=label, songwriter=songwriter, cb_playlist=cb_playlist)
    
