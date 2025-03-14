import re
import ast
import openai
from litellm import completion
from extractors.util.spacy import SpacySingleton
from pydantic import BaseModel

INPUT_EXAMPLE = {
    "apiKey": "<API_KEY_GOES_HERE>",
    "text" : "The Beatles were an English rock band, formed in Liverpool in 1960, that comprised John Lennon, Paul McCartney, George Harrison and Ringo Starr.",
    "extractionKeyword": "names",
    "temperature": 0.0,
    "spacyTokenizer": "en_core_web_sm",
}


class GptInformationExtractionModel(BaseModel):
    apiKey: str
    text: str
    extractionKeyword: str
    temperature: float
    spacyTokenizer: str

    class Config:
        schema_example = {"example": INPUT_EXAMPLE}


def gpt_information_extraction(req: GptInformationExtractionModel):
    """Uses OpenAI's GPT model to extract keyword from a text."""
    openai.api_key = req.apiKey
    try: 
        response = completion(
            model = "gpt-3.5-turbo",
            messages = [
                {
                    "role": "system",
                    "content":   f"""
                        Please extract all {req.extractionKeyword} from following text:
                        {req.text}-
                        Only return things that are linked to {req.extractionKeyword}.
                        Return only a valid JSON with this structure. 
                        ```json
                        {{
                            "keywords": ["list with keywords goes here"]
                        }}
                        ```
                        Return nothing except this JSON. Make sure to only return {req.extractionKeyword} and nothing else. 
                        If you can't find any {req.extractionKeyword} in the text, just return nothing."""
                    ,
                },
            ],
            temperature=req.temperature,
        )

        out = response["choices"][0]["message"]["content"]
        output_dict = ast.literal_eval(out)

        # check if the output is really a dictionary
        if isinstance(output_dict, dict):
            nlp = SpacySingleton.get_nlp(req.spacyTokenizer)
            doc = nlp(req.text)

            char_positions = []
            if len(output_dict["keywords"]) > 0:
                for found_keyword in output_dict["keywords"]:
                    regex = re.compile(f"{found_keyword}")
                    match =  regex.search(req.text)
                    start, end = match.span()
                    span = doc.char_span(start, end, alignment_mode="expand")
                    char_positions.append((req.extractionKeyword, span.start, span.end)) 
            else:
                return "No matching keywords found."
            return {"extraction": char_positions}
        else:
            return f"GPT response was not a valid dictionary. The response was: {response}."
    except Exception as e: 
            return f"That didn't work. Did you provide a valid API key? Go error: {e}"
