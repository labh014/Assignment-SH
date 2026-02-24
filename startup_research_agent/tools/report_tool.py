def generate_markdown_report(data: dict) -> str:
    """
    Generates a professional markdown report from the analyzed startup data.
    
    Args:
        data: A dictionary containing the analytical insights (SWOT, score, risk, etc.)
        
    Returns:
        str: A formatted markdown report.
    """
    report = f"""# Startup Investment Research Report

## Executive Summary
**Investment Score:** {data.get('investment_score', 'N/A')}
**Risk Level:** {data.get('risk_level', 'N/A')}

## Recommendation
{data.get('recommendation', 'N/A')}

## SWOT Analysis
{data.get('swot_analysis', 'N/A')}

---
*Report generated autonomously by Startup Research Agent.*
"""
    return report
