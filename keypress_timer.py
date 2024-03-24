# Script by Fr0z3n

from pynput import keyboard
import time

last_r_press_time = None

def on_press(key):
    global last_r_press_time
    try:
        # Check if the pressed Key is 'r' or 'R'
        if key.char.lower() == 'r':
            current_time = time.time()
            if last_r_press_time is not None:
                elapsed_time = current_time - last_r_press_time
                print(f"Time passed since last '{key.char}' key press: {elapsed_time:.2f} seconds")
            last_r_press_time = current_time
    except AttributeError:
        # The pressed key is not a character key
        pass

# Start listening for key presses globally (when not focused)
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Keep the script running
listener.join()