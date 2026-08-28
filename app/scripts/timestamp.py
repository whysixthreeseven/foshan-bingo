# Datetime import:
from datetime import datetime


def timestamp() -> str:
    
    # Generating timestamp:
    datetime_now = datetime.now()
    timestamp_format: str = "%Y_%m_%d_%H_%M_%S"
    timestamp: str = datetime_now.strftime(timestamp_format)
    
    # Returning:
    return timestamp

