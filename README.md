
# LoanManager — Django API

A lightweight backend API for managing loan records, developed with Python and Django as a hands-on software engineering project.

The project demonstrates REST-style HTTP communication, database persistence, input validation, and error handling using Django's built-in tools.

## Tech Stack

- Python 3.14
- Django 5.2
- SQLite
- Django ORM
- HTTP / JSON
- Git and GitHub

## Features

- Create loan records using POST requests.
- Retrieve loan records using GET requests.
- Store data in a relational SQLite database.
- Validate loan amounts before saving.
- Reject invalid requests with HTTP 400.
- Return HTTP 201 when a loan is created.
- Use Django's built-in CSRF protection.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/loans/ | Retrieve all loans |
| POST | /api/loans/ | Create a new loan |

### Example POST Request

```json
{
  "amount": "10000.00",
  "interest_rate": "15.00"
}
```

Successful response: HTTP 201 Created.

Loan amounts must be greater than zero.

Invalid requests return HTTP 400 Bad Request.

POST requests require a valid CSRF cookie and token under the current Django configuration.

## Project Structure

```text
LoanManager/
├── config/          # Django project settings and URLs
├── loans/           # Models, views, routes and migrations
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Local Installation

Clone the repository:

```bash
git clone https://github.com/DanielGaitan1/LoanManager-Django-API.git
cd LoanManager-Django-API
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows CMD:

```cmd
.venv\Scripts\activate.bat
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Configure the environment variable `DJANGO_SECRET_KEY` with a locally generated secret key before running Django.

Apply database migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

API available at:

http://127.0.0.1:8000/api/loans/

## Architecture

1. A client sends an HTTP request.
2. Django resolves the URL.
3. The view processes the request.
4. The ORM interacts with SQLite.
5. Django returns an HTTP response containing JSON.

## Current Limitations

This is an educational project, not a production-ready financial system.

The API currently does not implement user authentication, authorization, automated tests, or loan update/delete endpoints.

## Author

Daniel Gaitan

Computer Engineering Student — University of Guadalajara

GitHub: https://github.com/DanielGaitan1
```
