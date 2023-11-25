import json

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
    

    def get_prompt(self) -> str:
        """formulates prompt to chatgpt

        Returns:
            str: string to pass to chatgpt
        """
        prompt = ""

        instruction = "Rate provided html, css and javascript file. If some file is missing, rate it as 0. Fill out this json template:\n"

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

        filled = json.loads(filled_template)

        return filled.get("Total Website Score", "Score not found")
    
        
    def extract_website_name(self, filled_template: str) -> str:
        """extracts website name from filled rating template

        Args:
            filled_template (json): filled rating template by chatgpt

        Returns:
            str: name of website
        """
        filled = json.loads(filled_template)

        return filled.get("Website Evaluation", {}).get("Page Title", "Page Title not found")
    

    def extract_evaluation_date(self, filled_template: str) -> str:
        """extracts evaluation date

        Args:
            filled_template (json): filled rating template by chatgpt

        Returns:
            str: date of evaluation
        """
        filled = json.loads(filled_template)

        return filled.get("Website Evaluation", {}).get("Evaluation Date", "Date not found")
