import sqlite3  # Or your preferred database library

def log_to_database(timestamp, country, task_name, status_code, log_message, additional_data):
    """
    Inserts a log entry into the database.

    Args:
        timestamp: The timestamp of the log event.
        country: The country code.
        task_name: The name of the task.
        status_code: The status code.
        log_message: The log message.
        additional_data: Additional data to be logged.
    """
    try:
        conn = sqlite3.connect('mapaction_logging.db')
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO logs (timestamp, country, task_name, status_code, log_message, additional_data)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (timestamp, country, task_name, status_code, log_message, str(additional_data)))

        conn.commit()
    except Exception as e:
        # Handle database errors (e.g., log the error, raise an exception)
        raise e  # Or handle the error differently
    finally:
        if conn:
            conn.close()