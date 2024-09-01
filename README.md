How It Works:
Imports: The code imports keyboard from the pynput library.
Log File: It defines a file key_log.txt where all keystrokes will be logged.
Key Logging:
write_to_file function logs each keystroke to the file.
It tries to write the character representation of the key. If the key doesn't have a character (like Ctrl or Alt), it writes the key's name instead.
Listener: The code listens for key press and release events. It stops logging if the Esc key is pressed.
Step 3: Run the Keylogger
Run the script, and it will start logging keystrokes to the key_log.txt file until the Esc key is pressed.

Ethical Use:
Remember, always obtain explicit permission before running any keylogger on someone else’s system. Unauthorized use of keyloggers is illegal and unethical.

