class Stack:

  def __init__(self, size, data_type=None) -> None:
    self.internal_data = [None for element in range(size)]
    self.tail = 0
    self.data_type = data_type
    self.size = size
    self.non_none = 0

  def __repr__(self) -> str:

    output_str = str()

    for index, element in enumerate(self.internal_data):
      if element != None:
        output_str += f"{element}"
        if (index + 1) != self.non_none:
          output_str += " <- "

    output_str += f"\n{self.non_none} non-None elements out of {self.size} sized array of {str(self.data_type)} data type elements."

    return output_str

  def __sizeof__(self) -> int:
    return self.size

  def __len__(self) -> int:
    return self.non_none

  def __eq__(self, __o: object) -> bool:
    if self.internal_data == __o.internal_data:
      return True
    else:
      return False

  def __iter__(self):
    return self.internal_data

  def __add__(self, other):
    if self.data_type == None and other.data_type == None:
      _dataType = None
    elif self.data_type == None and other.data_type != None:
      _dataType == other.data_type
    elif self.data_type != None and other.data_type == None:
      _dataType == self.data_type
    elif self.data_type == other.data_type:
      _dataType = self.data_type
    else:
      raise TypeError(
        f"Cannot combine stacks with data types of {self.data_type} and {other.data_type}"
      )

    _stack = Stack(size=(self.size + other.size), data_type=_dataType)
    for item in self.internal_data:
      if item != None:
        _stack.push(item)
    for item in other.internal_data:
      if item != None:
        _stack.push(item)

    return _stack

  def push(self, element) -> None:
    if self.data_type == None:
      self.data_type = type(element)
    if self.data_type != type(element):
      raise TypeError(
        "Element data type is not equal to standard element datatype.")
    else:
      if self.size == self.tail:
        raise OverflowError("Stack size reached")
      if self.internal_data[self.tail] == None:
        self.internal_data[self.tail] = element
        self.non_none += 1
        self.tail += 1
      else:
        raise BufferError("Cannot overwrite already stacked value")

  def pop(self, count=1):

    if count < 1: raise IndexError("Count cannot be lower than one.")
    if self.tail == 0: return None

    out_list = list()
    for _ in range(count):
      _element = self.internal_data[self.tail - 1]
      if type(_element) != None:
        out_list.append(_element)
        self.internal_data[self.tail - 1] = None
        self.non_none -= 1
        self.tail -= 1
      else:
        raise IndexError("Cannot return value of None")

    if count == 1:
      return out_list[0]
    else:
      return out_list

  def peek(self):
    return self.internal_data[self.tail - 1]
