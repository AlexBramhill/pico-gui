class PageBuilder():
    def __init__(self, page):
        self.page = page

    def build(self):
        self.page.build_header()
        self.page.build_body()
        self.page.build_footer()
        return self.page
