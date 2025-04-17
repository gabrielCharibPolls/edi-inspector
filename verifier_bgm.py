
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
        pass    
        VALID_DOCUMENT_TYPES = {"380", "351", "384"}

    def verifier_bgm(self, lines, text_widget):
        for idx, line in enumerate(lines):
            if line.startswith("BGM"):
                parts = line.strip().split('+')
                if len(parts) < 4:
                    self.highlight_line(text_widget, idx, "erreur")
                else:
                    doc_type = parts[1]
                    print(f"Document Type: {doc_type}")
                    if doc_type not in ["380", "351", "384"]:
                        self.highlight_line(text_widget, idx, "erreur")
                    else:
                        # Assuming the rest of the line is correct
                        # Define a set of valid document types as a class variable
                        

                        if doc_type not in self.VALID_DOCUMENT_TYPES:
                            self.highlight_line(text_widget, idx, "erreur")
                        else:
                            self.highlight_line(text_widget, idx, "correct") 
                            self.highlight_line(text_widget, idx, "correct")
    
    def highlight_line(self, text_widget, idx, tag):
        start = f"{idx + 1}.0"
        end = f"{idx + 1}.end"
        text_widget.tag_add(tag, start, end)
