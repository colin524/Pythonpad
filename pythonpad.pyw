import pyautogui
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import subprocess
import os
import tkinter.font as tkFont

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Pythonpad")
        self.master.iconbitmap('C:/Users/ColinDuperron/icon.ico')
        self.master.geometry("1200x700")
        self.file_path = None
        # Create a notebook to display tabs
        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(fill="both", expand=True)
        tabs = 0
        self.tab_dict = {}
        self.add_tab()
        # Create a label for the status bar
        self.style = ttk.Style()
        self.style.theme_use('vista')

        # Function to update the status bar

        def satan(self):
            messagebox.showerror("666", "Mauvaise idée... Apres si tu veut... Bon courage...")
            root.destroy()
        def fortnite(self):
            messagebox.showwarning("ALERTE", "ALERTE : Fortinite kid détécté ! VOus allez etre viré !")
            root.destroy()
        def mib(self):
            messagebox.showerror("MIB", "TOI TAIT TOI (neurolaser)")
            self.notebook.delete("1.0", tk.END)
        def ph(self):
            messagebox.showerror("C'est pas bien", "Euhhhhhhhhhhh, a eviter ; merci, au revoir")
            root.destroy()
        def dame(self):
            messagebox.showerror("Dame blanche est tu la ? ", "Dame blanche est tu la ? Dame blanche est tu la ? Dame blanche est tu la ? Dame blanche est tu la ? Dame blanche est tu la ?")
            messagebox.showerror("oui....", "NON, AU SECOURS, AHHHHHHHHHHHHHHH")
            messagebox.showerror("Dame blanche", "(dead) ne pas reproduire chez soit... au revoiiiiiiiir....")
            root.destroy()

        def quitter(self):
            rep = messagebox.askyesno("Pythonpad", "Voulez-vous vraiment quitter Pythonpad sans sauvegarder ?")
            if rep == True:
                root.destroy()
            else:
                self.notebook.delete("1.0", tk.END)
        



        # Bind the update_status_bar function to the text box
        # Create a menu bar
        menu_bar = tk.Menu(self.master)
        self.master.config(menu=menu_bar)

        submenu = tk.Menu(self.master, tearoff=0)
        submenu.add_command(label="Enregister et fermer", command=self.save_close)
        submenu.add_command(label="Fermer sans enregistrer", command=self.close_current)


        # Create file menu
        self.file_menu = tk.Menu(self.master, tearoff=0)
        self.file_menu.add_command(label="Nouveau", command=self.add_tab)
        self.file_menu.add_command(label="Ouvrir", command=self.open_file)
        self.file_menu.add_command(label="Enregistrer", command=self.save_file)
        self.file_menu.add_command(label="Enregistrer sous", command=self.save_as)
        self.file_menu.add_separator()
        self.file_menu.add_cascade(label="Fermer l'onglet", menu=submenu)
        self.file_menu.add_command(label="Fermer tout", command=self.on_closing)

        # Create edit menu
        self.edit_menu = tk.Menu(self.master, tearoff=0)
        self.edit_menu.add_command(label="Copier", command=self.copy_text)
        self.edit_menu.add_command(label="Coller", command=self.paste_text)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Rechercher", command=self.dev)
        self.edit_menu.add_command(label="Remplacer", command=self.dev)

        self.py_menu = tk.Menu(self.master, tearoff=0)
        self.py_menu.add_command(label="Enregistrer en Python", command=self.save_py)
        self.py_menu.add_command(label="Executer en tant que code Python", command=self.run)
        self.py_menu.add_command(label="Executer en *.pyw (Sans CLI)", command=self.run_pyw)

        self.autre_menu = tk.Menu(self.master, tearoff=0)
        self.autre_menu.add_command(label="Paramètres", command=self.settings)
        self.autre_menu.add_command(label="A propos", command=self.display_about)
        

        # Add menus to menu bar
        self.menu_bar = tk.Menu(self.master)
        self.menu_bar.add_cascade(label="Fichier", menu=self.file_menu)
        self.menu_bar.add_cascade(label="Modifier", menu=self.edit_menu)
        self.menu_bar.add_cascade(label="Python", menu=self.py_menu)
        self.menu_bar.add_cascade(label="Autres", menu=self.autre_menu)
        self.master.config(menu=self.menu_bar)

    def settings(self):
    
            settings = tk.Toplevel(root)
            settings.title("Paramètres - Pythonpad")
            settings.iconbitmap('C:/Users/ColinDuperron/icon.ico')
            
    
            width = 500
            height = 300

            # Get the screen width and height
            screen_width = settings.winfo_screenwidth()
            screen_height = settings.winfo_screenheight()

            # Calculate the x and y coordinates to center the window
            x = (screen_width // 2) - (width // 2)
            y = (screen_height // 2) - (height // 2)

            # Set the geometry of the window
            settings.geometry(f"{width}x{height}+{x}+{y}")
            settings.resizable(False, False)
        
            about_label = tk.Label(settings, text="Ce logiciel a été créer par Colin 524")
            about_label.pack()

            about_label2 = tk.Label(settings, text="2023 - Touts droits réservés")
            about_label2.pack()

            about_button = ttk.Button(settings, text="Fermer", command=settings.destroy)
            about_button.pack()



    def dev(self):
            messagebox.showerror("Pythonpad", "Cette fonctionnalité est en cours de dévloppement et sera disponible prochainement")


    def add_tab(self, filename=None, event=None):
        # Create a new tab with a text box
        frame = ttk.Frame(self.notebook)
        text_box = tk.Text(frame)
        text_box.pack(fill="both", expand=True)
        self.notebook.add(frame, text=filename if filename else "Sans titre")

        # Bind a function to the closing of the tab
        self.notebook.bind("<Button-3>", self.focus_tab)
        self.notebook.bind("<Button-2>", self.close_tab)
        self.notebook.bind("<Shift-Button-3>", self.close_tab)
        self.notebook.bind("<Shift-Button-1>", self.focus_tab)
        text_box.bind("<Button-3>", self.show_popup_menu)
        text_box.bind("<Control-s>", self.save_file)
        text_box.bind("<Control-n>", self.add_tab_n)
        text_box.bind("<Control-o>", self.open_file)
        text_box.bind("<Control-w>", self.exit)

    def add_tab_n(self, filename=None, event=None):
        # Create a new tab with a text box
        frame = ttk.Frame(self.notebook)
        text_box = tk.Text(frame)
        text_box.pack(fill="both", expand=True)
        self.notebook.add(frame, text="Sans titre")
        self.tab_dict[text_box] = None
        old_index = self.notebook.index("current")
        self.notebook.select(old_index)

        # Bind a function to the closing of the tab
        self.notebook.bind("<Button-3>", self.focus_tab)
        self.notebook.bind("<Button-2>", self.close_tab)
        self.notebook.bind("<Shift-Button-3>", self.close_tab)
        self.notebook.bind("<Shift-Button-1>", self.focus_tab)
        text_box.bind("<Button-3>", self.show_popup_menu)
        text_box.bind("<Control-s>", self.save_file)
        text_box.bind("<Control-n>", self.add_tab)
        text_box.bind("<Control-o>", self.open_file)
        text_box.bind("<Control-w>", self.exit)


    def focus_tab(self, event):
        old_index = self.notebook.index("current")
        index = self.notebook.index("@%d,%d" % (event.x, event.y))
        if index != -1:
            self.notebook.select(index)
            # Show a popup menu when the right mouse button is clicked
            popup_menu = tk.Menu(self.master, tearoff=0)
            popup_menu.add_command(label="Nouveau document", command=self.add_tab)
            if old_index != index:
                popup_menu.add_command(label="Enregister", command=self.save_file)
                popup_menu.add_command(label="Enregister sous", command=self.save_as)
            popup_menu.add_command(label="Enregister et fermer", command=self.save_close)
            popup_menu.add_command(label="Fermer sans enregistrer", command=self.close_current)
            popup_menu.add_command(label="Annuler")
            popup_menu.tk_popup(event.x_root, event.y_root)

    
    def show_popup_menu(self, event):
        # Show a popup menu when the right mouse button is clicked
        popup_menu = tk.Menu(self.master, tearoff=0)
        popup_menu.add_command(label="Couper", command=lambda: event.widget.event_generate("<<Cut>>"))
        popup_menu.add_command(label="Copier", command=lambda: event.widget.event_generate("<<Copy>>"))
        popup_menu.add_command(label="Coller", command=lambda: event.widget.event_generate("<<Paste>>"))
        popup_menu.add_separator()
        popup_menu.add_command(label="Enregister et fermer", command=self.save_close)
        popup_menu.add_command(label="Fermer sans enregistrer", command=self.close_current)
        popup_menu.tk_popup(event.x_root, event.y_root)

    def show_tab_menu(self, event):
        tab_index = self.notebook.index("@%d,%d" % (event.x, event.y))
        current_tab_index = self.notebook.index("current")
        if tab_index == current_tab_index:
                # Show a popup menu when the right mouse button is clicked
                popup_menu = tk.Menu(self.master, tearoff=0)
                popup_menu.add_command(label="Enregister et fermer", command=self.save_close)
                popup_menu.add_command(label="Fermer sans enregistrer", command=self.close_current)
                popup_menu.add_command(label="Annuler")
                popup_menu.tk_popup(event.x_root, event.y_root)
        else:
                # Show a popup menu when the right mouse button is clicked
                popup_menu = tk.Menu(self.master, tearoff=0)
                popup_menu.add_command(label="Enregister et fermer", state="disabled")
                popup_menu.add_command(label="Fermer sans enregistrer", state="disabled")
                popup_menu.add_command(label="Annuler")
                popup_menu.tk_popup(event.x_root, event.y_root)



    def run(self):
        full = tk.Toplevel(root)
        full.attributes('-fullscreen', True)
        full.attributes('-alpha', 0.5)
        full.wm_title("Execution de code • Pythonpad")
        full.iconbitmap('C:/Users/ColinDuperron/icon.ico')
        full.wm_attributes("-topmost", 1)
        frame = tk.Frame(full, bg="#000000") # Black background frame to display widgets over it
        frame.pack(fill="both", expand=True)
        rep = messagebox.askyesno("Executer - Pythonpad", "Voulez-vous executer ce code ? \nATTENTION : N'executez JAMAIS de code téléchargé sur intenet sans faire une analyse antivirus, cela peut avoir des conséquences sur vos fichiers.", icon='warning', default=messagebox.NO, parent=full)
        if rep == True:
                full.destroy()
                # Get the code from the text box
                current_tab_index = self.notebook.index("current")
                
                # If the current tab is a file, save the contents to the file
                code = self.notebook.winfo_children()[current_tab_index].winfo_children()[0]
                with open("temp.py", "w") as f:
                        f.write(code.get("1.0", "end-1c"))

                # Run the code
                subprocess.Popen(["python", "temp.py"])
        else:
            full.destroy()

    def run_pyw(self):
        full2 = tk.Toplevel(root)
        full2.attributes('-fullscreen', True)
        full2.attributes('-alpha', 0.5)
        full2.wm_title("Execution de code • Pythonpad")
        full2.iconbitmap('C:/Users/ColinDuperron/icon.ico')
        full2.wm_attributes("-topmost", 1)
        frame = tk.Frame(full2, bg="#000000") # Black background frame to display widgets over it
        frame.pack(fill="both", expand=True)
        rep = messagebox.askyesno("Executer - Pythonpad", "Voulez-vous executer ce code en mode sans CLI? \nATTENTION : N'executez JAMAIS de code téléchargé sur intenet sans faire une analyse antivirus, encore moins du code pyw (sans CLI), cela peut avoir des conséquences sur vos fichiers.", icon='warning', default=messagebox.NO, parent=full2)
        if rep == True:
                full2.destroy()
                # Get the code from the text box
                current_tab_index = self.notebook.index("current")
                
                # If the current tab is a file, save the contents to the file
                code = self.notebook.winfo_children()[current_tab_index].winfo_children()[0]
                with open("temp.pyw", "w") as f:
                        f.write(code.get("1.0", "end-1c"))

                # Run the code
                subprocess.Popen(["python", "temp.pyw"])
        else:
            full2.destroy()


    def close_tab(self, event):
        # Get the index of the tab that was clicked
        tab_index = self.notebook.index("@%d,%d" % (event.x, event.y))

        # If the user clicked on a tab, remove it
        if tab_index != -1:
            self.notebook.forget(tab_index)
            self.show_info()

    def show_info(self, event=None):
        info_window = tk.Toplevel(root)
        # Remove title bar
        info_window.overrideredirect(True)
        info_window.wm_attributes("-topmost", 1)


        # Get screen width and height
        screen_width = info_window.winfo_screenwidth()
        screen_height = (info_window.winfo_screenheight() - 10)

        # Set window size and position
        width = 205
        height = 50
        x = (screen_width - width) // 2
        y = screen_height - height
        info_window.geometry(f"{width}x{height}+{x}+{y}")

        info_label = tk.Label(info_window, text="Onglet fermé   ")
        info_label.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
        button = ttk.Button(info_window, text="  Annuler  ", command=self.show_info)
        button.grid(row=1, column=2, padx=5, pady=5, sticky=tk.W)
        root.after(5000, info_window.destroy) # destroy the window after 10 seconds



    def close_current(self, event=None):
        # Get the index of the tab that was clicked
        tab_index = self.notebook.index("current")

        # If the user clicked on a tab, remove it
        if tab_index != -1:
            self.notebook.forget(tab_index)

    def erase(self):
        response = messagebox.askyesno("Attention - Pythonpad", "Voulez-vous effacer tout le contenu du document ? Une fois le contenu effacé et le fichier enregistré, cette action est irrevesible !", icon='warning')
        if response == True:
                text_box = self.notebook.winfo_children()[-1].winfo_children()[0]
                text_box.delete("1.0", tk.END)

    def on_closing(self):
            # Ask the user if they want to close the window
            rep = messagebox.askyesno("Pythonpad", "Voulez-vous vraiment quitter Pythonpad ? \nTouts les fichiers non enregistés seront perdus.", icon="warning", default=messagebox.NO)
            if rep == True:
                self.master.destroy()
    
    def copy_text(self):
        self.master.clipboard_clear()
        self.master.clipboard_append(self.notebook.selection_get())

    def paste_text(self):
        self.notebook.insert("insert", self.master.clipboard_get())

    def new_file(self):
        if messagebox.askyesno("Pythonpad", "Voulez-vous créer un nouveau fichier ? Toute modification non enregistrée sera perdue."):
            self.filename = None
            self.notebook.delete("1.0", tk.END)
            self.master.title("Sans titre - Pythonpad")
    def display_about(self):
        about_window = tk.Toplevel(root)
        about_window.title("About")
        about_window.attributes("-toolwindow", "1")
        
        about_label = tk.Label(about_window, text="Ce logiciel a été créer par Colin 524")
        about_label.pack()

        about_label2 = tk.Label(about_window, text="2023 - Touts droits réservés")
        about_label2.pack()

        about_button = ttk.Button(about_window, text="Fermer", command=about_window.destroy)
        about_button.pack()


        # Center the window on the screen
        about_window.geometry("+%d+%d" % (root.winfo_rootx() + 50, root.winfo_rooty() + 50))

    def a_propos(self):
        messagebox.showinfo("A propos - Pythonpad", "Ce logiciel a été créer entierement par Colin 524. Touts droits réservés")
    def nouveau(self):
        if messagebox.askyesno("Pythonpad", "Voulez-vous créer un nouveau fichier ? Toute modification non enregistrée sera perdue."):
            self.notebook.delete("1.0", tk.END)


    def exit(self, event=None):
        current_tab_index = self.notebook.index("current")

        # If the current tab is a file, save the contents to the file
        if self.notebook.tab(current_tab_index, "text") != "Sans titre":
                response = tk.messagebox.askyesno("Pythonpad", "Les modifications n'ont peut-être pas été enregistrées. Voulez-vous fermez cet onglet quand même ? ")
                if response == tk.YES:
                    self.close_current()
        # Otherwise, prompt the user to select a filename to save to
        else:
            response = tk.messagebox.askyesno("Pythonpad", "Le fichier n'a pas été enregistré. Voulez-vous fermez cet onglet quand même ? ")
            if response == tk.YES:
                    self.close_current()



    def open_file(self, event=None):
        # Open a file dialog to select a file to open
        filename = filedialog.askopenfilename(title = "Ouvrir le fichier dans un nouvel onglet • Pythonpad", defaultextension=".txt", filetypes=[("Fichiers supportés", ("*.txt", "*.py", "*.pyw", "*.bat", "*.vbs"))])

        # If a file was selected, create a new tab with the file contents
        if filename:
            with open(filename, "r") as f:
                contents = f.read()
            self.add_tab(filename=filename)
            text_box = self.notebook.winfo_children()[-1].winfo_children()[0]
            text_box.insert("1.0", contents)
    def save_file(self, event=None):
        # Get the index of the current tab
        current_tab_index = self.notebook.index("current")

        # If the current tab is a file, save the contents to the file
        if self.notebook.tab(current_tab_index, "text") != "Sans titre":
            filename = self.notebook.tab(current_tab_index, "text")
            text_box = self.notebook.winfo_children()[current_tab_index].winfo_children()[0]
            with open(filename, "w") as f:
                f.write(text_box.get("1.0", "end-1c"))
                info_window = tk.Toplevel(root)
                # Remove title bar
                info_window.overrideredirect(True)
                info_window.wm_attributes("-topmost", 1)

                my_font = tkFont.Font(family='Helvetica', size=10, weight='normal')
                text = ("✔ Fichier enregistré a " + filename)
                width = my_font.measure(text)


                # Get screen width and height
                screen_width = info_window.winfo_screenwidth()
                screen_height = (info_window.winfo_screenheight() - 10)

                # Set window size and position
                height = 40
                x = (screen_width - width) // 2
                y = screen_height - height
                info_window.geometry(f"{width}x{height}+{x}+{y}")

                info_label = tk.Label(info_window, text=("✔ Fichier enregistré a " + filename))
                info_label.grid(row=1, column=1, padx=5, pady=5)
                root.after(5000, info_window.destroy) # destroy the window after 10 seconds



        # Otherwise, prompt the user to select a filename to save to
        else:
            filename = filedialog.asksaveasfilename(title = "Enregistrer le fichier actuel • Pythonpad", defaultextension=".txt", filetypes=[("Fichiers texte", "*.txt"), ("Fichier Python", "*.py"), ("Fichier Python (sans CLI)", "*.pyw"), ("Fichier de commande Windows", "*.bat"), ("Fichier VBS", "*.vbs"), ("Autres fichiers", "*")])
            if filename:
                text_box = self.notebook.winfo_children()[current_tab_index].winfo_children()[0]
                with open(filename, "w") as f:
                    f.write(text_box.get("1.0", "end-1c"))
                self.notebook.tab(current_tab_index, text=filename)
                info_window = tk.Toplevel(root)
                # Remove title bar
                info_window.overrideredirect(True)
                info_window.wm_attributes("-topmost", 1)


                # Get screen width and height
                screen_width = info_window.winfo_screenwidth()
                screen_height = (info_window.winfo_screenheight() - 10)

                # Set window size and position
                width = 805
                height = 40
                x = (screen_width - width) // 2
                y = screen_height - height
                info_window.geometry(f"{width}x{height}+{x}+{y}")

                info_label = tk.Label(info_window, text=("Fichier enregistré a " + filename))
                info_label.grid(row=1, column=1, padx=5, pady=5)
                root.after(5000, info_window.destroy) # destroy the window after 10 seconds


        
     

    def save_as(self):
        # Get the index of the current tab
        current_tab_index = self.notebook.index("current")
        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Fichiers texte", "*.txt"), ("Fichier Python", "*.py"), ("Fichier Python (sans CLI)", "*.pyw"), ("Fichier de commande Windows", "*.bat"), ("Fichier VBS", "*.vbs"), ("Autres fichiers", "*")])
        if filename:
                text_box = self.notebook.winfo_children()[current_tab_index].winfo_children()[0]
                with open(filename, "w") as f:
                    f.write(text_box.get("1.0", "end-1c"))
                self.notebook.tab(current_tab_index, text=filename)
    def save_close(self):
                # Get the index of the current tab
                current_tab_index = self.notebook.index("current")

                # If the current tab is a file, save the contents to the file
                if self.notebook.tab(current_tab_index, "text") != "Sans titre":
                        filename = self.notebook.tab(current_tab_index, "text")
                        text_box = self.notebook.winfo_children()[current_tab_index].winfo_children()[0]
                        with open(filename, "w") as f:
                                f.write(text_box.get("1.0", "end-1c"))

                
                else:
                    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Fichiers texte", "*.txt"), ("Fichier Python", "*.py"), ("Fichier Python (sans CLI)", "*.pyw"), ("Fichier de commande Windows", "*.bat"), ("Fichier VBS", "*.vbs"), ("Autres fichiers", "*")])
                if filename:
                        text_box = self.notebook.winfo_children()[current_tab_index].winfo_children()[0]
                        with open(filename, "w") as f:
                                f.write(text_box.get("1.0", "end-1c"))
                        self.notebook.tab(current_tab_index, text=filename)

                # If the user clicked on a tab, remove it
                if current_tab_index != -1:
                    self.notebook.forget(current_tab_index)

    def save_py(self):
        # Get the index of the current tab
        current_tab_index = self.notebook.index("current")
        filename = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python", "*.py"), ("Python (sans CLI)", "*.pyw")])
        if filename:
                text_box = self.notebook.winfo_children()[current_tab_index].winfo_children()[0]
                with open(filename, "w") as f:
                    f.write(text_box.get("1.0", "end-1c"))
                self.notebook.tab(current_tab_index, text=filename)
                self.master.title("Pythonpad")
                
    def save_and_quit(self):
        if self.file_path:
            with open(self.file_path, "w") as file:
                file.write(self.notebook.get("1.0", tk.END))
                root.destroy()
        else:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt")
            if file_path:
                self.file_path = file_path
                with open(file_path, "w") as file:
                    file.write(self.notebook.get("1.0", tk.END))
                self.master.title(file_path + " - Pythonpad")
                root.destroy()


root = tk.Tk()
app = App(root)
def on_closing():
    # Ask the user if they want to close the window
    rep = messagebox.askyesno("Pythonpad", "Voulez-vous vraiment quitter Pythonpad ? \nTouts les fichiers non enregistés seront perdus.", icon="warning", default=messagebox.NO)
    if rep == True:
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.configure(background='white')
root.mainloop()
