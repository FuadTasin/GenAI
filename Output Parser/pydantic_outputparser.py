from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from dotenv import load_dotenv

load_dotenv()

model=ChatGroq(model="openai/gpt-oss-120b",temperature=0.3)

class ModelEvaluation(BaseModel):

    model_name: str=Field(description="Name of the machine learning Model")
    accuracy: float=Field(gt=0,lt=1,description="Accuracy of the model.Greater than 0 and less than 1")
    dataset: str=Field(description="Name of the dataset used for evaluation")

parser=PydanticOutputParser(
    pydantic_object=ModelEvaluation
)

template=PromptTemplate(
    template="""
        Generate the name,accuracy,and dataset of a fictional machine learning model trained for {task}.
        {format_instruction}
        """,
    input_variables=["task"],
    partial_variables={"format_instruction":parser.get_format_instructions()}
        
)

# print(template.format(task="image classification"))

chain=template|model|parser

result=chain.invoke({
    "task":"image classification"
})

print(result)