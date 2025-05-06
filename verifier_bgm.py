class BGMVerifier:
###############################################################
## BGM Verifier
## ce code est un module de vérification de la syntaxe des lignes
## BGM dans un fichier EDI (EDI = Electronic Data Interchange).
#IL est aussi les type de document EDI :
#380 = Facture
#351 = Bon de livraison
#384 = Bon de commande
#si c'est pas un de ces trois types, il y a une erreur
###############################################################
    VALID_DOCUMENT_TYPES = {380, 351, 384}

    def verifier_bgm(self, lines, text_widget):
        for idx, line in enumerate(lines):
            if not line.startswith("BGM"):
                continue
            if self.est_ligne_bgm_valide(line):
                self.highlight_line(text_widget, idx, "correct")
            else:
                self.highlight_line(text_widget, idx, "erreur")

                

    def est_ligne_bgm_valide(self, line):
        #verifier la longeur de la ligne
        parts = line.strip().split('+')

        if len(parts) < 4:
            return False

        try:
            type_document_str = parts[1].split(':')[0]
            type_document = int(type_document_str)
            # Debug print removed to avoid redundancy
        except (IndexError, ValueError):
            return False

        if type_document in self.VALID_DOCUMENT_TYPES:
            print(f"Type de document valide: {type_document}")
            return True
        else:
            print(f"Type de document invalide: {type_document}")
            return False

    def est_type_document_valide(self, type_document): 
        print(f"Type de document: {type_document}")     
        return type_document in self.VALID_DOCUMENT_TYPES

    #################################################################################
    #ajouter une balise de couleur pour les lignes correctes et incorrectes
    ##################################################################################
    def highlight_line(self, text_widget, idx, tag):
        start = f"{idx + 1}.0"
        end = f"{idx + 1}.end"
        text_widget.tag_add(tag, start, end)
