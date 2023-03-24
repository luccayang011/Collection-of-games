def add(n1, n2):
  return n1 + n2

def substract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def devide(n1, n2):
  return n1 / n2

operations = {}

operations["+"] = add
operations["-"] = substract
operations["*"] = multiply
operations["/"] = devide

def calculator():
  num1 = float(input("what is the first number? "))
  num2 = float(input("what is the second number? "))
  for symbol in operations:
    print(symbol)
  
  operation_symbol = input("pick an operation from the line above: ")
  
  calculation_function = operations[operation_symbol]
  result = calculation_function(num1, num2)
  
  print(f"{num1} {operation_symbol} {num2} = {result }")
  
  calculation_finished = False
  
  while not calculation_finished:
    should_continue = input("type y to continue, type n to start a new calculation ").lower()
    if should_continue == 'n':
      calculation_finished = True
      calculator() # recursion
    else:
      num3 = float(input("what is the number? "))
      for symbol in operations:
        print(symbol)
      
      operation_symbol = input("pick an operation from the line above: ")
      
      calculation_function = operations[operation_symbol]
      result_old = result
      result = calculation_function(result, num3)
      print(f"{result_old} {operation_symbol} {num3} = {result}")

calculator()
