from dotenv import load_dotenv
from langchain_groq import ChatGroq
from pydantic import BaseModel,Field
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_core.runnables import RunnableBranch

load_dotenv()

model=ChatGroq(model="openai/gpt-oss-120b",temperature=0.3)

class MovieReview(BaseModel):
    sentiment:str=Field(description="Review will be either Positive or Negative or Neutral")

pydantic_parser=PydanticOutputParser(
    pydantic_object=MovieReview
)

classifier_prompt=PromptTemplate(
    template="""
    Think you are a movie review classifier.
    Classify the following review as either:
    - Positive
    - Negative
    Return only one word: Positive or Negative
    Review: {review}
    {format_instruction}
    """,
    input_variables=["review"],
    partial_variables={"format_instruction":pydantic_parser.get_format_instructions()}
)

classifier_chain=classifier_prompt|model|pydantic_parser

positive_prompt=PromptTemplate(
    template="Reply to this positive movie review in a friendly way: \n {review}",
    input_variables=["review"]
)
negative_prompt=PromptTemplate(
    template="Reply to this negative movie review by apologizing and offering help: \n Review: {review}",
    input_variables=["review"]
)
neutral_prompt=PromptTemplate(
    template="Reply politely to this neutral review ask for suggestions to improve: \n Review: {review}",
    input_variables=["review"]
)
default_prompt=PromptTemplate(
    template=":The sentiment could not be determined: \n Review: {review}",
    input_variables=["review"]
)

str_parser=StrOutputParser()

positive_chain=positive_prompt|model|str_parser
negative_chain=negative_prompt|model|str_parser
neutral_chain=neutral_prompt|model|str_parser
default_chain=default_prompt|model|str_parser

conditional_chain=RunnableBranch(
    (
        lambda x:"positive"==x["sentiment"].sentiment.strip().lower(),positive_chain
    ),
    (
        lambda x:"neutral"==x["sentiment"].sentiment.strip().lower(),positive_chain
    ),
    (
        lambda x:"negative"==x["sentiment"].sentiment.strip().lower(),positive_chain
    ),
    default_chain
)

review="The movie was average"

sentiment=classifier_chain.invoke({
    "review":review
})

result=conditional_chain.invoke({
    "review":review,
    "sentiment":sentiment
})

print(f"Sentiment:{sentiment.sentiment}\nResult:{result}")