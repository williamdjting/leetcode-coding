#1
# Your task: fill in the blanks
# class Person:
#     def __init__(self, name: str, age: int) -> None:
#         self.name = name
#         self.age = age

#     def introduce(self) -> None:
#         print(f"Hi my name is {self.name} and I am {self.age} years old.")  
#         # Use self to access name and age

# # Create an instance and call the method


# # person = Person("dog", 12)

# # person.introduce()

#     def is_adult(self) -> None:
#             if self.age >= 18:
#                 print(f"{self.name} is an adult.")
#             else:
#                 print(f"{self.name} is a minor.")

# # Try it
# p = Person("Alice", 17)
# p.introduce()
# p.is_adult()

#2
class BankAccount:
    def __init__(self, owner: str, balance: int) -> None:
        self.owner = owner
        self.balance = balance


    def deposit(self, amount: int) -> None:
        self.amount = amount

        self.balance = self.balance + self.amount


    def withdraw(self, amount: int) -> None:
        self.amount = amount

        self.balance = self.balance - self.amount




    def get_balance(self) -> int:


        print(f"this is the value of your bank balance {self.balance}")
        return self.balance


# Expected usage:
account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(200)
account.get_balance()  # Should show 1300-