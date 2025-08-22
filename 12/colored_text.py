import bext

bext.fg("red")
print("This text is red.")
bext.bg("blue")
print("Red text on a blue background is an ugly color scheme.")
bext.fg("reset")
bext.bg("reset")
print("The text is normal again. Ah, much better.")
