import tkinter as tk

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Basic Paint App")

        # Create a canvas widget
        self.canvas = tk.Canvas(self.root, bg="white", width=800, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Bind mouse events to the canvas
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

        # Initialize variables
        self.old_x = None
        self.old_y = None

    def paint(self, event):
        paint_color = "black"
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y,
                                    width=5, fill=paint_color,
                                    capstyle=tk.ROUND, smooth=tk.TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x = None
        self.old_y = None

if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()
