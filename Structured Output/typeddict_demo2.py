from optparse import Option
from typing_extensions import NotRequired
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Literal,Optional

load_dotenv()

model=ChatGroq(model= "openai/gpt-oss-120b")

class ResumeAnalyzer(TypedDict):
    candidate_name:Annotated[str,"Extract the name of the candidate"]
    key_skills:Annotated[list[str],"Extract all technical and soft skill's from the resume"]
    summary:Annotated[str,"Write a brief summary from the candidate's profile"]
    experience_level:Annotated[Literal["entry_level","mid_level","senior_level"],"Classify the candidate's experience level"]
    strength:Annotated[Optional[list[str]],"List candidate's major strength"]
    weakness:Annotated[Optional[list[str]],"List candidate's weaknesses or areas for improvement"]

structured_model=model.with_structured_output(ResumeAnalyzer)

result = structured_model.invoke(
    """My name is  Fuad Hasan Tasin. I am a Computer Science graduate with two years
    of experience working as a Machine Learning Engineer.

    I have experience with Python, PyTorch, TensorFlow, Scikit-learn,
    FastAPI, Docker, Kubernetes, MLflow, and AWS. I have built machine
    learning pipelines, deployed deep learning models, and developed
    REST APIs for AI applications.

    I also have experience working with LangChain and Retrieval-Augmented
    Generation (RAG) systems.

    My main strength is my ability to build complete machine learning
    systems from data preprocessing to deployment. However, I have limited
    experience managing large engineering teams and need to improve my
    system design skills.

    Education:
    BSc in Computer Science and Engineering.
    Age is 21 years old.
    """
)

print(result)