from bs4 import BeautifulSoup

def temperature():
    search = 'Temperature in kanpur'
    url = f"https://www.google.com/search?q= + {search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text , "html.parser")
    temperature = data.find("div",class_= "BNeawe").text
    speak(f"The temperature is :{temperature}")
  
temperature()
