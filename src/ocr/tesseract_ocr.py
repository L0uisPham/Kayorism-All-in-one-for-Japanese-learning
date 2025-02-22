import pytesseract

# Optional: If Tesseract isn’t in your PATH, specify the full path to the executable:
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image, lang='jpn'):
    """
    Uses Tesseract OCR to extract Japanese text from an image.
    
    Args:
        image (PIL.Image): The preprocessed image for OCR.
        lang (str): The language to use (default 'jpn' for Japanese).
    
    Returns:
        str: The extracted text.
    """
    text = pytesseract.image_to_string(image, lang=lang)
    return text
