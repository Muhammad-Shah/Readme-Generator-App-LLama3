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
    system = "You create mardown from the code As an assistant."
    human = '{query} \n\n `Read the code and generate README.md file?` Avoid writing "Here is a generated README.md file based on the provided code:" It make it obvious that AI wrote the READ.md file'
    prompt = ChatPromptTemplate.from_messages(
        messages=[('system', system), ('human', human)])
    chain = prompt | chat
    response = chain.invoke({"query": f'{text}'}).content
    return response
