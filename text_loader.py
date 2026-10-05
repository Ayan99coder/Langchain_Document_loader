from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()
model = ChatGoogleGenerativeAI(model = 'gemini-3.7-flash')
loader = TextLoader('poem.txt',encoding='Utf-8')
docs = loader.load()
print(docs[0].page_content)
print(docs[0].metadata)
print(len(docs))

prompt = PromptTemplate(template='PLease give me the summary of the following txt file {text}',input_variables=['text'])

chain = prompt|model|StrOutputParser()

output = chain.invoke({'text':docs[0].page_content})
print(output)