from typing import TypedDict, Annotated
from langchain_core.messages import AnyMessage
import operator

class ChatAgentState(TypedDict):
    """
    """
    messages: Annotated[list[AnyMessage], operator.add]