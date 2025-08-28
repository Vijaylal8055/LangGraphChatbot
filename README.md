Features
Graph-based conversation flow using StateGraph from LangGraph.
Local LLM support via Ollama (supports models like llama3).
State management using TypedDict for clean structure.
Streaming responses from the LLM for an interactive experience.
Simple CLI interface for chat.
How It Works
Defines a State (list of messages with roles: user/assistant).
Builds a StateGraph with:
START → chatbot → END
chatbot node uses Ollama LLM (llama3) to generate responses.
Streams responses back to the user in a loop.
Installation
Prerequisites
Python 3.10+
Ollama
installed and running locally
langgraph and langchain_community installed
Code Overview
State Definition: Stores conversation messages.
Graph Construction: Adds a chatbot node and connects it between START and END.
Streaming Updates: Outputs assistant responses continuously as events stream.
Main Loop: Handles user input until quit is typed.
Future Enhancements
Add memory for multi-turn conversations across sessions.
Integrate with a web UI or FastAPI backend.
Support multiple LLM providers.
