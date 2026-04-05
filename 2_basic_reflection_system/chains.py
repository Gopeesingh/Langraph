from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI


generation_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a twitter techie influencer assistant task with writing excellent twitter posts. "
            "Generate best twitter post possible for user's request."
            "if the user provide critique, respond with revised version of your previous attempts.",
            ),
        MessagesPlaceholder(variable_name="messages"),
    ]
        )

reflection_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a viral twitter techie influencer grading a tweet. Generate critique and recommendations for user's tweet."
            "Always provide details recommendations, including request for length, virality style, etc."
            "if the user provide critique, respond with revised version of your previous attempts.",
            ),
        MessagesPlaceholder(variable_name="messages"),
    ]
        )
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
generation_chain = generation_prompt | llm
reflection_chain = reflection_prompt | llm

        