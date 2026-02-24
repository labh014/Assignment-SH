def analyze_startup(data: dict) -> dict:
    """
    Analyzes the startup research data and structures the investment evaluation.
    
    Args:
        data: A structured dictionary containing the agent's analysis results including SWOT analysis, investment score, risk level, and recommendation.
        
    Returns:
        dict: A structured dictionary of the final analysis.
    """
    return {
        "swot_analysis": data.get("swot_analysis", "SWOT analysis not provided."),
        "investment_score": data.get("investment_score", "Score not available."),
        "risk_level": data.get("risk_level", "Risk level not determined."),
        "recommendation": data.get("recommendation", "No recommendation provided.")
    }
