def execute_query(cursor, query):
    cursor.execute(query)

    result = [
        dict(zip([column[0] for column in cursor.description], row))
        for row in cursor.fetchall()
    ]

    return result