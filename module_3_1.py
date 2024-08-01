calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    _string = str(string)
    _tuple = (len(_string), _string.upper(), _string.lower())
    count_calls()
    return _tuple

def is_contains(string,  list_to_search):
    string = str(string).lower()
    list_to_search = list(list_to_search)
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            result = True
            break
        else:
            result = False
            continue
    return result

print(string_info('Program'))
print(string_info('Study'))
print(string_info('Python'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches

print(calls)