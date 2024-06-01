import requests


class ResponseError:
    @staticmethod
    def get_error_message(exception) -> str:
        if isinstance(exception, requests.exceptions.HTTPError):
            if exception.response.status_code == 404:
                return 'Currency data not found. Please check the data.'
            else:
                return f'HTTP error occurred'
        elif isinstance(exception, requests.exceptions.ConnectionError):
            return 'Connection error. Please check your network connection and try again.'
        elif isinstance(exception, requests.exceptions.Timeout):
            return 'The request timed out. Please try again later.'
        else:
            return f'An error occurred'
