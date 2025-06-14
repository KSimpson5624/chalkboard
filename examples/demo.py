
from chalkboard import rt

def interpolate_rgb(start, end, steps):
    for i in range(steps):
        t = i / (steps - 1)
        yield (
            int(start[0] + (end[0] - start[0]) * t),
            int(start[1] + (end[1] - start[1]) * t),
            int(start[2] + (end[2] - start[2]) * t),
        )

text = "Welcome to chalkboard"
colors = [
    (255, 0, 0),     # Red
    (255, 127, 0),   # Orange
    (255, 255, 0),   # Yellow
    (0, 255, 0),     # Green
    (0, 0, 255),     # Blue
    (75, 0, 130),    # Indigo
    (148, 0, 211),   # Violet
]

steps_per_blend = 5  # Increase for smoother gradients

for i in range(len(colors) - 1):
    start_color = colors[i]
    end_color = colors[i + 1]
    for r, g, b in interpolate_rgb(start_color, end_color, steps_per_blend):
        print(rt.custom_foreground(text, r, g, b))
