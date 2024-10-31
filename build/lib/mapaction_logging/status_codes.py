from enum import Enum
import logging
from requests import Response

class StatusCode(Enum):
    """
    Defines HTTP status codes for logging events.
    """
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
    UNKNOWN = -1  # Default for unrecognized status codes

    @staticmethod
    def from_response(response: Response, log: bool = True) -> 'StatusCode':
        """
        Get status code from a Response object.

        :param response: The response object.
        :param log: Log the status code retrieval.
        :return: The corresponding StatusCode enum member, or StatusCode.UNKNOWN.
        """
        try:
            status_code = response.status_code
            if log:
                logging.debug(f"Status code from response: {status_code}")
            return StatusCode(status_code)
        except ValueError as e:
            if log:
                logging.error(f"Unrecognized status code: {response.status_code}")
                logging.error(f"Error: {e}")
            return StatusCode.UNKNOWN
        except AttributeError as e:
            if log:
                logging.error(f"Invalid response object: {e}")
            return StatusCode.UNKNOWN
