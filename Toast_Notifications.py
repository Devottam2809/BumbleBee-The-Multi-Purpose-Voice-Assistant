from winotify import Notification,audio

toast = Notification(app_id = "BumbleBee Launched",title = "Voice Assistant Activated",msg = "Hi! I am BumbleBee, your Mutipurpose Voice Assistant.",duration = "short",icon="C:/Users/91745/Desktop/Final Finished Code/Bumblebeeicon.png")
toast.set_audio(audio.Default,loop=False)
toast.add_actions(label = "Click Here",launch="C:/Users/91745/Desktop/Final Finished Code")

# to call the above use the predefined function toast.show()
