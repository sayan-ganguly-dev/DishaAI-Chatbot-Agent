from src.agents.chat_agent.states.chat_agents_state import ChatAgentState
from src.agents.chat_agent.nodes.chat_node import chat
from langgraph.graph import START, END, StateGraph
from langgraph.graph.state import CompiledStateGraph

def create_chat_agent_graph() -> CompiledStateGraph:
    """
    """
    graph_builder = StateGraph(ChatAgentState)
    
    graph_builder.add_node("chat_node", chat)

    graph_builder.add_edge(START, "chat_nde")
    graph_builder.add_edge("chat-node", END)

    return graph_builder.compile()