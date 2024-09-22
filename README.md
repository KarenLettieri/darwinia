# Telegram Expense Bot

This project is a Telegram bot designed to record expenses via text messages. The bot processes messages such as "Pizza 20 bucks," automatically categorizes the expense, and saves it into a PostgreSQL database. The bot features user verification via a whitelist and automatically handles expense categorization.

### Main Directories:

- `app/usecases`: Contains the main logic for the use cases, such as whitelist verification.
- `core/exceptions`: Defines custom exceptions used in the project.
- `domain/repositories`: Defines interfaces and repositories for data access.
- `infrastructure/database`: Modules for database connection.
- `tests`: Directory for unit tests.

## Project Requirements

### Primary Requirements

- **Python 3.8+**
- **PostgreSQL**: The database to store expenses and users.
- **Node.js LTS**: For the connector service (though not detailed in this README).

### Libraries Used

- `langchain==0.0.X` - Handles LLM processing.
- `psycopg2-binary==2.9.X` - PostgreSQL connection from Python.
- `aiogram==2.15.X` - Telegram API handling.
- `asyncpg==0.23.X` - Asynchronous PostgreSQL operations.
- `unittest` - Standard Python library for unit testing.
- `unittest.mock` - To mock objects in unit tests.

### Database

We used the following DDL to create the PostgreSQL tables:

```sql
CREATE TABLE users (
    "id" SERIAL PRIMARY KEY,
    "telegram_id" text UNIQUE NOT NULL
);

CREATE TABLE expenses (
    "id" SERIAL PRIMARY KEY,
    "user_id" integer NOT NULL REFERENCES users("id"),
    "description" text NOT NULL,
    "amount" money NOT NULL,
    "category" text);

## Project Requirements

### Clone the repository

git clone https://github.com/KarenLettieri/darwinia
cd telegram-expense-bot/bot_service

## Create a virtual environment and activate it
python -m venv venv
source venv/bin/activate    # On Linux/Mac
venv\Scripts\activate        # On Windows

### Install dependencies
langchain==0.0.X
psycopg2-binary==2.9.X
aiogram==2.15.X
asyncpg==0.23.X

### and then install the dependencies with pip install

## .env File

TELEGRAM_BOT_TOKEN=your_token_here
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_password

### Running the bot

python main.py

### Unit tests
## Runing tests

python -m unittest discover -s tests


```
