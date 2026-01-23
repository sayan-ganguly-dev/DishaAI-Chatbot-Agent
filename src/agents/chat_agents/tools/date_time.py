import time
from langchain.tools import tool

@tool
def get_current_date_and_time() -> str:
    """
    use this to get current date and time
    """
    return time.ctime()