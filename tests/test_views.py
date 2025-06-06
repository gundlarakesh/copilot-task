import pytest
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_chatbot_query_data_success(api_client):
    url = reverse("query-data")
    payload = {"query": "List all tickets"}
    response = api_client.post(url, payload, format="json")
    # The actual result depends on your implementation of handle_chatbot_query
    # Here we just check for a successful response and expected keys
    assert response.status_code == 200
    assert "result" in response.data
    assert "sql_query" in response.data


@pytest.mark.django_db
def test_chatbot_query_data_missing_query(api_client):
    url = reverse("query-data")
    payload = {}
    response = api_client.post(url, payload, format="json")
    assert response.status_code == 400
    assert "error" in response.data
    assert response.data["error"] == "query parameter is required."
