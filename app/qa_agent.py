from openai import OpenAI
from app.config import Config



class QAAgent:
    def __init__(self):
        self.client = OpenAI(
    # This is the default and can be omitted
    api_key=Config.OPENAI_API_KEY,
)

    def extract_answer(self, text: str, question: str) -> str:
        prompt = f"Answer the question based on the text below:\n\nText: {text}\n\nQuestion: {question}\n\nAnswer:"

       

        try:
            response = self.client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="gpt-3.5-turbo",


)
            answer = response.choices[0].message.content
           
            
            return answer if answer else "Data Not Available"
        except Exception as e:
            return f"Error extracting answer: {str(e)}"
