#!/usr/bin/python
# Filename : mwitTest.py

import Tkinter as tk
import ttk

HOST = "192.168.0.222"

class MWITApp(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        master.title("GDC : MTIT")
        self.parent = master
        self.pack(fill=tk.BOTH, expand=1)
        
        s = ttk.Style()
        s.configure("Treeview", borderwidth=1)
        s.map("ReadOnly.TEntry", background=[("readonly", "grey")])

        panel = ttk.PanedWindow(self, orient=tk.HORIZONTAL)
        panel.pack(fill=tk.BOTH, expand=1, padx=5, pady=5)
        
        frame_1 = self.frameL = ttk.Frame(panel)
        panel.add(frame_1)
#        frame_1.columnconfigure(2, weight=1)
#        frame_1.rowconfigure(1, weight=1)

        self.host = tk.StringVar()
        self.host.set(HOST)

        ttk.Label(frame_1, text="Host:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        entry_host = self.__entryHost = ttk.Entry(frame_1, width=15, textvariable=self.host)
        entry_host.grid(row=0, column=1, sticky=tk.W)
        button_loadlocal = self.buttonLoadLocal = ttk.Button(frame_1, text="Load Local")
        button_loadlocal.grid(row=0, column=2, sticky=tk.W)
        button_loadUSB = self.buttonLoadUSB = ttk.Button(frame_1, text="Load USB")
        button_loadUSB.grid(row=0, column=3, sticky=tk.W)



if __name__ == "__main__":
    root = tk.Tk()
    app = MWITApp(root)
    root.mainloop()
