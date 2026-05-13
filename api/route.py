# TODO: GET and POST routes for the API
from fastapi import APIRouter
from pydantic import BaseModel
from llm.client import ask

router = APIRouter()

class QuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    answer: str
# RISK FORMAT OF HOW THE LLM IS GOING TO OUTPUT THE ANSWER, MAYBE WE NEED TO CHANGE THIS
@router.post("/ask", response_model=AnswerResponse)
def ask_question(payload: QuestionRequest):
    answer = ask(payload.question)
    return AnswerResponse(answer=answer)