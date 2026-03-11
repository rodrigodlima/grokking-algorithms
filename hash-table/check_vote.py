# This is an example of voting system, to check if someone already voted
voted = {}


def check_elector(name):
    if voted.get(name):
        print("Already voted")
    else:
        print("Can vote")
        voted[name] = name


check_elector("Mike")
check_elector("Rodrigo")
check_elector("Mike")  # The message ‘Already voted’ should appear here
