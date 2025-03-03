from fastapi import FastAPI
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from all_keys import groq_api_key

# Initialize FastAPI
app = FastAPI()

# Initialize Groq LLM
llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    temperature=0,
    groq_api_key=groq_api_key
)

# Define Prompt Template
prompt_extract = PromptTemplate.from_template(
   """
        ### SCRAPED TEXT FROM WEBSITE:
        {page_data}
        ### INSTRUCTION:
        The scraped text is from the career's page of a website.
        Your job is to extract the job postings and return them in JSON format containing the 
        following keys: role, experience, skills and description.
        Only return the valid JSON.
        ### VALID JSON (NO PREAMBLE):    
        """
)

# Define API Route
@app.get("/fetch-job/")
def fetch_job(url : str):
    try:
        # Load page content
        loader = WebBaseLoader(url)
        page_data = loader.load().pop().page_content

        # Extract information
        chain_extract = prompt_extract | llm
        res = chain_extract.invoke({"page_data": page_data})

        # Parse JSON output
        json_parser = JsonOutputParser()
        json_res = json_parser.parse(res.content)

        return {"status": "success", "data": json_res}

    except Exception as e:
        return {"status": "error", "message": str(e)}

# Run the server using:
# uvicorn main:app --reload
