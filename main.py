

from gpt.gpt import get_response
from Rating.Rating import Rating

if __name__ == '__main__':
    
        
    rating = Rating(template_path="Rating/template.json")

    prompt = rating.get_prompt()

    output = get_response(prompt=prompt, url="https://telekom.sk")

    print(type(output))
    print(output)

    #score = rating.extract_website_name(filled_template=output)

    #print(score)


