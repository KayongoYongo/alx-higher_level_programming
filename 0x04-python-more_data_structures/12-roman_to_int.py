#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ans = 0
    s = roman_string
    for i in range(len(roman_string)):
        if i+1 != len(s) and d[s[i]] < d[s[i + 1]]:
            ans = ans - d[s[i]]
        else:
            ans = ans + d[s[i]]
    return ans
