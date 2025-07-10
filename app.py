from typing import List, Dict, TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_community.llms import Ollama

# Step 1: Define State using TypedDict
class State(TypedDict):
    messages: List[Dict[str, str]]

# Step 2: Initialize StateGraph
graph_builder = StateGraph(State)

# ✅ Correct: 'ollamaLLM' doesn't exist; use 'Ollama' from langchain_community.llms
llm = Ollama(model="llama3")

# Define ChatBot function
def chatbot(state: State) -> State:
    response = llm.invoke(state["messages"])
    state["messages"].append({"role": "assistant", "content": response})
    return {"messages": state["messages"]}

# Add nodes and edges
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

# Compile the graph
graph = graph_builder.compile()

# Stream updates
def stream_graph_updates(user_input: str):
    # Initialize the state with the user's input
    state: State = {"messages": [{"role": "user", "content": user_input}]}
    for event in graph.stream(state):
        for value in event.values():
            # Print the assistant's response
            print("Assistant:", value["messages"][-1]["content"])

# Run chatbot in a loop
if __name__ == "__main__":
    while True:
        try:
            user_input = input("User: ")
            if user_input.lower() in ["quit", "exit", "q"]:
                print("Goodbye!")
                break

            stream_graph_updates(user_input)
        except Exception as e:
            print(f"An error occurred: {e}")
            break
