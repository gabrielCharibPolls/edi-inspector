from verifier_bgm import BGMVerifier
from validate_UNH import validate_UNH  

class EDIController:
    def __init__(self):
        self.verifiers = {
            "BGM": BGMVerifier(),
            "UNB": validate_UNH(),  # Placeholder for UNB verifier
            "UNH": None,  # Placeholder for UNH verifier


        }

    def verifier_lignes(self, lines, text_widget):
        for idx, line in enumerate(lines):
            segment_type = self.extraire_segment(line)
            if segment_type in self.verifiers:
                verifier = self.verifiers[segment_type]
                print(f"Vérification de la ligne {idx + 1}: {line.strip()}")
                verifier.verifier_ligne(line, idx, text_widget)

    def extraire_segment(self, line):
        return line.split('+')[0].strip() if '+' in line else line.strip()
