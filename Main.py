import tkinter as tk
from tkinter import filedialog

def verifier_bgm(lines, text_widget):
    for idx, line in enumerate(lines):
        if line.startswith("BGM"):
            parts = line.strip().split('+')
            if len(parts) < 4:
                # surligner la ligne en rouge
                start = f"{idx + 1}.0"
                end = f"{idx + 1}.end"
                text_widget.tag_add("erreur", start, end)

def ouvrir_fichier():
    fichier = filedialog.askopenfilename(title="Choisir un fichier EDI")
    if fichier:
        with open(fichier, "r", encoding="utf-8") as f:
            lignes = f.readlines()
            texte.delete("1.0", tk.END)  # vider le widget texte
            texte.insert(tk.END, ''.join(lignes))  # insérer le contenu
            verifier_bgm(lignes, texte)


fenetre = tk.Tk()
fenetre.title("EDI Inspector")

btn_ouvrir = tk.Button(fenetre, text="Ouvrir un fichier EDI", command=ouvrir_fichier)
btn_ouvrir.pack(pady=10)

texte = tk.Text(fenetre, wrap="none", height=30, width=100)
texte.pack()
########################################################################################
# Configuration du tag de mise en évidence
########################################################################################
texte.tag_config("erreur", background="red", foreground="white")

fenetre.mainloop()
