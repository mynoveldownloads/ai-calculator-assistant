from PyPDF2 import PdfReader
from ollama import chat

def extract(file_path: str, pg_reduction: int=0) -> list:
    path = PdfReader(str(file_path))

    #print(len(path.pages))
    content = []
    for page in range(len(path.pages) - pg_reduction):
        extract = path.pages[page]
        content.append(extract.extract_text())
    return content

def prompt(txt_content: str, 
            instructions: str="Your role is to summarise this research paper and tell me what it is about.") -> tuple[dict] :
    
    response = chat(
        model='phi3:instruct',
        messages=[{
            'role': 'user',
            'content': f'{instructions}. {txt_content}'
        }]
    )
    return response['message']['content'] # Not rly sure how this works

