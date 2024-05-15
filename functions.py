from ollama import chat

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

