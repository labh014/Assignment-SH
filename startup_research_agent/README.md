# Startup Research Agent

## Project Description
The Startup Research Agent is a powerful Multi-Agent System (MAS) built with Google's Agent Development Kit (ADK) and Gemini models. It automates the process of researching, analyzing, and reporting on startups. By simply providing a startup name, the system autonomously searches the internet, extracts key business data, performs an investment analysis, and generates a structured Markdown report.

## Architecture Explanation
This project follows a delegated multi-agent architecture orchestrated by a single Root Agent. The flow of information is as follows:
User Input -> Root Agent -> Research Agent -> Analysis Agent -> Report Agent -> Saved File.

## Agent Roles
- **Root Agent (`startup_research_root`)**: The main orchestrator that manages the flow between sub-agents.
- **Research Agent (`research_agent`)**: Responsible for gathering data from the internet (overview, founders, funding, competitors, market).
- **Analysis Agent (`analysis_agent`)**: Evaluates the gathered data to provide a SWOT analysis, investment score, risk level, and recommendation.
- **Report Agent (`report_agent`)**: Formats the analysis into a professional Markdown document and saves it locally.

## Tool Roles
- **`google_search`**: Built-in ADK tool used by the Research Agent to query the internet.
- **`extract_startup_info`**: Custom tool to structure the raw research data into a precise dictionary format.
- **`analyze_startup`**: Custom tool to perform structured logic and analysis on the extracted data.
- **`generate_markdown_report`**: Custom tool to convert analytical structured data into a Markdown string.
- **`save_report`**: Custom tool that persists the final Markdown string into a local file.

## Setup Instructions
1. Ensure you have Python 3.11+ installed.
2. Clone or download this project.
3. Rename `.env.example` to `.env` and add your valid `GOOGLE_API_KEY`.

## Installation Steps
```bash
pip install -r requirements.txt
```

## Run Instructions
To run the agent via the ADK CLI:
```bash
adk run startup_research_root
```

To run the agent with the ADK Web UI:
```bash
adk web
```
