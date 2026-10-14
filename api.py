import requests


def fetch_all_elements():
    """
    Fetches all element records from the API raw data and returns a dictionary of elements
    keyed by lowercase element symbols (e.g., 'h', 'he', 'fe').
    """
    try:
        response = requests.get("https://api.periodictableofelements.org/elements", timeout=10)
        response.raise_for_status()
        elements = response.json()
        
        
        # Start with an empty dictionary BEFORE the loop opens
        element_cache = {}

        for el in elements:
            # Extract the symbol and convert it to lowercase to use as the key
            symbol_key = el["symbol"].lower()
            
            # Map the symbol key directly to the entire element's data
            element_cache[symbol_key] = el

        # Return the entire dictionary after the loop finishes completely
        return element_cache

        
    except requests.RequestException as error:
        print(f"API Error: Failed to fetch element data ({error})")
        return None

def get_element_data(symbol): # fetches a single element record from the cached database i.e. element_cache
    """
    Safely retrieves single element record from cached database.
    """
    elements_db = fetch_all_elements()  # Ensure the database is fetched before accessing it
    return elements_db.get(symbol.lower())

if __name__ == "__main__":
    fetch_all_elements()  # Fetch elements when the script is run directly