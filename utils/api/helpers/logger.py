
def log_request(response):
    print(f"URL: {response.url}")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text[:200]}")