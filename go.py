import urllib.request
import json

url = "https://godaddy.com"
token = "gd_pat_UetkT8lL8Coo7nM0LdCkgDqqluBaEMed0lmExAiOluv_66ed2b54"

headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/json"
}

req = urllib.request.Request(url, headers=headers, method="GET")

try:
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        print("\n✅ SUCCESS!")
        print(f"Domain: {data.get('domain')}")
        print(f"Available: {data.get('available')}\n")
except urllib.error.HTTPError as e:
    print(f"\n❌ API Error Code: {e.code}")
    print(e.read().decode())
except Exception as e:
    print(f"\n❌ Connection Error: {e}")
