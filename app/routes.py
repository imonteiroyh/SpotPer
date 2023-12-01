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
        result = response['result']
        print(result)

        return render_template('playlist.html', playlist=result, playlist_code=playlist_code) if result else jsonify({'error': 'Playlist not found'})
    
    if request.method == 'DELETE':
        response = database_queries.delete_playlist(playlist_code)
        message = response['message']

        if message == 'success': 
            return {
                'message': 'Playlist deleted'
            }
        elif message == 'no changes':
            return {
                'message': 'No changes'
            }
    
        return {
            'error': 'Error deleting playlist'
        }
    
@routing.route('/playlist/<int:playlist_code>removeTrack', methods=['DELETE'])
def remove_track(playlist_code,album_code,album_media_number,track_number):
    # album_code = request.args.get('album_code')
    # album_media_number = request.args.get('album_media_number')
    # track_number = request.args.get('track_number')

    if request.method == 'DELETE':
        album_code = request.args.get('album_code')
        album_media_number = request.args.get('album_media_number')
        track_number = request.args.get('track_number')

        # Verifique se os parâmetros estão presentes
        if album_code is None or album_media_number is None or track_number is None:
            return jsonify({'error': 'Missing required parameters'})

        # Converta os parâmetros para inteiros se necessário
        album_code = int(album_code)
        album_media_number = int(album_media_number)
        track_number = int(track_number)

        # Chame a função de remoção de faixa
        response = database_queries.remove_track(playlist_code, album_code, album_media_number, track_number)
        return response
    

@routing.route('/playlist/<int:playlist_code>addTrack', methods=['GET', 'POST'])
def add_track(playlist_code,album_code,album_media_number,track_number):
    # album_code = request.args.get('album_code')
    # album_media_number = request.args.get('album_media_number')
    # track_number = request.args.get('track_number')

    if request.method == 'GET':
        # mostrar como se fosse no '/'
        # aqui se quiser mostrar quais tracks já estão na playlist
        response = database_queries.get_playlist(playlist_code)
        result = response['result']


        return render_template('index.html', playlist=result) if result else jsonify({'error': 'Playlist not found'})

    if request.method == 'POST':
        # aí aqui o mesmo esquema do '/' de receber os dados só que agora sem playlist_name
        # list of tuples (album_code, album_media_number, track_number)
        album_code = request.args.get('album_code')
        album_media_number = request.args.get('album_media_number')
        track_number = request.args.get('track_number')

        # Verifique se os parâmetros estão presentes
        if album_code is None or album_media_number is None or track_number is None:
            return jsonify({'error': 'Missing required parameters'})

        # Converta os parâmetros para inteiros se necessário
        album_code = int(album_code)
        album_media_number = int(album_media_number)
        track_number = int(track_number)

        response = database_queries.populate_playlist(playlist_code, album_code,album_media_number,track_number)

        return response

    
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