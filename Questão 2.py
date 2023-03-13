#Questão_2
def fibonacci(n):
  fibs_lst = [0,1]
  if n <= len(fibs_lst) - 1 :
    return n
  else:
    while n > len(fibs_lst) - 1:
      next_fib = fibs_lst[-1] + fibs_lst[-2]
      fibs_lst.append(next_fib)
    if n in fibs_lst:
      print(f"Ei, o seu número ({n}) está na lista de fibonacci! =)")
    return fibs_lst

print(fibonacci(7))



