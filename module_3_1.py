calls = 0
def count_calls():
    global calls
    calls = calls + 1
    return calls
def string_info(string):
    calls = count_calls()
    long_strUP_strdown = (len(string), string.upper(), string.lower())
    return long_strUP_strdown
def is_contains (string, list_to_search):
    calls = count_calls()
    m1 = []
    m = (len(string), string.upper(), string.lower())
    m1 = list(m)
    for i in range(0, len(list_to_search)):
        if list_to_search[i].upper() == m1[1]:
            tr_fal = 'True'
        else:
            tr_fal = 'False'
    return tr_fal
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)



