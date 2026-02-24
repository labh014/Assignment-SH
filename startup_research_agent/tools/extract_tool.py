import json

def extract_startup_info(data: str) -> dict:
    """
    Extracts structured startup information.
    
    Args:
        data: A JSON formatted string containing keys for overview, founders, funding, competitors, and market.
        
    Returns:
        dict: The parsed dictionary containing the extracted startup information.
    """
    try:
        # Try to parse the string as JSON
        parsed_data = json.loads(data)
        if isinstance(parsed_data, dict):
            return parsed_data
    except Exception:
        pass
        
    return {
        "raw_response": data,
        "overview": "Information gathered but could not be perfectly structured.",
        "founders": "N/A",
        "funding": "N/A",
        "competitors": "N/A",
        "market": "N/A"
    }
