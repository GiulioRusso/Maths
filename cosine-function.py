import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def update(val):
    a = slider_a.val
    b = slider_b.val
    c = slider_c.val
    p = slider_p.val
    f = a * np.cos(b * x + p) + c
    line.set_ydata(f)
    ax.set_title(f"Cosine Function f(x) = {a:.2f} * cos({b:.2f} * x + {p:.2f}) + {c:.2f}")
    fig.canvas.draw_idle()

# Create data for x values
x = np.arange(0, 2 * np.pi, 0.01)

# Initial values of a, b, c and p
initial_a = 1
initial_b = 1
initial_c = 0
initial_p = 0

# Create the plot
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)  # Adjust the plot area to accommodate sliders

# Plot the initial cosine function
line, = ax.plot(x, initial_a * np.cos(initial_b * x + initial_p) + initial_c, linewidth=2)

# Set plot labels and grid
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.grid(True)

# Set the x and y axis limits
plt.xlim(0, 2 * np.pi)
plt.ylim(-5, 5)

# Create sliders
ax_a = plt.axes([0.1, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_b = plt.axes([0.1, 0.05, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_c = plt.axes([0.1, 0.15, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_p = plt.axes([0.1, 0, 0.65, 0.03], facecolor='lightgoldenrodyellow')

slider_a = Slider(ax_a, 'a', -5, 5, valinit=initial_a, valstep=0.1)
slider_b = Slider(ax_b, 'b', -5, 5, valinit=initial_b, valstep=0.1)
slider_c = Slider(ax_c, 'c', -5, 5, valinit=initial_c, valstep=0.1)
slider_p = Slider(ax_p, 'p', -5, 5, valinit=initial_p, valstep=0.1)

# Update the plot when sliders' values change
slider_a.on_changed(update)
slider_b.on_changed(update)
slider_c.on_changed(update)
slider_p.on_changed(update)

plt.show()
