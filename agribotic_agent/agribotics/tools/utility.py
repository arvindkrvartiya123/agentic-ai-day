import  os
import requests
from typing import Dict
api_key=os.getenv('SERPER_KEY')

def get_weather(city: str) -> Dict:

    # Best Practice: Log tool execution for easier debugging
    print(f"--- Tool: get_weather called for city: {city} ---")
    city_normalized = city.lower().replace(" ", "") # Basic input normalization

    # Mock weather data for simplicity (matching Step 1 structure)
    mock_weather_db = {
        "newyork": {"status": "success", "report": "The weather in New York is sunny with a temperature of 25°C."},
        "london": {"status": "success", "report": "It's cloudy in London with a temperature of 15°C."},
        "tokyo": {"status": "success", "report": "Tokyo is experiencing light rain and a temperature of 18°C."},
        "chicago": {"status": "success", "report": "The weather in Chicago is sunny with a temperature of 25°C."},
        "toronto": {"status": "success", "report": "It's partly cloudy in Toronto with a temperature of 30°C."},
        "chennai": {"status": "success", "report": "It's rainy in Chennai with a temperature of 15°C."},
 }

    # Best Practice: Handle potential errors gracefully within the tool
    if city_normalized in mock_weather_db:
        return mock_weather_db[city_normalized]
    else:
        return {"status": "error", "error_message": f"Sorry, I don't have weather information for '{city}'."}

def search_google_serper(query: str) -> dict:
    """
    Search the web using the Google Serper API.

    Use Case:
        This function allows you to perform a Google search programmatically via Serper.dev's API. 
        It is useful for applications that need access to real-time web results, such as chatbots, 
        AI agents, or data enrichment pipelines.

    Parameters:
        query (str): The search query string to send to Google (e.g., "OpenAI ChatGPT 2025").

    Returns:
        dict: A dictionary containing the structured search results from Serper API.
              Typically includes:
                - 'organic': list of web results
                - 'knowledgeGraph': entity info (if available)
                - 'answerBox': direct answers (if any)

    Raises:
        requests.exceptions.RequestException: If the API call fails due to network issues.
        ValueError: If the API returns an error response or invalid data.

    Example:
        >>> results = search_google_serper("latest AI news", "your_api_key")
        >>> for result in results["organic"]:
        >>>     print(result["title"], result["link"])
    """

    url = "https://google.serper.dev/search"
    headers = {
        "X-API-KEY": api_key,
        "Content-Type": "application/json"
    }
    payload = {
        "q": query
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return {"status": "success", "search_result": response.json()}
    
    except requests.exceptions.RequestException as e:
        raise requests.exceptions.RequestException(f"Request failed: {e}")
    except ValueError as e:
        raise ValueError(f"Invalid response data: {e}")

def buy_crop():
    pass
def sale_crop():
    pass
def buy_fertilizer():
    pass