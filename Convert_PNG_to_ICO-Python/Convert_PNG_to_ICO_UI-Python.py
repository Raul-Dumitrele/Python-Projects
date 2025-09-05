import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

# Initialize Tkinter window
root = tk.Tk()
img=None

font=('helvetica',12,'bold')
bg='blue'
fg='white'
width=15

def getPNG():
    '''Function to get png image location and open it with pillow'''
    global img
    import_file_path = tk.filedialog.askopenfilename(filetypes=[("PNG File",'.png')])
    if import_file_path:    # only if a file was selected
        img = Image.open(import_file_path)
def convertToICO():
    '''Function to convert image from png to ico format with pillow and save to user specified location'''
    global img
    if img is None:
        tk.messagebox.showerror("Error","No File Selected")
    else:
        export_file_path= tk.filedialog.asksaveasfilename(defaultextension='.ico')
        if export_file_path:  # only if choose save location
            img.save(export_file_path, format='ICO')
            messagebox.showinfo("Success", "Image converted and saved successfully!")
    
# Set the window title
root.title('PNG to ICO Converter')
canvas1 = tk.Canvas(root, width=500, height=350, bg='lightblue')
canvas1.pack()

# Set the screen title
label1 = tk.Label(root, text='PNG to ICO Converter', bg='lightblue')
label1.config(font=('helvetica', 20))
canvas1.create_window(250, 100, window=label1)

# Browse button to browse for image
browseButton = tk.Button(text="Import PNG File", command=getPNG, bg=bg, fg=fg, font=font, width=width)
canvas1.create_window(250, 150, window=browseButton)

# Convert button to convert selected image and save
saveAsButton = tk.Button(text='Convert PNG to ICO', command=convertToICO, bg=bg, fg=fg, font=font, width=width)
canvas1.create_window(250, 200, window=saveAsButton)
root.mainloop()


