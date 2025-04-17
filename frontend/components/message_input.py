from nicegui import Textbox, Row
from nicegui.events import on

class MessageInput:
    def __init__(self, on_send):
        """
        Initialize the message input field.
        :param on_send: Function to call when the user sends a message
        """
        self.on_send = on_send
        self.textbox = Textbox(placeholder="Type your message...").style("width: 100%")

    def setup(self):
        """
        Set up the input box and handle user input.
        """
        self.textbox.on('keydown.enter', self.send_message)

    def send_message(self, event):
        """
        Called when the user presses Enter.
        """
        message = self.textbox.value
        if message:
            self.on_send(message)
            self.textbox.clear()

    def get_input_field(self):
        """
        Returns the input field to be rendered in the UI.
        """
        return self.textbox
