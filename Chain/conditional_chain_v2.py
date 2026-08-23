from dotenv import load_dotenv
from langchain_groq import ChatGroq
from pydantic import BaseModel,Field
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_core.runnables import RunnableBranch

load_dotenv()

model=ChatGroq(model="openai/gpt-oss-120b",temperature=0.3)

class MovieReview(BaseModel):
    sentiment:str=Field(description="Review will be either Positive or Negative")

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
    template="Reply to this negative movie review by apologizing and offering help: \n {review}",
    input_variables=["review"]
)

str_parser=StrOutputParser()

positive_chain=positive_prompt|model|str_parser
negative_chain=negative_prompt|model|str_parser

conditional_chain=RunnableBranch(
    (
        lambda x:"positive" in x["sentiment"].sentiment.lower(),positive_chain
    ),negative_chain
)

review="The movie was absolutely fantastic. I loved every minute of it."

sentiment=classifier_chain.invoke({
    "review":review
})

result=conditional_chain.invoke({
    "review":review,
    "sentiment":sentiment
})

print(result)