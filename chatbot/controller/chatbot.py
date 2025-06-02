from chatbot.controller.userlogs import log_user_query
from chatbot.repository.sql_executor import execute_sql_query
from chatbot.services.nlp_to_sql import convert_nlp_to_sql


def handle_chatbot_query(query, user_id=None):
    """
    Process the chatbot query and return a response.
    Calls the NLP-to-SQL conversion service and executes the SQL.
    Audits the user request.
    """
    # Audit the user request
    log_user_query(user_id, query)
    sql_query = convert_nlp_to_sql(query)
    results = execute_sql_query(sql_query)
    return results, sql_query
