# 🥗 Personal Chef — AI-Powered Vegetarian Recipe Generator

Personal Chef is a Generative AI application that helps users prepare vegetarian meals using ingredients they already have in their kitchen. Users can enter available ingredients, select the number of servings and preferred cooking time, and specify dietary preferences to receive a personalized recipe with ingredient quantities and step-by-step cooking instructions.

Built using **Python, Streamlit, LangChain, Google Gemini, and Tavily Search**, the application combines an AI agent with web search capabilities to make recipe suggestions more practical and informative.

## 🌐 Live Demo

**Try the application here:** [Personal Chef — Live App](https://personalchef-rukmat4tsbvjqh9nspuya5.streamlit.app/)

Enter the ingredients available in your kitchen and generate a personalized vegetarian recipe.

## ✨ Features

- **Ingredient-Based Recipes:** Generate recipes based on ingredients available at home.
- **AI-Powered Recommendations:** Uses Google Gemini to generate personalized cooking suggestions.
- **Web Search Integration:** Uses Tavily Search to find relevant recipe information when helpful.
- **Customizable Servings:** Choose the number of servings required.
- **Cooking Time Preferences:** Specify your preferred cooking duration.
- **Dietary Preferences:** Add preferences such as vegan, less spicy, or no onion.
- **Step-by-Step Instructions:** Receive ingredient quantities and clear cooking instructions.
- **Interactive Interface:** User-friendly interface built with Streamlit.
- **Secure API Keys:** Store API keys in environment variables or deployment secrets.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application interface |
| Google Gemini | AI-powered recipe generation |
| LangChain | AI agent creation and tool integration |
| LangGraph | Agent checkpointing and conversation state |
| Tavily Search | Web search integration |
| python-dotenv | Loading environment variables |
| Jupyter Notebook | Experimentation and development |

## 📁 Project Structure

```text
Personal_Chef/
│
├── Personal_Chef.ipynb   # Original experimentation notebook
├── chef_agent.py         # Reusable AI agent logic
├── app.py                # Streamlit frontend
├── requirements.txt      # Python dependencies
├── .gitignore            # Files excluded from Git
└── README.md             # Project documentation
```

**Note:** The `.env` file is used for local development but is intentionally excluded from GitHub to protect API keys.

## ⚙️ Prerequisites

Before running the application, you need:

- Python installed on your computer.
- Git installed.
- A Google AI API key for Gemini.
- A Tavily API key for web search.
- An internet connection.

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Sagar-Uppal-26/Personal_Chef.git
cd Personal_Chef
```

### 2. Create a virtual environment

On Windows:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure API keys

Create a `.env` file in the project root directory:

```env
GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Replace the placeholder values with your actual API keys.

**Important:** Never commit your `.env` file or expose API keys in public repositories, screenshots, or shared code.

### 5. Run the application

```bash
streamlit run app.py
```

Open the local URL shown in your terminal, usually `http://localhost:8501`.

## 🍳 How to Use

1. Open the Personal Chef application.
2. Enter the ingredients available in your kitchen.
3. Select the number of servings.
4. Choose your preferred cooking time.
5. Enter any dietary preferences, if applicable.
6. Click **Generate my recipe**.
7. Review the generated recipe, ingredient quantities, cooking instructions, and any web sources provided.

The AI may suggest optional ingredients when necessary. You do not need to use every ingredient you enter.

## 🔐 Environment Variables and Secrets

The application uses the following environment variables:

| Variable | Description |
|---|---|
| `GOOGLE_API_KEY` | API key for Google Gemini |
| `TAVILY_API_KEY` | API key for Tavily Search |

For local development, store these values in `.env`.

For Streamlit Community Cloud, configure them in the app's **Secrets** settings instead of uploading the `.env` file.

Example Secrets configuration:

```toml
GOOGLE_API_KEY = "your_actual_google_api_key"
TAVILY_API_KEY = "your_actual_tavily_api_key"
```

Never publish real API keys.

## ☁️ Deployment

The application is deployed using Streamlit Community Cloud.

To deploy your own instance:

1. Push the project to a GitHub repository.
2. Visit [Streamlit Community Cloud](https://share.streamlit.io/).
3. Connect your GitHub account.
4. Select the repository.
5. Set the main application file to `app.py`.
6. Add the required API keys in the app's Secrets settings.
7. Deploy the application.

The deployed application can be accessed using the live demo link provided at the top of this README.

## 🧪 Experimentation

The `Personal_Chef.ipynb` notebook is retained as the original experimentation and development record. The reusable AI agent implementation is maintained separately in `chef_agent.py`, while `app.py` provides the user-facing interface.

This structure separates experimentation, AI logic, and frontend development into distinct files.

## ⚠️ Limitations

- Recipe quality depends on the language model's output and the information available.
- API usage may be subject to provider quotas, rate limits, and pricing.
- Web search results may not always be accurate or relevant.
- Ingredient availability and food safety should be verified by the user.
- Generated recipes should be reviewed for allergies, dietary restrictions, and cooking requirements.

## 🔮 Future Improvements

- Add recipe images and richer visual presentation.
- Include cuisine selection, such as Indian, Italian, and Mexican.
- Add allergy-aware recipe filtering.
- Introduce nutritional information and calorie estimates.
- Support recipe history and saved favorites.
- Improve multi-turn conversation and ingredient substitutions.
- Add a shopping list for missing ingredients.

## 👨‍💻 Author

**Sagar Uppal**

GitHub: [Sagar-Uppal-26](https://github.com/Sagar-Uppal-26)

## 📄 License

This project is intended for educational and personal development purposes. A license can be added if the project is distributed under a specific open-source license.
