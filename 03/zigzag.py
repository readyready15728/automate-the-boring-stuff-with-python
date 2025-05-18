import time
import sys

indent = 0
indent_increasing = True

try:
    while True:  # The main program loop
        print(" " * indent, end="")
        print("********")
        time.sleep(0.1)  # Pause of 1/10 of a second

        if indent_increasing:
            # Increase the number of spaces
            indent += 1

            if indent == 20:
                # Change direction
                indent_increasing = False
        else:
            # Decrease the number of spaces
            indent -= 1

            if indent == 0:
                # Change direction
                indent_increasing = True
except KeyboardInterrupt:
    sys.exit()
