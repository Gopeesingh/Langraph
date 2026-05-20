1_basic_chatbot.py 

1.a -> create groq api key from groq.com
1.b -> pip install langchain-groq

2_chatbot_with_tools
explaination :- 
This code implements a tool-augmented chatbot using LangGraph. It defines a state containing message history and uses an LLM capable of tool calling. The chatbot node generates responses, and a router checks whether the response includes tool calls. If so, execution moves to a tool node that executes the requested tool, then loops back to the chatbot. This continues until no further tool calls are needed, enabling dynamic reasoning and tool usage.


4_chat_with_sqlLite_checkp 

pip install langgraph-checkpoint-sqlite