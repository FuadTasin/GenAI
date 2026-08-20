from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers import StructuredOutputParser,ResponseSchema
from dotenv import load_dotenv

load_dotenv()

model=ChatGroq(model="openai/gpt-oss-120b",temperature=0.3)

response_schema=[
    ResponseSchema(
        name='Fact 1',
        description='The 1st fact about the topic'
    ),
    ResponseSchema(
        name='Fact 2',
        description='The 2nd fact about the topic'
    ),
    ResponseSchema(
        name='Fact 3',
        description='The 3rd fact about the topic'
    ),
    ResponseSchema(
        name='Fact 4',
        description='The 4th fact about the topic'
    ),
]

parser=StructuredOutputParser.from_response_schemas(
    response_schema
)

template=PromptTemplate(
    template="""
    Give me five facts about {topic}.
    {format_instruction}
    """,
    input_variables=["topic"],
    partial_variables={"format_instruction":parser.get_format_instructions()}
)

chain=template|model|parser
result=chain.invoke(
    {
        "topic":"Machine Learning"
    }
)
print(result)