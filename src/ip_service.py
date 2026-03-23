import requests

def get_my_ip_data():
    """Connects to ipapi.co to fetch public network details."""
    url = "https://ipapi.co/json/"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Network error: {e}"}
