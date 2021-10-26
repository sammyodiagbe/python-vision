string = "Odiagbe Samson"
iterator = iter(string)
response = 'Yes'

while input('Do you want to proceed ?') not in ['No','no'] :
    print(next(iterator))

print('Alright we done with iteration')