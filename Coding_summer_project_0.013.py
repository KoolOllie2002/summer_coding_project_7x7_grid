import tkinter as tk

def __main_start__():
    class GameBoard(tk.Frame):
        def __init__(self, parent, rows=7, columns=7, size=32, color1="orange", color2="green"):
            '''size is the size of a square, in pixels'''

            self.rows = rows
            self.columns = columns
            self.size = size
            self.color1 = color1
            self.color2 = color2
            self.pieces = {}

            canvas_width = columns * size
            canvas_height = rows * size

            tk.Frame.__init__(self, parent)
            self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0,
                                    width=canvas_width, height=canvas_height, background="bisque")
            self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)

            # this binding will cause a refresh if the user interactively
            # changes the window size
            self.canvas.bind("<Configure>", self.redraw)

        

        def redraw(self, event):
            xsize = int((event.width-1) / self.columns)
            ysize = int((event.height-1) / self.rows)
            self.size = min(xsize, ysize)
            self.canvas.delete("square")
            color = self.color2
            for row in range(self.rows):
                color = self.color1 if color == self.color2 else self.color2
                for col in range(self.columns):
                    x1 = (col * self.size)
                    y1 = (row * self.size)
                    x2 = x1 + self.size
                    y2 = y1 + self.size
                    self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square")
                    color = self.color1 if color == self.color2 else self.color2



    if __name__ == "__main__":
        root = tk.Tk()
        board = GameBoard(root)
        board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
        root.mainloop()

def close_start_screen_and_start():
    print('Closeing \'start_screen\'')
    start_screen.destroy()
    print('\'start_screen\' closed')
    print('Starting Game!')
    __main_start__()
    

def close_start_screen():
    print('Closeing \'start_screen\'')
    start_screen.destroy()
    print('\'start_screen\' closed')
   
    
start_screen = tk.Tk()

print('Buttons Loading...')   
A = tk.Button(start_screen, text ="Start", command = close_start_screen_and_start)
A.pack()
B = tk.Button(start_screen, text ="EXIT", command = close_start_screen)
B.pack()
print('Buttons Loaded!')
start_screen.mainloop()
