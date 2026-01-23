from src.agents.chat_agent.states.chat_agents_state import ChatAgentState
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
from src.agents.chat_agents.tools.date_time import get_current_date_and_time


load_dotenv(override=True)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def chat(state: ChatAgentState) -> ChatAgentState:
    """
    """
    model = ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=GROQ_API_KEY
    )

    model = model.bind_tools(
        tools=[
            get_current_date_and_time
        ]
    )

    # print(state["message"]) 

    answer = model.invoke(state['messages'])
    return{
        "messages": [answer]
    }