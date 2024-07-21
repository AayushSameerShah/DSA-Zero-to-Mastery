counter = 0
def inception():
    global counter
    if counter > 3:
        return counter
    counter += 1
    return inception()

print(inception())