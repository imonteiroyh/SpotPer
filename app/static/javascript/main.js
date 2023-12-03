function deletePlaylist(playlistCode) {
    if (confirm('Tem certeza de que deseja excluir esta playlist?')) {
        const options = {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            },
        };

        fetch('/playlist/' + playlistCode, options)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                if (data.message === 'Playlist deleted') {
                    console.log('Playlist deletada com sucesso');
                    if (data.reload) {
                        // Recarrega a página apenas se 'reload' for verdadeiro
                        window.location.reload();
                    }
                } else {
                    console.error('Erro ao excluir a playlist:', data.error || data.message);
                }
            })
            .catch(error => {
                console.error('Erro na solicitação DELETE:', error.message);
            });
    }
};

function removeTrack(playlistCode, albumCode, albumMediaNumber, trackNumber) {
    const data = {
        'album_code': albumCode,
        'album_media_number': albumMediaNumber,
        'track_number': trackNumber
    };

    const options = {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    };

    fetch('/playlist/' + playlistCode + '/removeTrack', options)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');

                return response.json();
            }

            location.reload()
        })
        .catch(error => {
            console.error('Error removing track: ', error.message)
        })
};

function addToPlaylist(playlistCode, albumCode, albumMediaNumber, trackNumber) {

    if (albumCode === null || albumMediaNumber === null || trackNumber === -1) {
        alert('Não foi possível adicionar a faixa. Parâmetros inválidos.');
        location.reload();
        return;
    }

    const data = {
        'album_code': albumCode,
        'album_media_number': albumMediaNumber,
        'track_number': trackNumber
    };

    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    };

    fetch('/playlist/' + playlistCode + '/addTrack', options)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');

                return response.json();
            }

            location.reload()
        })
        .catch(error => {
            console.error('Error adding track: ', error.message)
            alert('Não foi possível adicionar a faixa. Tente novamente.');
        })
};