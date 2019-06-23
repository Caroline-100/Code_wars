def remove_char(s):
    s = s[:-1]
    s = s[1:]
    
    return s


assert remove_char('eloquent') == 'loquen'
assert remove_char('country') == 'ountr'
assert remove_char('person') == 'erso'
assert remove_char('place' )== 'lac'
assert remove_char('ok') == ''