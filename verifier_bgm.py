
###############################################################
## BGM Verifier
###############################################################
class BGMVerifier:
    def __init__(self):
        pass

    def verifier_bgm(self, lines, text_widget):
        for idx, line in enumerate(lines):
            if line.startswith("BGM"):
                parts = line.strip().split('+')
                if len(parts) < 4:
                    self.highlight_line(text_widget, idx, "erreur")
                else:
                    self.highlight_line(text_widget, idx, "correct")
    
    def highlight_line(self, text_widget, idx, tag):
        start = f"{idx + 1}.0"
        end = f"{idx + 1}.end"
        text_widget.tag_add(tag, start, end)
