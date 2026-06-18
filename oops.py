# custom Exception 
class InsufficientFundsError(Exception):
    pass


class OverdraftLimitError(Exception):
    pass
# Parent Class 
class BankAccount:   #Class
    

    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = float(balance)   # Encapsulation 

        self.__transactions = [
            f"Opening deposit: +{balance:.1f}"
        ]

    def deposit(self, amount):
        
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        self.__balance += amount

        self.__transactions.append(
            f"Deposit: +{amount:.1f}"
        )

    def withdraw(self, amount):
        
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        if amount > self.__balance:
            raise InsufficientFundsError(
                "Insufficient balance."
            )

        self.__balance -= amount

        self.__transactions.append(
            f"Withdrawal: -{amount:.1f}"
        )

    def get_balance(self):
        
        return self.__balance

    def get_owner(self):
        
        return self.__owner

    def get_statement(self):
        
        print("\n--- Statement ---")

        running_balance = 0

        for transaction in self.__transactions:

            print(transaction)

            if "+" in transaction:
                amount = float(
                    transaction.split("+")[1]
                )
                running_balance += amount

            elif "-" in transaction:
                amount = float(
                    transaction.split("-")[1]
                )
                running_balance -= amount

            print(f"Balance: {running_balance:.1f}")

    def _add_transaction(self, message):
       
        self.__transactions.append(message)

    def _set_balance(self, balance):
        
        self.__balance = balance

    def transfer(self, amount, target_account):
        

        self.withdraw(amount)
        target_account.deposit(amount)

        print(
            f"Transferred Rs.{amount} from "
            f"{self.get_owner()} to "
            f"{target_account.get_owner()}"
        )

# Inheritance 

class SavingsAccount(BankAccount):
    

    MIN_BALANCE = 500

    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
# Polymorphism 
    def withdraw(self, amount):

        if self.get_balance() - amount < self.MIN_BALANCE:

            raise InsufficientFundsError(
                "Cannot withdraw. Min balance "
                "of Rs.500 must be maintained."
            )

        new_balance = self.get_balance() - amount

        self._set_balance(new_balance)

        self._add_transaction(
            f"Withdrawal: -{amount:.1f}"
        )

    def add_interest(self):

        interest = (
            self.get_balance() *
            self.interest_rate
        )

        new_balance = self.get_balance() + interest

        self._set_balance(new_balance)

        self._add_transaction(
            f"Interest credit: +{interest:.1f}"
        )



class CurrentAccount(BankAccount):
    

    def __init__(
        self,
        owner,
        balance,
        overdraft_limit
    ):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):

        new_balance = self.get_balance() - amount

        if new_balance < -self.overdraft_limit:

            raise OverdraftLimitError(
                f"Overdraft limit of "
                f"Rs.{self.overdraft_limit} exceeded."
            )

        self._set_balance(new_balance)

        self._add_transaction(
            f"Withdrawal: -{amount:.1f}"
        )

# Test case 1 

print("\nTEST CASE 1")

try:
    acc = SavingsAccount(        # Object 
        "Alice",
        1000,
        0.05
    )

    acc.deposit(500)
    acc.withdraw(900)

    print(
        "Balance:",
        acc.get_balance()
    )

    acc.withdraw(200)

except InsufficientFundsError as e:
    print(e)

# test case 2

print("\nTEST CASE 2")

try:
    acc = CurrentAccount(
        "Bob",
        500,
        2000
    )

    acc.withdraw(2000)

    print(
        "Balance:",
        acc.get_balance()
    )

    acc.withdraw(600)

except OverdraftLimitError as e:
    print(e)


# Test case 3

print("\nTEST CASE 3")

acc = SavingsAccount(
    "Carol",
    2000,
    0.05
)

acc.add_interest()

print(
    "Balance:",
    acc.get_balance()
)

acc.get_statement()


# Transfer Test
print("\nTRANSFER TEST")

savings = SavingsAccount(
    "Alice",
    5000,
    0.05
)

current = CurrentAccount(
    "Bob",
    1000,
    2000
)

savings.transfer(
    1000,
    current
)

print(
    "Alice Balance:",
    savings.get_balance()
)

print(
    "Bob Balance:",
    current.get_balance()
)
