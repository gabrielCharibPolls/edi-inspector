
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
class BGMVerifier:
    def __init__(self):
        # Liste des types de documents valides
        #attention, il faut que ce soit un set et pas une liste, sinon ça ne marche pas
        self.VALID_DOCUMENT_TYPES = {380, 351, 384}
        pass    
  



 #todo  faire en sorte que cette fonction appel des autre fonction qui soit lier à la vérification de chaque type de document
    def verifier_bgm(self, lines, text_widget):
        for idx, line in enumerate(lines):
            #et si la ligne ne commence pas par BGM, on l'ignore
            if line.startswith("BGM"):
                parts = line.strip().split('+')
                if len(parts) < 4:
                    self.highlight_line(text_widget, idx, "erreur")
                else:
                    doc_type = parts[1]
                    if not self.verfier_type_document(int(doc_type)):
                        self.highlight_line(text_widget, idx, "erreur")
                    else:
                            self.highlight_line(text_widget, idx, "correct") 
                            print(f"Document Type: {doc_type} is valid.")
    #######################################################
    #verifie le type de document EDI
    #todo corriger cette erreur ValueError: invalid literal for int() with base 10: '380'
    ######################################################
    def verfier_type_document(self, type_document):
        if type_document not in self.VALID_DOCUMENT_TYPES:
            print(f"Invalid Document Type: {type_document}")

            return False
        return True

    def highlight_line(self, text_widget, idx, tag):
        start = f"{idx + 1}.0"
        end = f"{idx + 1}.end"
        text_widget.tag_add(tag, start, end)
