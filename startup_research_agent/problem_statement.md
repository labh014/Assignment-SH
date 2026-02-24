# Startup Research Agent: Problem Statement

## Problem Definition
Investors and business analysts often spend significant time manually researching startups. This involves searching for company overviews, founder details, funding histories, competitors, and market landscape. Synthesizing this disparate information into a coherent analysis and professional report is a slow, labor-intensive process prone to human error and bias.

## Objective
To automate the end-to-end process of startup research, analysis, and report generation using a Multi-Agent System (MAS). The system should take a startup name as input and output a comprehensive, professional investment research report.

## Solution Approach
We build a completely automated system using Google's Agent Development Kit (ADK) and Gemini models. The solution involves a coordinated workflow where specialized AI agents handle distinct parts of the task:
1. **Information Gathering:** Searching the web to extract factual data about the startup.
2. **Analysis:** Processing the gathered data to evaluate the startup's potential, risks, and market position (e.g., SWOT analysis, investment score).
3. **Report Generation:** Formatting the analysis into a polished, easily readable Markdown report.
4. **Persistence:** Saving the final report to the local file system for user access.

## Agent Architecture Explanation
The system employs a hierarchical Multi-Agent Architecture driven by a Root Agent:

- **Root Agent (`startup_research_root`)**: Orchestrates the entire workflow. It receives the user's input (startup name) and delegates tasks sequentially to the sub-agents.
- **Research Agent (`research_agent`)**: Uses the built-in `google_search` tool and a custom extraction tool to find and structure raw data about the startup (overview, founders, funding, competitors, market).
- **Analysis Agent (`analysis_agent`)**: Takes the structured data from the Research Agent and performs a deep business evaluation, outputting a SWOT analysis, investment score, and recommendations.
- **Report Agent (`report_agent`)**: Converts the analytical insights into a professional Markdown report, and finally utilizes a custom tool to save the report to the disk.
