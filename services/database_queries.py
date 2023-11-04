from database.connection import connect_to_database
from database.database import execute_query

connection, cursor = connect_to_database()

def get_tracks():
    query = '''
        SELECT
            *
        FROM
            track
    '''

    result = execute_query(cursor, query)
    
    response = {
        'result': result
    }

    return response