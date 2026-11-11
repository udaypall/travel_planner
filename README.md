

# CrewAI Travel Planner Agent

A simple AI-powered Travel Planner built using **Python, CrewAI, and OpenAI GPT-4o-mini**.

**GitHub Repository:** [https://github.com/udaypall/travel_planner](https://github.com/udaypall/travel_planner)

## 1. Project Overview

**Objective:** Build a first CrewAI agent that recommends exactly three places to visit in a city entered by the user.

**Technologies Used:**
- Python
- CrewAI
- OpenAI API
- GPT-4o-mini
- python-dotenv

## 2. Project Structure

```text
travel_planner/
│
├── venv/
├── travel_planner.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## 3. Features

- Accepts a city name through terminal input.
- Uses one AI Travel Planner Agent.
- Recommends exactly three tourist attractions.
- Provides descriptions and practical visiting tips.
- Executes tasks using CrewAI.

## 4. Installation

Clone the repository:

```cmd
git clone https://github.com/udaypall/travel_planner.git
cd travel_planner
```

Create and activate a virtual environment:

```cmd
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```cmd
pip install -r requirements.txt
```

## 5. Environment Configuration

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
MODEL=openai/gpt-4o-mini
```

**Important:** Never upload your `.env` file or expose your API key on GitHub.

## 6. Run the Application

```cmd
python travel_planner.py
```

Enter a city when prompted:

```text
Which city would you like to explore? Chennai
```

## 7. Sample Output

1. **Marina Beach** – Chennai's iconic beach, ideal for enjoying the sunrise and a leisurely stroll.

2. **Kapaleeshwarar Temple** – A historic temple showcasing beautiful Dravidian architecture.

3. **Fort St. George** – A historical landmark featuring colonial-era artifacts.

Each recommendation includes a practical visiting tip.

## 8. CrewAI Concepts Implemented

| Component | Purpose |
|---|---|
| Agent | Defines role, goal and backstory |
| Task | Defines the travel recommendation task |
| Expected Output | Specifies the required response format |
| Crew | Organizes the agent and task |
| kickoff() | Executes the CrewAI workflow |

## 9. Security

- API keys stored in environment variables.
- `.env` excluded using `.gitignore`.
- Virtual environment excluded from GitHub.

## 10. Future Enhancements

- Hotel recommendations.
- Restaurant and local food suggestions.
- Estimated travel budgets.
- Day-wise travel itineraries.
- Live weather integration.

## 11. Author

**Project:** CrewAI Travel Planner Agent

**Category:** AI Agent Development

**Framework:** CrewAI

**GitHub:** https://github.com/udaypall/travel_planner

---

*Built as part of a hands-on CrewAI learning assignment.*

