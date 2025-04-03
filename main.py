import turtle
import winsound  # Windows-only sound library

# Set up the screen and turtle
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(1)
t.pencolor("brown")
t.shape("turtle")

# Play a sound when starting to draw
winsound.Beep(440, 500)  # Frequency 440Hz, duration 500ms

# Draw the L shape
t.forward(100)

# Play a different sound when turning
winsound.Beep(523, 300)  # Higher pitch for turning

t.right(90)

# Play another sound for the second line
winsound.Beep(659, 500)  # Even higher pitch

t.forward(100)

# Final sound when done
winsound.Beep(880, 700)  # Completion sound

# Keep the window open
turtle.done()
