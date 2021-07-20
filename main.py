from pyqrcode import *
import tkinter
from PIL import Image

root = tkinter.Tk()
root.title("Qrcode Generator")
app_width = 375
app_height = 410
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 3) - (app_width / 6)
y = (screen_height / 8) - (app_height / 10)
root.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
name = tkinter.Entry(root)

f = ("Cambria", 20) # font family is "tahoma", font size "15", font type "bold"
death_font = ("Death Hector", 20)
cambria_font = ("Cambria", 13, "bold")

# generate new qr code
def generate_qr():
    global datas
    datas = name.get()
    datas = create(datas)
    datas.png("images/qr.png", scale = 8)
    test = datas.xbm(scale = 5)
    global xbm_image
    xbm_image = tkinter.BitmapImage(data = test, foreground = "blue", background = "pink")
    image_view.config(image = xbm_image)
    statement.config(text = "this qrcode containing: " + str(name.get()))
    note.config(text = "Scan the Qr code now!")
    scanbtn.config(text = "Scan")
    scanbtn.grid(row = 6, column = 0, columnspan = 2, pady = 3)

# new window
def new_window():
    top = tkinter.Toplevel()
    top.title("Qrcode Scanner")
    from pyzbar.pyzbar import decode
    note = tkinter.Label(top, text = "Qrcode contains: ", font = cambria_font).pack()

    # For scanning qrcode and print to the console/window
    decode = decode(Image.open("images/qr.png"))
    contain = decode[0].data.decode("ascii")
    data = tkinter.Label(top, text = contain, font= cambria_font,  bg = "gray").pack()


# functionalities
heading = tkinter.Label(root, text = "Qr code Generator", font = death_font, bg = "gray")
subtitle = tkinter.Label(root, text = "Enter the data below", font = cambria_font)
make_button = tkinter.Button(root, text = "Generate", font= cambria_font, bg = "orange", command = generate_qr) 
image_view = tkinter.Label(root)
statement = tkinter.Label(root)
note = tkinter.Label(root)
scanbtn = tkinter.Button(root, text = "Scan", font= cambria_font, bg = "green", command = new_window)

# gui grid
heading.grid(row = 0, column = 0, columnspan = 2)
subtitle.grid(row = 1, column = 0, columnspan = 2, pady = 2)
name.grid(row = 2, column = 0, columnspan = 2, pady = 2)
make_button.grid(row = 3, column = 0, columnspan = 2, pady = 5)
image_view.grid(row = 4, column = 0, columnspan = 2)
note.grid(row = 5, column = 0, columnspan = 2, pady = 3)

root.mainloop()