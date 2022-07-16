import pdfx
from ..link_analyzer.link_module import LinkAnalyzer


class PDFAnalyzer:

    def __init__(self, path):
        self.path = path
        self.text = self.read()
        self.link_analyzer = LinkAnalyzer(self.text)

    def read(self, path):
        with open(self.path) as f:
            self.text = f.read()
