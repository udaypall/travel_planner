
import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM

# Load environment variables
load_dotenv()

# Check API key
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY is missing. Please check your .env file.")

# Configure the language model
model_name = os.getenv("MODEL", "openai/gpt-4o-mini")
llm = LLM(model=model_name)

# Get city from user
city = input("Which city would you like to explore? ").strip()

if not city:
    raise ValueError("City name cannot be empty.")

# Create Travel Planner Agent
planner = Agent(
    role="Experienced Travel Planner",
    goal="Recommend exactly three interesting places to visit in the requested city.",
    backstory=(
        "You are an experienced travel planner who specializes in "
        "helping first-time visitors discover the best attractions in a city. "
        "You write for travelers who want practical, easy-to-follow "
        "recommendations rather than lengthy travel essays. "
        "You provide useful descriptions and simple visiting tips."
    ),
    llm=llm,
    verbose=True
)

# Create Task
travel_task = Task(
    description=(
        "Suggest exactly 3 places to visit in {city}. "
        "Choose popular and worthwhile attractions. "
        "For each place, provide its name, a short description "
        "explaining why it is worth visiting, and one practical travel tip. "
        "Do not include any additional places."
    ),
    expected_output=(
        "Exactly 3 numbered recommendations. "
        "Each recommendation must contain:\n"
        "1. Place name\n"
        "2. A short description (1-2 sentences)\n"
        "3. One practical visiting tip.\n"
        "Do not include an introduction, conclusion, or extra attractions."
    ),
    agent=planner
)

# Assemble the Crew
crew = Crew(
    agents=[planner],
    tasks=[travel_task],
    verbose=True
)

# Execute the Crew
result = crew.kickoff(inputs={"city": city})

# Display the result
print("\n========== YOUR TRAVEL PLAN ==========\n")
print(result)
