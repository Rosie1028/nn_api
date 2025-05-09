import re

def remove_tags(text: str) -> str:
    """
    Remove HTML/XML tags from the input text.

    Args:
        text (str): The input string possibly containing tags.

    Returns:
        str: The text with tags removed.
    """
    return re.sub(r'<[^>]+>', '', text)