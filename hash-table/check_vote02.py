voted = {}

def check_vote(name):
    if voted.get(name):
        print("User already voted")

