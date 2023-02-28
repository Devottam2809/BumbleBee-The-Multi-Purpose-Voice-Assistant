import urllib.request
main_url="http://192.168.37.119"
def IOT(s):
    try:
        def sendRequest(url):
            a=urllib.request.urlopen(url)
        def ledon(a):
            if(a==4):
                sendRequest(main_url+"/turn_on/relay1")
            elif(a==5):
                sendRequest(main_url+"/turn_on/relay2")
            elif(a==6):
                sendRequest(main_url+"/turn_on/relay3")
            elif(a==7):
                sendRequest(main_url+"/turn_on/relay4")

        def ledoff(a):
            if(a==4):
                sendRequest(main_url+"/turn_off/relay1")
            elif(a==5):
                sendRequest(main_url+"/turn_off/relay2")
            elif(a==6):
                sendRequest(main_url+"/turn_off/relay3")
            elif(a==7):
                sendRequest(main_url+"/turn_off/relay4")
            # s=input()
        if('turn off' in s):
            if('first' in s):
                ledon(4)
            elif('fourth' in s):   
                ledon(5)
            elif('second' in s):
                ledon(6)
            elif('third' in s):
                ledon(7)
        elif('turn on' in s):
            if('fourth' in s):  
                ledoff(5)
            elif('first' in s):
                ledoff(4)
            elif('second' in s):
                ledoff(6)
            elif('third' in s):
                ledoff(7)
    except:
        return()