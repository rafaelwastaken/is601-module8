# IS601 Module 8
FastAPI based calculator application

## 📦 Requirements

- Python 3.11+
- FastAPI 0.104.1
- Uvicorn 0.24.0
- Pydantic 2.5.0
- Pytest 7.4.3
- Playwright 1.40.0

## 🛠️ Installation

1. **Clone the repository** (or navigate to the project directory)

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers** (for E2E tests):
   ```bash
   playwright install
   ```

## 🏃 Running the Application

Start the FastAPI application:

```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

Then open your browser and navigate to:
```
http://localhost:8000
```

## 🧪 Running Tests

### Run all tests:
```bash
pytest -v
```

### Run specific test suites:

**Unit tests** (test calculator operations):
```bash
pytest tests/test_operations.py -v
```

**Integration tests** (test API endpoints):
```bash
pytest tests/test_main.py -v
```

**End-to-End tests** (test UI interactions):
```bash
pytest tests/test_e2e.py -v
```

### Run tests with coverage:
```bash
pytest --cov=app --cov=main tests/ -v
```

## 📁 Project Structure

```
.
├── main.py                      # FastAPI application
├── requirements.txt             # Python dependencies
├── README.md                    # This file
├── app/
│   ├── __init__.py             # Package initialization
│   └── operations.py           # Calculator operations module
├── templates/
│   └── index.html              # Web UI
├── tests/
│   ├── __init__.py             # Test package initialization
│   ├── test_operations.py      # Unit tests
│   ├── test_main.py            # Integration tests
│   └── test_e2e.py             # End-to-end tests
└── .github/
    └── workflows/
        └── ci.yml              # GitHub Actions CI configuration
```

## 📚 API Endpoints

### GET `/`
Returns the HTML calculator interface.

### POST `/add`
Adds two numbers.
```json
Request: {"a": 5, "b": 3}
Response: {"result": 8}
```

### POST `/subtract`
Subtracts two numbers.
```json
Request: {"a": 10, "b": 3}
Response: {"result": 7}
```

### POST `/multiply`
Multiplies two numbers.
```json
Request: {"a": 4, "b": 5}
Response: {"result": 20}
```

### POST `/divide`
Divides two numbers.
```json
Request: {"a": 20, "b": 4}
Response: {"result": 5}
```
