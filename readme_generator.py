from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
chat = ChatGroq(temperature=0.5,
                model_name="Llama3-70b-8192",
                api_key=GROQ_API,
                max_tokens=100,
                model_kwargs={
                    "top_p": 1,
                    "frequency_penalty": 0.0,
                    "presence_penalty" : 0.0
                }
                )
def ask(text):
    system = "You help developers creationg readme file from code as an Assistant don't include irrelevant words just give me readme text so that I can copy pate"
    human = '{query} \n\n `Read the code and generate README.md file?`'
    prompt = ChatPromptTemplate.from_messages(messages=[('system', system), ('human', human)])
    chain = prompt | chat
    response = chain.invoke({"query": f'{text}'}).content
    return response
