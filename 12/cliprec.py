import pyperclip
import time

print('Recording clipboard... (Ctrl-C to terminate)')

previous_content = ''

try:
    while True:
        content = pyperclip.paste()

        if content != previous_content:
            print(content)
            previous_content = content

    time.sleep(0.01) # Pause to avoid hogging the CPU
except KeyboardInterrupt:
    pass
