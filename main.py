# Dalton Wright
# 10/29/24
# While vs recursion

def while_substitution(num):
  rec = []
  current_num = num

  while True:
    if current_num == 0:
        print("\nBASE CASE REACHED\n")
        break
    print(f"Recursing; num = {current_num}")
    rec.append(current_num)
    current_num-=1
  
  while rec:
    current_num= rec.pop()
    print(f"Returning; num = {current_num}")

if __name__=="__main__":
  while_substitution(5)