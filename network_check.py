import urllib.request
import urllib.error

# 1. Define a List of websites to monitor
websites = [
    "https://www.google.com",
    "https://www.github.com",
    "https://this-site-surely-does-not-exist.com"
]

print("Starting SRE Monitoring Script...\n")
print("-" * 40)

# 2. Loop through each website in our list
for site in websites:
    # 3. Fault Tolerance: 'Try' to connect
    try:
        response = urllib.request.urlopen(site)
        status = response.getcode()
        
        if status == 200:
            print(f"[SUCCESS] {site} is ONLINE (Status: 200)")
        else:
            print(f"[WARNING] {site} returned unexpected status: {status}")
            
    # Catch HTTP Errors
    except urllib.error.HTTPError as e:
        print(f"[ERROR]   {site} is DOWN (HTTP Error: {e.code})")
        
    # Catch Connection/DNS Errors
    except urllib.error.URLError as e:
        print(f"[ERROR]   {site} is UNREACHABLE (Reason: {e.reason})")
        
    # Catch any other unexpected crashes
    except Exception as e:
        print(f"[CRITICAL] {site} failed with an unexpected error: {e}")

print("-" * 40)
print("Monitoring check complete.")






	 

