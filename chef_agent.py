
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.memory import InMemorySaver
from langchain.tools import tool
from tavily import TavilyClient


SYSTEM_PROMPT = """
You are Personal Chef, a helpful vegetarian chef.

The user will provide ingredients available in their kitchen.
Suggest a practical vegetarian recipe using those ingredients.

Rules:
1. Do not suggest meat, poultry, fish, or seafood.
2. Do not force every ingredient into one recipe.
3. Separate available ingredients from optional ingredients.
4. Give the recipe name, preparation time, cooking time,
   servings, ingredient quantities, and numbered instructions.
5. Keep instructions simple and beginner-friendly.
6. Respect any dietary preferences the user provides.
7. Use web search when helpful.
8. Include source URLs when you use web search results.
9. Never assume leftover food is safe just because it looks usable.
"""


def create_chef_agent(google_api_key, tavily_api_key):
    tavily_client = TavilyClient(api_key=tavily_api_key)

    @tool
    def web_search(query: str) -> dict:
        """Search the web for vegetarian recipes and cooking instructions."""
        return tavily_client.search(query, max_results=5)

    llm = ChatGoogleGenerativeAI(
        model="gemini-3.5-flash-lite",
        google_api_key=google_api_key,
        temperature=0.4,
    )

    agent = create_agent(
        model=llm,
        tools=[web_search],
        system_prompt=SYSTEM_PROMPT,
        checkpointer=InMemorySaver(),
    )

    return agent
