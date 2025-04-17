################################################################################
# tooltip 
################################################################################
import tkinter as tk

class TooltipHandler:
    def __init__(self, root):
        self.root = root

    def show_tooltip(self, event, message):
        tooltip = tk.Toplevel()
        tooltip.wm_overrideredirect(True)
        tooltip.geometry(f"+{event.x_root + 10}+{event.y_root + 10}")
        label = tk.Label(tooltip, text=message, background="yellow", relief="solid", borderwidth=1)
        label.pack()
        label.after(800, tooltip.destroy)
