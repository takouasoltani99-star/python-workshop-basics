
def my_lists(keys,values):
 if len(keys)==len(values):
  return dict(zip(keys,values))
 else:
  print("error lists must have the same length")


