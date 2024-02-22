import pyttsx3
import os

def text_to_speech_from_file(file_path):
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

    # Read text from file
    with open(file_path, 'r') as file:
        text = file.read()

    # Convert text to speech
    engine.say(text)

    # Save the audio to a file
    output_folder = 'output'
    os.makedirs(output_folder, exist_ok=True)
    output_file = os.path.join(output_folder, 'output.mp3')  # You can change the extension as needed
    engine.save_to_file(text, output_file)

    # Wait for the speech to finish
    engine.runAndWait()

    # Prompt user for the next process
    user_input = input("automater> Start process number 2 (video maker)? Y/N: ").strip().lower()
    if user_input == 'y':
        os.system("python videomaker.py")
    elif user_input == 'n':
        print("Exiting...")
    else:
        print("Invalid input. Exiting...")

# Example usage
text_file_path = 'script.txt'
text_to_speech_from_file(text_file_path)
