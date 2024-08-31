import google.generativeai as genai

genai.configure(api_key="YOUR_GEMINI_API_KEY")

model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

def interaction(prompt):
    response = chat.send_message(prompt)
    return response.text

