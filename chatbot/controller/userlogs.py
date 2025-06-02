from chatbot.models import UserQuery


def log_user_query(user_id, query_text):
    """
    Create a UserQuery record when a user requests something.
    """
    UserQuery.objects.create(user_id=user_id, query_text=query_text)
