#  Copyright (c) 2024. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
import pyttsx3

from main import mp


def Data_TTS(map=mp):
    """
    Reads data as text and converts it to speech.

    Args:
        mp: The data to be converted to speech.

    Returns:
        None
    """
    # Your data text-to-speech code here
    # ...
 # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set the properties of the speech
    engine.setProperty('rate', 150)  # Speed of speech (words per minute)

    # Convert the data to speech
    engine.say(map)
    engine.runAndWait()