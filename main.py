

from gpt.gpt import get_response
from Rating.Rating import Rating
from Files.Files import Files

if __name__ == '__main__':
    
        
    rating = Rating(template_path="Rating/template.json")
    files = Files()

    html_file = files.get_html("test_files/index.html")
    css_file = files.get_css("test_files/screenStyle.css")
    js_file = files.get_js("test_files/js_file.js")


    prompt = rating.get_prompt(html_file, css_file, js_file)

    output = get_response(prompt=prompt, url="https://telekom.sk")

    #print(type(output))
    #print(output)

    #score = rating.extract_website_name(filled_template=output)

    #print(score)


