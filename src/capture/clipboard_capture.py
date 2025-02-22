import pyperclip

def get_clipboard_text():
    """
    Retrieves the current text from the clipboard.
    
    Returns:
        str: The text currently stored in the clipboard.
    """
    return pyperclip.paste()
