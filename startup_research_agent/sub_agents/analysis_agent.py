from google.adk.agents import Agent
from tools.analysis_tool import analyze_startup

analysis_agent = Agent(
    name="analysis_agent",
    model="gemini-1.5-flash",
    description="Analyzes startup research data to provide investment insights.",
    instruction="""You are an expert investment analyst. You will receive structured research data about a startup.
1. Analyze the data to provide the following:
   - A detailed SWOT analysis.
   - An investment score out of 10.
   - A risk level (Low, Medium, High).
   - A final investment recommendation.
2. Use the analyze_startup tool to structure your analysis. Pass a dictionary with keys: 'swot_analysis', 'investment_score', 'risk_level', 'recommendation' into the tool, and return the result of the tool.""",
    tools=[analyze_startup]
)
