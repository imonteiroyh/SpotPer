import pyodbc
from config.database import (
    SERVER,
    DATABASE,
    USERNAME,
    PASSWORD
)

def connect_to_database(
    driver='SQL Server',
    server=SERVER,
    database=DATABASE,
    username=USERNAME,
    password=PASSWORD,
    trusted_connection='yes'
):

    connection_string = (
        f'DRIVER={driver};'
        f'SERVER={server};'
        f'DATABASE={database};'
        f'USERNAME={username};'
        f'PASSWORD={password};'
        f'TRUSTED_CONNECTION={trusted_connection}'
    )

    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    return connection, cursor