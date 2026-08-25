# GenAI Practice Repository

A personal practice repository for learning and experimenting with **Generative AI, LLMs, and LangChain** using Python.

This repository is mainly focused on **learning by building small examples** rather than being a single production-ready application. Each folder explores a different concept, API, or LangChain component through simple experiments and demos.

## What I Practiced

The repository covers several core GenAI concepts:

- **Chat Models** — experimenting with models from Groq, Google Gemini, and Hugging Face.
- **Prompts** — working with prompt templates, dynamic prompts, and interactive prompt-based applications.
- **Messages** — understanding system, human, and AI messages while building simple chatbots.
- **Chains** — exploring simple, sequential, parallel, and conditional chains.
- **Embeddings** — generating and experimenting with embeddings using Gemini, Hugging Face, and Sentence Transformers.
- **Output Parsers** — converting model responses into strings, JSON, Pydantic objects, and structured formats.
- **Structured Output** — practicing `TypedDict` and Pydantic-based structured responses.
- **Streamlit** — creating small interactive GenAI interfaces.
- **Jupyter** — experimenting with concepts interactively through notebooks.

## Repository Structure

```text
GenAI/
│
├── Chain/
│   ├── simple_chain.py
│   ├── sequential_chain.py
│   ├── parallel_chain_demo1.py
│   ├── parallel_chain_demo2.py
│   ├── conditional_chain.py
│   ├── conditional_chain_v2.py
│   ├── conditional_chain_v3.py
│   └── lambda_function.ipynb
│
├── Embedding/
│   ├── gemini_embedding_demo1.py
│   ├── gemini_embedding_demo2.py
│   ├── huggingface_embedding_demo2.py
│   ├── huggingface_embedding_demo3.py
│   └── sentence_transformer.py
│
├── LLM/
│   └── llm_model.py
│
├── Message/
│   ├── simple_chatbot.py
│   ├── final_chatbot.py
│   └── chatbot_with_ui.py
│
├── Output Parser/
│   ├── str_outputparser.py
│   ├── json_outputparser.py
│   ├── pydantic_outputparser.py
│   └── structured_outputparser.py
│
├── Structured Output/
│   ├── pydantic_demo.py
│   ├── pydantic_demo2.py
│   ├── pydantic_demo3.py
│   ├── typeddict_demo.py
│   └── typeddict_demo2.py
│
├── chat_model/
│   ├── chatgroq.py
│   ├── gemini_demo.py
│   └── huggingface_demo.py
│
├── prompts/
│   ├── dynamic_ui.py
│   └── modern_version.py
│
├── requirements.txt
└── README.md
```

## Technologies Used

- Python
- LangChain
- LangChain Core
- OpenAI
- Google Gemini
- Anthropic
- Groq
- Hugging Face Transformers
- Sentence Transformers
- Pydantic
- Streamlit
- Jupyter Notebook
- NumPy
- Scikit-learn

The dependencies used throughout the repository are listed in [`requirements.txt`](requirements.txt).

## Setup

Clone the repository:

```bash
git clone https://github.com/FuadTasin/GenAI.git
cd GenAI
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows:

```powershell
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Some examples use external LLM providers, so API keys may be required.

Create a `.env` file in the project root and add the keys required by the example you want to run. For example:

```env
OPENAI_API_KEY=your_api_key
GROQ_API_KEY=your_api_key
GOOGLE_API_KEY=your_api_key
ANTHROPIC_API_KEY=your_api_key
HUGGINGFACEHUB_API_TOKEN=your_api_key
```

Only configure the provider keys needed for the particular example. Do not commit real API keys to the repository.

## Running the Examples

Most files are standalone Python examples and can be run directly. For example:

```bash
python chat_model/chatgroq.py
```

For Streamlit-based examples:

```bash
streamlit run prompts/modern_version.py
```

For notebook-based examples, start Jupyter with:

```bash
jupyter notebook
```

and open the relevant `.ipynb` file.

## Learning Goals

The main goal of this repository is to build a practical understanding of how modern GenAI applications are constructed.

Rather than jumping directly into a large project, the examples break the ecosystem into smaller pieces: connecting to models, constructing prompts, working with messages, composing chains, generating embeddings, validating structured responses, and building simple interfaces.

## Note

This is a **practice and learning repository**. The code is intentionally organized as small experiments and demonstrations, so some examples may be repetitive, simplified, or written in different styles while exploring the same concept.

The repository is not intended to represent a polished production system.

## Author

**Fuad Tasin**

GitHub: [@FuadTasin](https://github.com/FuadTasin)

---

Built for learning, experimentation, and getting hands-on with Generative AI 🚀
