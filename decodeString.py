def decodeString(string):

  indicies = []
  for index, value in enumerate(string):
  # save indicies of the numbers
    if value.isdigit() and not string[index + 1].isdigit():
      indicies.append(index)

  while indicies:
    # find start bracket [ next to the last number in string
    start_bracket = max(indicies) + 1

    # find end bracket ]
    for index, value in enumerate(string):
      if index > start_bracket and value == ']':
        end_bracket = index
        break

    # remove ending parethesis
    string = string[:end_bracket] + string[end_bracket + 1:]

    # remove starting parethesis
    string = string[:start_bracket] + string[start_bracket + 1:]

    # if multiplier <= 9 i.e. single digit
    if not string[start_bracket - 2].isdigit():
      multiplier = int(string[start_bracket - 1])
      string_to_multiply = string[start_bracket:end_bracket - 1]
      print "mult single"

    # if multiplier > 9 i.e. multi digit
    else:
      multiplier = ''
      for index, value in reversed(list(enumerate(string))):
        # print index, value, start_bracket, end_bracket
        if index < start_bracket and value.isdigit():
          multiplier += value
          # stop the loop once the mult digit multiplier ends
          if not string[index - 1].isdigit():
            break
          # print value
      multiplier = int(multiplier[::-1])
      string_to_multiply = string[start_bracket:end_bracket - 1]

    # replace multiplier and string chuck with multiplied string chunk
    x = len(str(multiplier))
    replaced = string[start_bracket - x:end_bracket - 1]
    insert = multiplier * string_to_multiply
    string = string.replace(replaced, insert)

    # remove number index
    indicies.pop()
  return string