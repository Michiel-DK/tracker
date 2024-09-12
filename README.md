# Financial Data API

## Project Overview

This project extracts financial data from multiple companies using the `yfinance` library, stores it in a PostgreSQL database, and provides access to the data via a RESTful API built with `FastAPI` and SQLAlchemy ORM. The entire setup is containerized using Docker Compose for ease of deployment and scalability.

## Technologies Used

- **Python**: Programming language used for the application logic.
- **yfinance**: Python library to fetch financial data from Yahoo Finance.
- **FastAPI**: Web framework used for building the API.
- **PostgreSQL**: Relational database to store financial data.
- **SQLAlchemy**: ORM used for database interaction and management.
- **Docker & Docker Compose**: Containerization and orchestration tools for the development and production environment.