# IT Chatbot Backend

This project is a chatbot application designed to provide IT services such as ticket resolution, department management, and data retrieval based on user queries. It utilizes Django and Django REST Framework for the backend and integrates Google Generative AI for converting natural language queries into SQL.

## Project Structure

```
it-chatbot-backend
├── chatbot
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── services
│       └── nlp_to_sql.py
├── it_chatbot_backend
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd it-chatbot-backend
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the migrations:
   ```
   python manage.py migrate
   ```

2. Start the development server:
   ```
   python manage.py runserver
   ```

3. Access the API at `http://127.0.0.1:8000/`.

## Features

- Ticket resolution management
- Change assigned department
- Data retrieval based on user queries using natural language processing

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes. 

## License

This project is licensed under the MIT License.