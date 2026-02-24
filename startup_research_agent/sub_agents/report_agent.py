from google.adk.agents import Agent
from tools.report_tool import generate_markdown_report

report_agent = Agent(
    name="report_agent",
    model="gemini-1.5-flash",
    description="Generates a professional markdown report from the startup analysis data.",
    instruction="""You are a technical report writer. You will receive an investment analysis dictionary about a startup.
1. Use the generate_markdown_report tool to generate a markdown string based on the data.
2. Return the generated markdown string.""",
    tools=[generate_markdown_report]
)
