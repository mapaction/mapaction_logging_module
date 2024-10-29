# MapAction Logging Module

This module provides a structured and flexible way to log events in your MapAction applications, including the ability to store logs in a database for later analysis.

## Features

*   **Status Codes:** Uses an `Enum` to define clear and organized status codes for various events (success, errors, no data, etc.).
*   **Detailed Logging:** Captures essential information like timestamps, country, task name, status code, log message, and optional additional data.
*   **Database Storage:** Logs events to a database (SQLite for local development, easily configurable for other databases).
*   **Integration with Python's `logging`:**  Leverages the built-in `logging` module for flexibility in log handling and output.
*   **Easy to Use:** Provides a simple `log_event` function to handle logging operations.

## Installation

```bash
pip install . 
```

## Usage

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

log_event(
    country="UK",
    task_name="process_payment",
    status_code=StatusCode.ERROR_DATABASE,
    log_message="Failed to update payment status in the database",
    level=logging.ERROR 
)
```

## Configuration

*   **Database:**
    *   The module is set up to use SQLite for local development.  
    *   To use a different database, modify the database connection details in the `log_event` function (in `mapaction_logging/logger.py`).
    *   Consider using an ORM or a separate data access layer for easier database switching.

*   **Logging Levels:**
    *   Uses Python's standard logging levels (`logging.DEBUG`, `logging.INFO`, etc.).
    *   Configure logging levels and output (console, file) using `logging.basicConfig()` or a logging configuration file.

## Status Codes

The `StatusCode` enum (in `mapaction_logging/status_codes.py`) defines the following codes:

```python
from enum import Enum

class StatusCode(Enum):
    SUCCESS = 0
    ERROR_GENERIC = 100
    ERROR_DATABASE = 101
    ERROR_NETWORK = 102
    ERROR_FILE_IO = 103
    ERROR_VALIDATION = 104
    NO_DATA_FOUND = 200
    # Add more codes as needed
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
└── setup.py
```

## Requirements

The `requirements.txt` file lists the dependencies for this module:

```
sqlite3  # Or your preferred database library
```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

[MIT License]