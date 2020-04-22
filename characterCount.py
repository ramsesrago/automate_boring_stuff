import pprint

message = 'Message to count the characters'
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character]+=1
    
pprint.pprint(count)


