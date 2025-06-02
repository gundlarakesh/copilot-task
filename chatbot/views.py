from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .controller.chatbot import handle_chatbot_query  # Import the controller function


class ChatbotViewSet(viewsets.ViewSet):

    @action(detail=False, methods=["post"], url_path="query-data")
    def query_data(self, request):
        query = request.data.get("query")
        # Call the controller function
        result, sql_query = handle_chatbot_query(query)
        return Response({"result": result, "sql_query": sql_query})
