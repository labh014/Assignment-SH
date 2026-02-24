import os
from dotenv import load_dotenv
load_dotenv()

from google.adk.agents import Agent
from google.adk.tools import AgentTool
from sub_agents.research_agent import research_agent
from sub_agents.analysis_agent import analysis_agent
from sub_agents.report_agent import report_agent
from tools.save_tool import save_report

root_agent = Agent(
    name="startup_research_root",
    model="gemini-1.5-flash",
    description="Orchestrates the entire startup research, analysis, and reporting process.",
    instruction="""You are the root orchestrator for a startup research process.
Follow this exact workflow for the user's requested startup:
1. Pass the startup name to the research_agent to gather and extract data.
2. Pass the extracted data from step 1 to the analysis_agent to perform an investment analysis.
3. Pass the analysis from step 2 to the report_agent to generate a professional markdown report.
4. Finally, use the save_report tool to save the generated markdown report to a local file. Name the file '<startup_name>_report.md' where '<startup_name>' is the name of the startup.
5. Return a user friendly message indicating the process is complete and where the report was saved.""",
    tools=[AgentTool(research_agent), AgentTool(analysis_agent), AgentTool(report_agent), save_report]
)

if __name__ == "__main__":
    # Provides optional testing or entry point if needed
    pass
