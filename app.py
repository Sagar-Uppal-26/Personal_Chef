
import os
import uuid

import streamlit as st
from dotenv import load_dotenv
from langchain.messages import HumanMessage

from chef_agent import create_chef_agent

load_dotenv()

st.set_page_config(
    page_title="Personal Chef",
    page_icon="🥗",
    layout="centered",
)

st.title("🥗 Personal Chef")
st.write(
    "Turn the ingredients in your kitchen into "
    "a delicious vegetarian meal."
)

st.divider()

with st.form("recipe_form"):
    ingredients = st.text_area(
        "What ingredients do you have?",
        placeholder="Example: potatoes, capsicum, bread, tomatoes, spices",
        height=120,
    )

    servings = st.selectbox(
        "Number of servings",
        [1, 2, 3, 4, 5, 6],
        index=1,
    )

    cooking_time = st.selectbox(
        "Preferred cooking time",
        ["Any", "15 minutes", "30 minutes", "45 minutes", "60 minutes"],
        index=2,
    )

    preferences = st.text_input(
        "Dietary preferences (optional)",
        placeholder="Example: vegan, no onion, less spicy",
    )

    submitted = st.form_submit_button(
        "🍳 Generate my recipe",
        type="primary",
        use_container_width=True,
    )

if submitted:
    if not ingredients.strip():
        st.warning("Please enter the ingredients you have.")
        st.stop()

    google_key = os.getenv("GOOGLE_API_KEY")
    tavily_key = os.getenv("TAVILY_API_KEY")

    # On Streamlit Community Cloud, use its private Secrets settings.
    if not google_key:
        try:
            google_key = st.secrets["GOOGLE_API_KEY"]
        except (KeyError, FileNotFoundError):
            pass

    if not tavily_key:
        try:
            tavily_key = st.secrets["TAVILY_API_KEY"]
        except (KeyError, FileNotFoundError):
            pass

    if not google_key or not tavily_key:
        st.error(
            "API keys are missing. Check your local .env file "
            "or your deployed app's Secrets settings."
        )
        st.stop()

    try:
        # Keep a separate conversation ID for this browser session.
        if "thread_id" not in st.session_state:
            st.session_state.thread_id = str(uuid.uuid4())

        agent = create_chef_agent(google_key, tavily_key)

        request = f"""
Available ingredients:
{ingredients}

Number of servings: {servings}
Preferred cooking time: {cooking_time}
Dietary preferences: {preferences or "None specified"}

Suggest one suitable vegetarian recipe.
Do not force every available ingredient into the recipe.
Separate optional ingredients from ingredients I already have.
Include quantities and numbered cooking instructions.
Use web search when helpful and cite source URLs when used.
"""

        with st.spinner("Your Personal Chef is preparing a recipe..."):
            response = agent.invoke(
                {
                    "messages": [
                        HumanMessage(content=request)
                    ]
                },
                {
                    "configurable": {
                        "thread_id": st.session_state.thread_id
                    }
                },
            )

        answer = response["messages"][-1].content

        st.divider()
        st.subheader("👨‍🍳 Your Recipe")

        if isinstance(answer, str):
            st.markdown(answer)
        elif isinstance(answer, list):
            for item in answer:
                if isinstance(item, dict) and item.get("type") == "text":
                    st.markdown(item["text"])
                else:
                    st.write(item)
        else:
            st.write(answer)

        st.info(
            "Use properly stored ingredients and discard food that "
            "may be spoiled."
        )

    except Exception:
        st.error(
            "The recipe could not be generated. Check your API keys, "
            "model access, and terminal error details."
        )
