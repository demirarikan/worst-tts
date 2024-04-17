import sys
import re
from PySide6 import QtWidgets
import pygame

class TTSWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.text_field = QtWidgets.QPlainTextEdit()
        self.speak_button = QtWidgets.QPushButton('Speak!')
        # Initialize pygame
        pygame.mixer.init()
        self.sound_path = 'sound_files/'

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text_field)
        self.layout.addWidget(self.speak_button)

        self.speak_button.clicked.connect(self.speak_text)

    def play_ogg(self, file_path):
        try:
            # Load the .ogg file
            pygame.mixer.music.load(file_path)
            # Play the .ogg file
            pygame.mixer.music.play()
            # Wait until the .ogg finishes playing
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        except pygame.error:
            print("Could not load or play the .ogg file.")

    def speak_text(self):
        text_to_speak = self.text_field.toPlainText().lower()
        for letter in self.remove_non_alphanumeric(text_to_speak):
            file_path = self.sound_path + str(letter) + '.ogg'
            self.play_ogg(file_path)

    def remove_non_alphanumeric(self, text):
        return re.sub(r'\W+', '', text)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = TTSWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())