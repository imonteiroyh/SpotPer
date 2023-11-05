from flask import Blueprint, request
from services import database_queries

routing = Blueprint('routing', __name__)

@routing.route('/', methods=['GET'])
def home():
    # PRIMEIRO CARD DEVE SER PRA REDIRECIONAR PRA CRIAÇÃO DE PLAYLIST
    # QUALQUER CARD CLICADO DEVE REDIRECIONAR PARA AS INFORMAÇÕES DAS FAIXAS NA PLAYLIST

    if request.method == 'GET':
        response = database_queries.get_playlists()
        return response

@routing.route('/playlist/<int:playlist_code>', methods=['GET', 'DELETE'])
def playlist(playlist_code):
    
    if request.method == 'GET':
        response = database_queries.get_playlist(playlist_code)
        result = response['result']

        return result if result else {
            'error': 'Playlist not found'
        }
    
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
    
@routing.route('/playlist/<int:playlist_code>/removeTrack', methods=['DELETE'])
def remove_track(playlist_code):
    # album_code = request.args.get('album_code')
    # album_media_number = request.args.get('album_media_number')
    # track_number = request.args.get('track_number')

    if request.method == 'DELETE':
        album_code = 1
        album_media_number = 1
        track_number = 1

        response = database_queries.remove_track(playlist_code, album_code, album_media_number, track_number)

        return response
    

@routing.route('/playlist/<int:playlist_code>/addTrack', methods=['GET', 'POST'])
def add_track(playlist_code):
    # album_code = request.args.get('album_code')
    # album_media_number = request.args.get('album_media_number')
    # track_number = request.args.get('track_number')

    if request.method == 'GET':
        # mostrar como se fosse no '/'
        # aqui se quiser mostrar quais tracks já estão na playlist
        response = database_queries.get_playlist(playlist_code)
        result = response['result']


        return result if result else {
            'error': 'Playlist not found'
        }

    if request.method == 'POST':
        # aí aqui o mesmo esquema do '/' de receber os dados só que agora sem playlist_name
        # list of tuples (album_code, album_media_number, track_number)
        tracks = [
        (1, 1, 1),
        (1, 1, 2)
        ]

        response = database_queries.populate_playlist(playlist_code, tracks)

        return response

    
@routing.route('/createPlaylist', methods=['GET', 'POST'])
def create_playlist():
    if request.method == 'GET':
        response = database_queries.get_albums()
        result = response['result']

        return result if result else {
            'error': 'Error getting albums'
        }
    
    if request.method == 'POST':
        # string
        playlist_name = 'x' 

        # list of tuples (album_code, album_media_number, track_number)
        tracks = [
        (1, 1, 2),
        (2, 1, 1),
        (3, 1, 1)
        ]

        response = database_queries.create_playlist(playlist_name, tracks)

        return response