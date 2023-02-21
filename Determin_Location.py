import requests

def My_Location():
        ip_add =requests.get('https://api.ipify.org').text
        url = 'https://get.geojs.io/v1/ip/geo/'+ip_add+'.json'
        geo_q=requests.get(url)
        geo_d= geo_q.json()
        state = geo_d['city']
        country=geo_d['country']
        speak(f"Sir you are now in {state , country}")
        
My_Location()
