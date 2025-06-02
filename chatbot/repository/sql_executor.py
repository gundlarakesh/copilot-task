from django.db import connection


def execute_sql_query(sql_query):
    """
    Executes a raw SQL query and returns the result as a list of dictionaries.
    """
    with connection.cursor() as cursor:
        cursor.execute(sql_query)
        columns = [col[0] for col in cursor.description] if cursor.description else []
        results = (
            [dict(zip(columns, row)) for row in cursor.fetchall()] if columns else []
        )
    return results
