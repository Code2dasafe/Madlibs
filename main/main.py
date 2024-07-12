# string concatenation (aka how to put strings together)
# suppose we want to create a string that says "subscribe to _____"
# youtuber = "Theodore Morgan" # some string variable 

# a few ways to do this
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subcribe to {youtuber}")
adj = input("Adjective: ")
verb = input("Verb: ")
verb2 = input("Another verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \nI love to {verb}. Stay hydrated and {verb2} like you are {famous_person}!"
print(madlib)