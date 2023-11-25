
class Files:

    def __init__(self) -> None:
        self.html = None
        self.css = None
        self.js = None


    def get_html(self, path):
        try:
            with open(path, 'r') as file:
                # Read the entire contents of the file
                self.html = file.read()
        except FileNotFoundError:
            self.html = "HTML file not provided"

        return self.html
    
    def get_css(self, path):
        try:
            with open(path, 'r') as file:
                # Read the entire contents of the file
                self.css = file.read()
        except FileNotFoundError:
            self.css = "CSS file not provided"

        return self.css
    
    def get_js(self, path):
        try:
            with open(path, 'r') as file:
                # Read the entire contents of the file
                self.js = file.read()
        except FileNotFoundError:
            self.js = "JavaScript file not provided"


        return self.js