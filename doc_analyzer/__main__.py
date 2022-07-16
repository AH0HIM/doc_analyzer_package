import doc_analyzer


class MainApp:
    def __init__(self, path):
        self.path = path

    def run(self):
        pdf = doc_analyzer.PDFAnalyzer(self.path)
        pdf.link_analyzer.collect_links()
        pdf.link_analyzer.review_link()
        pdf.link_analyzer.clean()
        pdf.link_analyzer.make_report()


if __name__ == "__main__":
    print("Run my doc_analyzer_package")
    pdf_ = doc_analyzer.PDFAnalyzer('//')
    print("Done")
