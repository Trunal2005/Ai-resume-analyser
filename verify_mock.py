import requests

url = 'http://127.0.0.1:5000/'
files = {'resume': ('Trunal reaume 1.pdf', open('Trunal reaume 1.pdf', 'rb'))}

try:
    response = requests.post(url, files=files)
    if "MOCK ANALYSIS" in response.text:
        print("Mock fallback verified successfully.")
    else:
        print("Mock fallback failed. content:", response.text[:200])
except Exception as e:
    print(f"Request failed: {e}")
