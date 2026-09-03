from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import WebBaseLoader,SeleniumURLLoader
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

url="https://www.amazon.com/Apple-2025-MacBook-Laptop-10%E2%80%91core/dp/B0FWD623D1/ref=sr_1_1?crid=31959N3AM4DEV&dib=eyJ2IjoiMSJ9.UkU3eReZ9_5MrRIUTFUKj5_E7BkYAVRRt2KNUR_B6MxMrU43GqlfYuLLN9fxsJlX_mHhlc-YwYO184SOAM8vYqLsCudQ4BCrWmQKzK0bLyTMvtXAHVNrhubSXi9HmQTr6JQjyJA5ZC6qjB39sdtRfwhvzUDNLE0HKS949T-n4FOwaT7eGWJokTNN1tO64FU6FwmdO-_Oyn_5iQj2sHtG17DME_fuDqmt1DlDgqL2MRs.c2VwCFfnpINUNc4jvLA9usjhFL-j-_r_Pj368lUhhCY&dib_tag=se&keywords=macbook%2Bpro&qid=1788439827&sprefix=macbook%2Caps%2C339&sr=8-1&th=1"

# web_loader=WebBaseLoader(url)
# web_docs=web_loader.load()

# print(web_docs[0])
# print(sel_docs[0])

sel_loader=SeleniumURLLoader(urls=[url])
sel_docs=sel_loader.load()

model=ChatGroq(model='openai/gpt-oss-120b',temperature=0.5)
parser=StrOutputParser()
prompt=PromptTemplate(
    template="""
    Give the ans of the following question:
    {question},
    from the following document
    {document}
    """,
    input_variables=["question","document"]
)

chain=prompt|model|parser

result=chain.invoke({
    "question":"What is name of the model? and then what is the price of that model?",
    "document":sel_docs
})
print(result)