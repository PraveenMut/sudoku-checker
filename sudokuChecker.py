tester_correct = [[1,2,3],
                  [2,3,1],
                  [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]

def flatten(p):
  flattened_array = []
  for list in p:
    for n in list:
      flattened_array.append(n)
  return flattened_array

def string_checker(arr):
  p = flatten(arr)
  stored_var = 0
  for e in p:
    if isinstance(e, int):
      stored_var = e
    else:
      return False
  if stored_var > 0:
    return True

def max_element(p):
  flattened_arr = flatten(p)
  if len(p)+1 in flattened_arr:
    return False
  else:
    return True

def column_checker(p):
  matches = 0
  i = 0
  arr = flatten(p)
  for e in arr:
    matches = arr.count(e)
    if matches != len(p):
      return False
    else:
      i += 1
  return True

def row_transposer(p):
    transposed = map(list, zip(*p))
    return transposed

def row_checker(p):
    arr = row_transposer(p)
    matches = 0
    for e in arr:
        arr1 = e
        for n in arr1:
            matches = arr1.count(n)
            if matches != 1:
                return False
    return True    

def check_sudoku(p):
  if string_checker(p):
    if max_element(p):
      if column_checker(p) and row_checker(p):
        return True
  return False


print check_sudoku(tester_correct)
print check_sudoku(incorrect)
print check_sudoku(incorrect2)
print check_sudoku(incorrect3)
print check_sudoku(incorrect4)
print check_sudoku(incorrect5)