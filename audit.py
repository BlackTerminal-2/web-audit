import requests

url = input("Website URL: ").strip()

# Automatically add https:// if missing
if not url.startswith(("http://", "https://")):
    url = "https://" + url

try:
    response = requests.get(
        url,
        timeout=10,
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )

    print("=" * 40)
    print("Website :", url)
    print("Status   :", response.status_code)
    print("Server   :", response.headers.get("Server", "Unknown"))
    print("=" * 40)

    security_headers = {
        "Content-Security-Policy": "CSP",
        "Strict-Transport-Security": "HSTS",
        "X-Frame-Options": "Clickjacking Protection",
        "X-Content-Type-Options": "MIME Protection",
        "Referrer-Policy": "Referrer Policy",
        "Permissions-Policy": "Permissions Policy"
    }

    print("\nSecurity Header Check\n")

    for header, desc in security_headers.items():
        if header in response.headers:
            print(f"[OK] {header}")
        else:
            print(f"[MISSING] {header} ({desc})")

except requests.exceptions.RequestException as e:
    print("\nConnection Error:")
    print(e)
