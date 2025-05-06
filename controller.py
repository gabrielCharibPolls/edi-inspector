from verifier_bgm import BGMVerifier

class EDIController:
    def __init__(self):
        self.verifiers = {
            "BGM": BGMVerifier(),

        }

    def verifier_lignes(self, lines, text_widget):
        for idx, line in enumerate(lines):
            segment_type = self.extraire_segment(line)
            if segment_type in self.verifiers:
                verifier = self.verifiers[segment_type]
                verifier.verifier_ligne(line, idx, text_widget)

    def extraire_segment(self, line):
        return line.split('+')[0].strip() if '+' in line else line.strip()
