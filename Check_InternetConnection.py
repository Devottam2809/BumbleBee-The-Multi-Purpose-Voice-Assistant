from urllib.request import urlopen

def check_internet():
    try:
        urlopen('https://www.google.com',timeout=1)
        return True
    except:
        return False
      
check_internet()
