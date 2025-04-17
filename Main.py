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
                # Ajouter un ToolTip pour afficher un message d'erreur
                def show_tooltip(event):
                    # Créer un tooltip à la position de la souris
                    # todo :Vérifier si le tooltip existe déjà pour éviter les doublons
                    # utiliser un bolean pour savoir si le tooltip existe déjà
                    # si oui, ne pas créer un nouveau tooltip
                    # sinon, créer un nouveau tooltip
                    # Créer un tooltip à la position de la souris               
                    tooltip = tk.Toplevel()
                    tooltip.wm_overrideredirect(True)
                    tooltip.geometry(f"+{event.x_root + 10}+{event.y_root + 10}")
                    label = tk.Label(tooltip, text="Erreur dans la ligne BGM", background="yellow", relief="solid", borderwidth=1)
                    label.pack()
                    # Supprimer le tooltip après un délai
                    label.after(800, tooltip.destroy)

                text_widget.tag_bind("erreur", "<Enter>", show_tooltip)
            else:
                print("Ligne BGM correcte")
                # cas où la ligne BGM est correcte
                # surligner la ligne en vert    
                start = f"{idx + 1}.0"
                end = f"{idx + 1}.end"
                text_widget.tag_add("correct", start, end)
                    
           
                    
                  



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
texte.tag_config("correct", background="lightgreen")

fenetre.mainloop()
