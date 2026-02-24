from google.adk.agents import Agent
from google.adk.tools import google_search
from tools.extract_tool import extract_startup_info

research_agent = Agent(
    name="research_agent",
    model="gemini-1.5-flash",
    description="Gathers comprehensive data about a startup from the internet.",
    instruction="""You are a startup research assistant. 
1. Use the google_search tool to find the following information about the given startup:
   - Company overview
   - Founders
   - Funding history
   - Competitors
   - Market landscape
2. Once you have gathered sufficient information, use the extract_startup_info tool to format your findings. Ensure you pass a well-formatted JSON string with keys: 'overview', 'founders', 'funding', 'competitors', 'market' into the tool. Return the result of the tool.""",
    tools=[google_search, extract_startup_info]
)
