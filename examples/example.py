
from chalkboard import rt


# colorize will only take one of the 17 predefined colors. Use repr(rt) for a list of predefined colors
print(rt.colorize(text='Hello world!', color='green'))

# custom_foreground will accept RGB or hex colors (if using hex, you must assign RGB to None)
print(rt.custom_foreground(text='Colored with hex color', r=None, g=None, b=None, hex_color='#16FFB3'))

# Style has the most functionality. Can use predefined colors, RGB, or hex. Can also add bold, italic, strikethrough, blink,
# underline, or reverse.
print(rt.style(text='Hello world!', color='red', bold=True, italic=True))

print(rt.boldize(text='This is bold'))

print(rt.italicize(text='This is italic'))

print(rt.reversedize(text='This is reversed'))

print(rt.custom_background(text='Custom background color', r=225, g=50, b=100))



