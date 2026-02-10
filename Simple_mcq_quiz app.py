score = 0
wrong = 0  

print("Simple MCQ Quiz\n")
print("1. Which function is used to take input from the user in Python?")
print("a) print()")
print("b) input()") 
print("c) scan()")
print("d) read()")
ans = input("Answer: ").lower()
if ans == 'b':
    score += 1
else:
    wrong += 1
print("2. What type of loop is best suited for repeatedly showing the ATM menu?")
print("a) for loop")
print("b) while loop")
print("c) do-while loop")
print("d) if loop")
ans = input("Answer: ").lower()
if ans == 'b':
    score += 1
else:
    wrong += 1
print("3. Which statement checks if the balance is sufficient for withdrawal?")
print("a) for")
print("b) if")
print("c) while")
print("d) switch")
ans = input("Answer: ").lower()
if ans == 'b':
    score += 1
else:
    wrong += 1
print("4. What is a menu-driven program?")
print("a) A program with loops only")
print("b) A program that shows options to the user and performs actions based on choice")
print("c) A program that has no input")
print("d) A program that only prints messages")
ans = input("Answer: ").lower()
if ans == 'b':
    score += 1
else:
    wrong += 1
print("5. How do you stop the ATM program when the user selects 'Exit'?")
print("a) break")
print("b) continue")
print("c) return")
print("d) stop")
ans = input("Answer: ").lower()
if ans == 'a':
    score += 1
else:
    wrong += 1
print("6. Which of the following is a correct data type for balance?")
print("a) int")
print("b) str")
print("c) bool")
print("d) char")
ans = input("Answer: ").lower()
if ans == 'a':
    score += 1
else:
    wrong += 1
print("7. Which data type is best for storing the ATM PIN?")
print("a) int")
print("b) str")
print("c) float")
print("d) bool")
ans = input("Answer: ").lower()
if ans == 'b':
    score += 1
else:
    wrong += 1
print("8. What will balance = balance + deposit do?")
print("a) Subtract deposit from balance")
print("b) Add deposit to balance")
print("c) Multiply balance by deposit")
print("d) Divide balance by deposit")
ans = input("Answer: ").lower()
if ans == 'b':
    score += 1
else:
    wrong += 1

print("9. Which Python keyword is used to exit a loop?")
print("a) stop")
print("b) exit")
print("c) break")
print("d) continue")
ans = input("Answer: ").lower()
if ans == 'c':
    score += 1
else:
    wrong += 1
print("10. What happens if the withdrawal amount is greater than the balance?")
print("a) Withdrawal succeeds")
print("b) Program crashes")
print("c) Shows 'Insufficient balance'")
print("d) Balance becomes negative")
ans = input("Answer: ").lower()
if ans == 'c':
    score += 1
else:
    wrong += 1
print("11. Which operator is used to subtract money from balance?")
print("a) +")
print("b) -")
print("c) *")
print("d) /")
ans = input("Answer: ").lower()
if ans == 'b':
    score += 1
else:
    wrong += 1
print("12. What type of loop ensures the ATM menu keeps showing until exit?")
print("a) while loop")
print("b) for loop")
print("c) if statement")
print("d) switch case")
ans = input("Answer: ").lower()
if ans == 'a':
    score += 1
else:
    wrong += 1
print("13. How do you convert user input to float for money calculations?")
print("a) int(input())")
print("b) str(input())")
print("c) float(input())")
print("d) bool(input())")
ans = input("Answer: ").lower()
if ans == 'c':
    score += 1
else:
    wrong += 1
print("14. Which Python statement handles multiple conditions in ATM operations?")
print("a) if-elif-else")
print("b) while")
print("c) for")
print("d) switch")
ans = input("Answer: ").lower()
if ans == 'a':
    score += 1
else:
    wrong += 1
print("15. What happens if the user enters the wrong PIN?")
print("a) Access denied")
print("b) Balance is shown")
print("c) Deposit allowed")
print("d) Program crashes")
ans = input("Answer: ").lower()
if ans == 'a':
    score += 1
else:
    wrong += 1
print("16. Which of the following is NOT an ATM operation?")
print("a) Deposit")
print("b) Withdraw")
print("c) Check balance")
print("d) Play game")
ans = input("Answer: ").lower()
if ans == 'd':
    score += 1
else:
    wrong += 1
print("17. What will balance -= withdraw do?")
print("a) Add withdraw to balance")
print("b) Subtract withdraw from balance")
print("c) Multiply balance by withdraw")
print("d) Divide balance by withdraw")
ans = input("Answer: ").lower()
if ans == 'b':
    score += 1
else:
    wrong += 1
print("18. Which of the following is used to display a message in Python?")
print("a) print()")
print("b) input()")
print("c) scan()")
print("d) show()")
ans = input("Answer: ").lower()
if ans == 'a':
    score += 1
else:
    wrong += 1
print("19. What is the initial step in ATM program?")
print("a) Display menu")
print("b) Initialize balance")
print("c) Withdraw money")
print("d) Deposit money")
ans = input("Answer: ").lower()
if ans == 'b':
    score += 1
else:
    wrong += 1
print("20. Why do we use loops in ATM programs?")
print("a) To perform multiple transactions until user exits")
print("b) To store PINs")
print("c) To display welcome message once")
print("d) To crash the program")
ans = input("Answer: ").lower()
if ans == 'a':
    score += 1
else:
    wrong += 1

# --- Final Output ---
print(f"\nYou scored {score} out of 20")
print(f"Number of wrong answers: {wrong}")

