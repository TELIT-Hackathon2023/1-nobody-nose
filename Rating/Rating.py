import json
import re

class Rating:

    def __init__(self, template_path) -> None:
        
        self.template: json = None

        self.load_template(template_path=template_path)


    def load_template(self, template_path):
        """extracts rating template as .json
        """

        json_file_path = template_path

        # Otevření a načtení JSON souboru
        with open(json_file_path, 'r') as json_file:
            self.template = json.load(json_file)

    
    def get_template(self) -> json:
        """gets json template

        Returns:
            json: rating template in json format
        """
        return json.dumps(self.template, indent=2)
    

    def get_prompt(self, html_file, css_file, js_file) -> str:
        """formulates prompt to chatgpt

        Returns:
            str: string to pass to chatgpt
        """
        prompt = html_file + "\n" + css_file + "\n" + js_file + "\n"

        instruction = "Rate provided html, css and javascript file. If some file is missing, rate it as 0. Fill out this json template and do not add additional text after:\n"

        template = self.get_template()

        prompt = prompt + instruction + template

        return prompt
    

    def extract_score(self, filled_template: str) -> str:
        """Extracts score from filled rating template.

        Args:
            filled_template (str): Filled rating template by chatgpt.

        Returns:
            str: Score of the website.
        """
        total_website_score = None
        match = re.search(r'"Total Website Score": "([^"]+)"', filled_template)
        if match:
            total_website_score = match.group(1)
        else:
            total_website_score = "Not found"

        return total_website_score
    
        
    def extract_website_name(self, filled_template: str) -> str:
        """extracts website name from filled rating template

        Args:
            filled_template (json): filled rating template by chatgpt

        Returns:
            str: name of website
        """
        page_title = None
        match = re.search(r'"Page Title": "([^"]+)"', filled_template)
        if match:
            page_title = match.group(1)
        else:
            page_title = "Page title not found"

        return page_title
    

    def extract_evaluation_date(self, filled_template: str) -> str:
        """extracts evaluation date

        Args:
            filled_template (json): filled rating template by chatgpt

        Returns:
            str: date of evaluation
        """
        evaluation_date = None
        match = re.search(r'"Evaluation Date": "([^"]+)"', filled_template)
        if match:
            evaluation_date = match.group(1)
        else:
            evaluation_date = "Date not found"

        return evaluation_date
