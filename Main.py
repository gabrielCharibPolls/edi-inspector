# main.py
import tkinter as tk
from tkinter import filedialog,ttk, messagebox
from verifier_bgm import BGMVerifier
from tooltip import TooltipHandler

class EDIInspectorApp:
    def __init__(self):
        self.fenetre = tk.Tk()
        ################################################################
        #todo : rajouter une icone
        # rajouter le nom de fichier avant EDI inspector
        ############################################################
        self.fenetre.title("EDI Inspector")

        self.bgm_verifier = BGMVerifier()
        self.tooltip_handler = TooltipHandler(self.fenetre)


        self.setup_interface()

    def setup_interface(self):
        #btn_ouvrir = tk.Button(self.fenetre, text="Ouvrir un fichier EDI", command=self.ouvrir_fichier)
        #btn_ouvrir.pack(pady=10)

        self.texte = tk.Text(self.fenetre, wrap="none", height=30, width=100)
        self.texte.pack()

        self.texte.tag_config("erreur", background="red", foreground="white")
        self.texte.tag_config("correct", background="lightgreen")
    #######################################################################################################
    # Menu structure 
    # ---------------------------------------------------
    # Fichier    Edition    Format    Affichage    Aide
    # ---------------------------------------------------
    # Ouvrir     Annuler    Police... Zoom         Aide
    # Fermer     Couper                Barre       À propos de...
    # Enregistrer sous... Copier                 
    #             Coller
    #             Supprimer
    ########################################################################################################
        menu_bar = tk.Menu(self.fenetre)

        #TODO: rajouter des raccourcis clavier pour les boutons
    

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Ouvrir", command=self.ouvrir_fichier)
        file_menu.add_command(label="Fermer", command=self.fenetre.quit)
        file_menu.add_command(label="Enregistrer sous...", command=self.enregistrer_sous)
        menu_bar.add_cascade(label="Fichier", menu=file_menu)

        edit_menu = tk.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Annuler")
        edit_menu.add_command(label="Couper")
        edit_menu.add_command(label="Copier")
        edit_menu.add_command(label="Coller")
        edit_menu.add_command(label="Supprimer")
        menu_bar.add_cascade(label="Edition", menu=edit_menu)

 
        format_menu = tk.Menu(menu_bar, tearoff=0)
        format_menu.add_command(label="Police...")
        menu_bar.add_cascade(label="Format", menu=format_menu)

        view_menu = tk.Menu(menu_bar, tearoff=0)
        view_menu.add_command(label="Zoom")
        view_menu.add_command(label="Barre d'état")
        menu_bar.add_cascade(label="Affichage", menu=view_menu)

        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="Aide")
        help_menu.add_command(label="À propos de...")
        menu_bar.add_cascade(label="Aide", menu=help_menu)

        # Attach the menu bar to the window
        self.fenetre.config(menu=menu_bar)
        self.fenetre.mainloop()

        ################################################################################################
        #todo : rajouter un ckeck tout les secondepour savoir si le fichier à été modifié
        #si c'est le cas, demander à l'utilisateur s'il veut recharger le fichier ou pas
        ################################################################################################
    
    def enregistrer_sous(self):
        fichier = filedialog.asksaveasfilename(title="Enregistrer sous", defaultextension=".txt",
        filetypes=[("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")])
        if fichier:
            with open(fichier, "w", encoding="utf-8") as f:
                contenu = self.texte.get("1.0", tk.END).strip()
                f.write(contenu)

    def ouvrir_fichier(self):
        fichier = filedialog.askopenfilename(title="Choisir un fichier EDI")
        if fichier:
            with open(fichier, "r", encoding="utf-8") as f:
                lignes = f.readlines()
                self.texte.delete("1.0", tk.END)  # vider le widget texte
                self.texte.insert(tk.END, ''.join(lignes))  # insérer le contenu
                ## Appel de la méthode de vérification a chaque ligne 
                
                self.bgm_verifier.verifier_bgm(lignes, self.texte)
                self.texte.tag_bind("erreur", "<Enter>", lambda event: self.tooltip_handler.show_tooltip(event, "Erreur détectée"))

if __name__ == "__main__":
    app = EDIInspectorApp()
