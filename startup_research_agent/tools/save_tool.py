import os

def save_report(filename: str, content: str) -> str:
    """
    Saves the generated markdown report to a local file.
    
    Args:
        filename: The name of the file to save (e.g., 'startup_report.md').
        content: The markdown content to write to the file.
        
    Returns:
        str: A success message indicating where the file was saved.
    """
    # Ensure filename has .md extension
    if not filename.endswith('.md'):
        filename += '.md'
        
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"Report successfully saved to {os.path.abspath(filename)}"
    except Exception as e:
        return f"Error saving report: {str(e)}"
