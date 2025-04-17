# main.py
import tkinter as tk
from tkinter import filedialog
from verifier_bgm import BGMVerifier
from tooltip import TooltipHandler

class EDIInspectorApp:
    def __init__(self):
        self.fenetre = tk.Tk()
        self.fenetre.title("EDI Inspector")

        self.bgm_verifier = BGMVerifier()
        self.tooltip_handler = TooltipHandler(self.fenetre)


        self.setup_interface()

    def setup_interface(self):
        btn_ouvrir = tk.Button(self.fenetre, text="Ouvrir un fichier EDI", command=self.ouvrir_fichier)
        btn_ouvrir.pack(pady=10)

        self.texte = tk.Text(self.fenetre, wrap="none", height=30, width=100)
        self.texte.pack()

        self.texte.tag_config("erreur", background="red", foreground="white")
        self.texte.tag_config("correct", background="lightgreen")

        self.fenetre.mainloop()

    def ouvrir_fichier(self):
        fichier = filedialog.askopenfilename(title="Choisir un fichier EDI")
        if fichier:
            with open(fichier, "r", encoding="utf-8") as f:
                lignes = f.readlines()
                self.texte.delete("1.0", tk.END)  # vider le widget texte
                self.texte.insert(tk.END, ''.join(lignes))  # insérer le contenu
                self.bgm_verifier.verifier_bgm(lignes, self.texte)
                self.texte.tag_bind("erreur", "<Enter>", lambda event: self.tooltip_handler.show_tooltip(event, "Erreur détectée"))

if __name__ == "__main__":
    app = EDIInspectorApp()
