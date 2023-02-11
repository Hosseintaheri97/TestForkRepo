def hello_world(my_list : list) -> list:
  return list(filter(lambda item: 'hello' in item, my_list))
