import hashlib
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
class Checks:
    def AskForFile(self):
        file_path = filedialog.askopenfilename()
        return file_path
    def CalculateChecksums(self, file_path):
        hash_func = hashlib.new("sha256")
        with open(file_path, "rb") as file:
            while chunk := file.read(8192):
                hash_func.update(chunk)
        return hash_func.hexdigest()
class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("CheckSum Verifier")
        self.window.geometry("500x300")  # Larger window size
        self.window.configure(bg="#202020")  # Dark background color
        self.window.option_add("*TButton*highlightBackground", "#404040")  # Darker button color
        self.window.option_add("*TButton*highlightColor", "#404040")
        
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Helvetica", 16))  # Larger font
        self.style.configure("TLabel", font=("Helvetica", 16, "bold"), foreground="#ffffff", background="#202020")
        self.style.configure("TEntry", font=("Helvetica", 16), foreground="#000000", background="#ffffff")
        
        self.b1 = ttk.Button(self.window, text="Start!", command=self.AskForCheckSum)
        self.b1.pack(pady=50)
        self.window.mainloop()
        
    def AskForCheckSum(self):
        self.ck = Checks()
        location = self.ck.AskForFile()
        self.b1.destroy()
        self.checksum = self.ck.CalculateChecksums(location)
        
        self.label = ttk.Label(self.window, text="Enter Checksum:", style="TLabel")
        self.label.pack(pady=15)
        
        self.e1 = ttk.Entry(self.window, style="TEntry", width=64)  # Wider entry field
        self.e1.pack(pady=20)
        
        self.b2 = ttk.Button(self.window, text="Submit Checksum", command=self.ShowChecksumInfo)
        self.b2.pack(pady=20)
        
    def ShowChecksumInfo(self):
        UserChecksum = self.e1.get().replace(" ", "")
        if UserChecksum == self.checksum:
            messagebox.showinfo("FileChecksumInfo", "The file has the same checksum as the one you provided")
        else:
            messagebox.showerror("WARNING", "WARNING! The file has been tampered with")
        self.window.destroy()

if __name__ == "__main__":
    g = GUI()
