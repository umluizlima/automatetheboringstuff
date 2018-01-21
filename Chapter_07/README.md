https://automatetheboringstuff.com/chapter7/

1. The function that creates Regex objects is the .compile() function.
2. Raw strings are often used when creating Regex objects because otherwise it would interpret some characters as escape characters.
3. The search() method returns any regex matches to the given string.
4. To get the actual strings that match the pattern from a Match object you must use the group(), groups() or findall() methods.
5. Group 0 covers all match groups. Group 1 covers the first parentheses delimited group, and group 2 covers the second.
6. To specify that you want a regex to match actual parentheses and period characters you must use escape characters.
7. The findall() method will return a list of tuples of strings if the regex specifies match groups. If not, it returns a list of strings.
8. The | (pipe character) signify a bit-wise operator, allowing to apply boolean logic to the regex.
9. The ? character means that the given match might not exist, or return the non-greedy version of the curly brackets.
10. The + character returns matches of one or more occurrences, while the * character returns matches of zero or more occurrences.
11. {3} returns a match if the given string repeats the regex exactly 3 times, while {3,5} returns a match if it repeats 3, 4 or 5 times.
12. The following shorthand character classes signify: \d = [0-9]	\w = [a-zA-Z0-9_]	\s = any space, tab or newline character
13. The following shorthand character classes signify: \D = [^0-9]	\W = [^a-zA-Z0-9_]	\S = any character that is not a space, tab or newline
14. To make a regular expression case-insensitive you must pass re.IGNORECASE or re.I as argument after the compile regex.
15. The . character normally matches to any character except \n. If re.DOTALL is passed as the second argument to re.compile() it will also math \n.
16. The .* uses greedy mode, trying to match as much text as possible, while .*? uses non-greedy mode.
17. The character class syntax to match all numbers and lowercase letters is: [0-9a-z]
18. If numRegex = re.compile(r'\d+'), numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens') will return 'X drummers, X pipers, five rings, X hens'.
19. Passing re.VERBOSE as second argument to the compile() method will allow the use of whitespace and comments inside the regular expression string.
20. numRegex = re.compile(r'^(\d{,3})(,(\d{3}))*$')
21. nakaRegex = re.compile(r'[A-Z][a-z]+ Nakamoto')
22. doRegex = re.compile(r'(Alice|Bob|Carol) (eats|pets|throws) (apples|cats|baseballs).', re.I)