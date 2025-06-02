import os

import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


def convert_nlp_to_sql(nlp_query):
    """
    Converts a natural language query into an SQL query using Google Generative AI.

    Args:
        nlp_query (str): The natural language query to be converted.

    Returns:
        str: The corresponding SQL query.
    """
    genai.configure(api_key=GOOGLE_API_KEY)

    model = genai.GenerativeModel()  # Use the default generative model

    prompt = (
        "You are an expert in converting English questions to SQL query!\n"
        "The SQL database has the following tables and columns:\n"
        "TABLE: DEPARTMENT (id, name, description)\n"
        "TABLE: TICKET (id, title, description, created_at, updated_at, status, assigned_department_id)\n"
        "If the question is related to creating please include the created_at and updated_at(datetime in string), and status fileds in the sql query.\n"
        "For example,\n"
        "Example 1 - How many tickets are open? The SQL command will be: SELECT COUNT(*) FROM TICKET WHERE status='open';\n"
        "Example 2 - List all tickets assigned to department 1? The SQL command will be: SELECT * FROM TICKET WHERE assigned_department_id=1;\n"
        "Example 3 - What are the names of all departments? The SQL command will be: SELECT name FROM DEPARTMENT;\n"
        "Also, the SQL code should not have ``` in the beginning or end.\n"
        "In any situation, or the request please give the SQL query only, without any additional text.\n"
        "Convert the following request:\n"
    )

    response = model.generate_content([prompt, nlp_query])
    sql_query = response.text.strip().strip("`").strip("sql").strip()
    print(sql_query)
    return sql_query


def validate_sql_query(sql_query):
    """
    Validates the generated SQL query to ensure it is safe to execute.

    Args:
        sql_query (str): The SQL query to validate.

    Returns:
        bool: True if the query is valid, False otherwise.
    """
    # Placeholder for SQL validation logic
    # Implement validation to prevent SQL injection and other vulnerabilities
    return (
        True
        if sql_query.lower().startswith(("select", "insert", "update", "delete"))
        else False
    )
