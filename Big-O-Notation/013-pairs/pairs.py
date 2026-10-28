def pairs(elements):
  unique = []

  for i in range(0, len(elements)):
    for j in range(i + 1, len(elements)):
      pairs = [elements[i], elements[j]]
    unique.append(pairs)
  return unique