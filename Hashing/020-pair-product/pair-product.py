def pair_product(numbers, target_product):
  prev = {}

  for index, num in enumerate(numbers):
    comp = target_product / num
    if comp in prev: 
      return (index, prev[comp])
    prev[index] = num

  return prev