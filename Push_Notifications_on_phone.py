from pushbullet import PushBullet

def push_notifications():

    API_KEY="o.YBvGUX8Xdd5PGfhO08CQ506Ldqe6FY4N"
    file="database.txt"
    with open(file,mode='r') as f:
        text=f.read()

    pb=PushBullet(API_KEY)
    push=pb.push_note("Please Remember",text)
    
push_notifications()

# for this install push bullet application on your phone .
# connect the app and sign up on push bullet website with the same email account
