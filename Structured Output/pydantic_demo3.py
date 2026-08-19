from pydantic import BaseModel,EmailStr,Field
from typing import Optional,Literal,Annotated
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()
model=ChatGroq(model= "openai/gpt-oss-120b")

class JobApplication(BaseModel):
    name:str="Unknown"
    experience:Optional[int]=None
    email: EmailStr
    expected_salary:int=Field(gt=0,description="Expected Annual Salary of the candidate")

structured_model=model.with_structured_output(JobApplication)

result=structured_model.invoke(
     """My name is Arif Hasan. I have 3 years of experience
    as a Machine Learning Engineer.

    My email is arif@gmail.com.
    I am expecting an annual salary of 50000 dollars.
    """
)

print(result)
print(result.name)
