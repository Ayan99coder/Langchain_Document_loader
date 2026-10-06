
from langchain_community.document_loaders import WebBaseLoader
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-3.7-flash')

url = 'https://roadmap.sh/r/ai-roadmap-for-2026---final-draft'
loader = WebBaseLoader(url)
docs = loader.load()
parser = StrOutputParser()
prompt = PromptTemplate(template='give me answere on {question} from this {text}',input_variables=['question','text'])
chain = prompt|model| parser
output = chain.invoke({'question':'ya kis baary me baat krha iss document me ','text':docs[0].page_content})
print(output)