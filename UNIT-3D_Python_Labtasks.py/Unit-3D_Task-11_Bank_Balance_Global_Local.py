balance = 1000
def deposit(amount):
    global balance
    balance += amount
    print("Balance after deposit: ", balance)
def show_local_balance():
    balance = 500  
    print("Local balance inside function: ", balance)
print("Initial global balance: ", balance)

deposit(500)

show_local_balance()

print("Global balance after local function call: ", balance)