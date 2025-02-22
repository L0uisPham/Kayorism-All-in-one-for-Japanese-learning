from PIL import ImageOps, ImageFilter

def preprocess_image(image):
    """
    Preprocesses the input image to improve OCR accuracy.
    Converts the image to grayscale, adjusts contrast, and sharpens it.
    
    Args:
        image (PIL.Image): The image to process.
    
    Returns:
        PIL.Image: The processed image.
    """
    # Convert image to grayscale
    gray = ImageOps.grayscale(image)
    # Automatically adjust contrast
    contrasted = ImageOps.autocontrast(gray)
    # Sharpen the image slightly
    sharpened = contrasted.filter(ImageFilter.SHARPEN)
    return sharpened
