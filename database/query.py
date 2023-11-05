from flask import request
from database.connection import connect_to_database

class Query():
    response_map = {
        'GET': {
            'fetch': True
        },
        'POST': {
            'fetch': False
        },
        'DELETE': {
            'fetch': False
        }
    }

    def __init__(self, query, *args, **kwargs):
        self.connection, self.cursor = connect_to_database()
        self.query = query
        self.response = {'message': ''}
        
        method = request.method
        response_data = self.response_map.get(method)
        self.fetch = (kwargs.get('get', False) | response_data.get('fetch', False))

        self.__run_query(*args)

    def __run_query(self, *args):
        try:
            self.connection.autocommit = False
            self.cursor.execute(self.query, args)

            if self.fetch:
                self.result = [
                    dict(zip([column[0] for column in self.cursor.description], row))
                    for row in self.cursor.fetchall()
                ]

                self.response = {
                    'result': self.result
                }

            else:
                if self.cursor.rowcount > 0:
                    self.response = {
                        'message': 'success'
                    }
                
                else:
                    self.response = {
                        'message': 'no changes'
                    }

        except Exception as error:
            self.connection.rollback()
            self.response = {
                'error': f'Error running query: {str(error)}'
            }
        
        else:
            self.connection.commit()
        
        finally:
            self.connection.autocommit = True