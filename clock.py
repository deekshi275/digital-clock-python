from tkinter import Label, Tk, Canvas
import time
import math

app = Tk()
app.title("Digital Clock")
app.geometry("420x420")
app.resizable(False, False)
app.configure(bg="#222831")

canvas_size = 400
clock_radius = 180
center_x = center_y = canvas_size // 2

canvas = Canvas(app, width=canvas_size, height=canvas_size, bg="#222831", highlightthickness=0)
canvas.pack()

# Draw the round clock face
def draw_clock_face():
    canvas.create_oval(
        center_x - clock_radius, center_y - clock_radius,
        center_x + clock_radius, center_y + clock_radius,
        fill="#393E46", outline="#FFD369", width=8
    )
    # Draw hour marks
    for i in range(12):
        angle = math.radians(i * 30 - 90)
        x1 = center_x + (clock_radius - 20) * math.cos(angle)
        y1 = center_y + (clock_radius - 20) * math.sin(angle)
        x2 = center_x + (clock_radius - 40) * math.cos(angle)
        y2 = center_y + (clock_radius - 40) * math.sin(angle)
        canvas.create_line(x1, y1, x2, y2, fill="#FFD369", width=4)

# Digital time and date labels
time_label = Label(
    app,
    bg="#393E46",
    fg="#00FFF5",
    font=("DS-Digital", 36, "bold"),
    relief='flat'
)
time_label.place(x=center_x, y=center_y-30, anchor="center")

date_label = Label(
    app,
    bg="#393E46",
    fg="#FFD369",
    font=("Helvetica", 14, "bold"),
    relief='flat'
)
date_label.place(x=center_x, y=center_y+30, anchor="center")

def update_time():
    current_time = time.strftime("%H:%M:%S")
    current_date = time.strftime("%A, %d %B %Y")
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    app.after(1000, update_time)

draw_clock_face()
update_time()
app.mainloop()