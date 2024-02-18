import speech_recognition as sr


# Function to convert speech to text
def speech_to_text(num):
    # Creating a recognizer object for speech recognition operations
    recognizer = sr.Recognizer()

    # Creating a microphone object to select the microphone used by the user
    microphone = sr.Microphone()

    n = 1

    with microphone as source:
        # Adjust the noise level based on the first second of recording
        recognizer.adjust_for_ambient_noise(source)

        print("\nStarting listening...\n")

        while n <= num:
            # Capture audio from the microphone
            audio_data = recognizer.listen(source)

            try:
                # Perform speech recognition
                text = recognizer.recognize_google(audio_data)
                print(f"{n}. {text}")

                # Write the recognized text to a file
                audio_to_file(text)

                n += 1
            except sr.UnknownValueError:
                print("Unable to recognize speech")
            except sr.RequestError as e:
                print("Error making request to speech recognition service; {0}".format(e))
        print("\nListening stopped\n")


# Function to append recognized text to a file
def audio_to_file(text):
    with open("output.txt", "a") as f:
        f.write(text + "\n")
