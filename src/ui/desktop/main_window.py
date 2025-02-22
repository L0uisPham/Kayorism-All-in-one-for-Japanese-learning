import sys
from PyQt5 import QtWidgets
from src.capture import window_capture, clipboard_capture, image_preprocessing
from src.ocr import tesseract_ocr

class TextExtractorUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Japanese Text Extractor")
        self.setGeometry(100, 100, 800, 600)

        # Create layout containers
        main_layout = QtWidgets.QVBoxLayout()
        button_layout = QtWidgets.QHBoxLayout()

        # Dropdown for available windows
        self.window_dropdown = QtWidgets.QComboBox()
        self.refresh_windows()

        # Buttons for capture actions
        self.capture_window_btn = QtWidgets.QPushButton("Capture Window")
        self.capture_window_btn.clicked.connect(self.capture_window_text)
        self.capture_clipboard_btn = QtWidgets.QPushButton("Capture Clipboard")
        self.capture_clipboard_btn.clicked.connect(self.capture_clipboard_text)

        # Text area to display extracted text
        self.output_text = QtWidgets.QTextEdit()
        self.output_text.setReadOnly(True)

        # Arrange buttons in layout
        button_layout.addWidget(self.window_dropdown)
        button_layout.addWidget(self.capture_window_btn)
        button_layout.addWidget(self.capture_clipboard_btn)

        # Add all widgets to main layout
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.output_text)
        self.setLayout(main_layout)

    def refresh_windows(self):
        """
        Populate the dropdown with the list of available window titles.
        """
        windows = window_capture.list_windows()
        self.window_dropdown.clear()
        self.window_dropdown.addItems(windows)

    def capture_window_text(self):
        """
        Capture a screenshot from the selected window, process it,
        extract text via OCR, and display the result.
        """
        window_title = self.window_dropdown.currentText()
        if not window_title:
            self.output_text.append("No window selected!")
            return
        try:
            screenshot = window_capture.capture_window(window_title)
            processed_image = image_preprocessing.preprocess_image(screenshot)
            extracted_text = tesseract_ocr.extract_text_from_image(processed_image)
            self.output_text.append(f"Extracted Text from window '{window_title}':\n{extracted_text}\n")
        except Exception as e:
            self.output_text.append(f"Error capturing window: {e}")

    def capture_clipboard_text(self):
        """
        Retrieve text from the clipboard and display it.
        """
        try:
            text = clipboard_capture.get_clipboard_text()
            if text:
                self.output_text.append("Extracted Text from Clipboard:\n" + text + "\n")
            else:
                self.output_text.append("Clipboard does not contain text!")
        except Exception as e:
            self.output_text.append(f"Error capturing clipboard: {e}")

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = TextExtractorUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
