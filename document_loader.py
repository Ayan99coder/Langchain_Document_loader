from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader = DirectoryLoader(
   path='',
   glob='',
   loader_cls=PyPDFLoader
)
docs = loader.lazy_load()
print(docs[0].page_content)