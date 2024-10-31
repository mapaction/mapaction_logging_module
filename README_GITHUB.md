# MapAction Logging Module

This module provides a structured and flexible way to log events in your MapAction applications, including the ability to store logs in a database and visualize them with a Streamlit dashboard.

## Features

*   **Status Codes:** Uses an `Enum` to define clear and organized status codes for various events (success, errors, no data, etc.).
*   **Detailed Logging:** Captures essential information like timestamps, country, task name, status code, log message, and optional additional data.
*   **Database Storage:** Logs events to a SQLite database for easy analysis and retrieval.
*   **Integration with Python's `logging`:**  Leverages the built-in `logging` module for flexibility in log handling and output.
*   **Easy to Use:** Provides a simple `log_event` function to handle logging operations.
*   **Streamlit Dashboard:** Includes a Streamlit app (`dashboard/mapaction_logging_app.py`) to visualize and filter log data.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

**1. Logging events:**

```python
from mapaction_logging import log_event, StatusCode 

# Example usage
log_event(
    country="US", 
    task_name="user_registration", 
    status_code=StatusCode.SUCCESS, 
    log_message="User registered successfully", 
    additional_data={"user_id": 123}
)
```

**2. Running the dashboard:**

```bash
streamlit run dashboard/mapaction_logging_app.py
```

## Configuration

*   **Database:**
    *   The module uses an SQLite database (`mapaction_logging.db`) for storing logs.
    *   The database table is automatically created when the module is imported.

*   **Logging Levels:**
    *   Uses Python's standard logging levels (`logging.DEBUG`, `logging.INFO`, etc.).
    *   Configure logging levels and output (console, file) using `logging.basicConfig()` or a logging configuration file.

## Status Codes

The `StatusCode` enum (in `mapaction_logging/status_codes.py`) defines the following codes:

```python
from enum import Enum
import logging
from requests import Response

class StatusCode(Enum):
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NO_CONTENT = 204
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    PAYMENT_REQUIRED = 402
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    NOT_ACCEPTABLE = 406
    REQUEST_TIMEOUT = 408
    CONFLICT = 409
    INTERNAL_SERVER_ERROR = 500
    NOT_IMPLEMENTED = 501
    BAD_GATEWAY = 502
    SERVICE_UNAVAILABLE = 503
    GATEWAY_TIMEOUT = 504
    UNKNOWN = -1
```

## Database Table Schema

The log data will be stored in a database table with the following structure:

| Column        | Data Type    | Description                                 |
|---------------|--------------|---------------------------------------------|
| id            | INTEGER      | Primary key (auto-incrementing)             |
| timestamp     | TIMESTAMP    | When the event occurred                     |
| country       | VARCHAR(255) | Country code (e.g., "US", "GB")             |
| task_name     | VARCHAR(255) | Name of the task being logged              |
| status_code   | INTEGER      | The status code (from your `StatusCode` enum) |
| log_message   | TEXT         | The log message                             |
| additional_data | JSON/TEXT    | (Optional) Extra data in JSON or text format |

## File Structure

```
mapaction_logging_module/
├── mapaction_logging/
│   ├── __init__.py
│   ├── logger.py
│   ├── status_codes.py
│   └── database.py
├── dashboard/
│   └── mapaction_logging_app.py 
└── setup.py
```

## Requirements

The `requirements.txt` file lists the dependencies for this module:

```
streamlit pandas
```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

MIT License
