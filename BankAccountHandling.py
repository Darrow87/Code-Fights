# Write a method takes an array of bank account and executes withdraw, deposit, and transfer requests.

# If an error arises (e.g. negative account balance or account does not exist), return <-1> if 1 was the failing account etc.

def bankRequests(accounts, requests):

# models

# transfer
  def transfer(accounts, account1, account2, sum):
    account1 = int(account1)
    account2 = int(account2)
    sum = int(sum)

    for index, value in enumerate(accounts, 1):
      if account1 == index:
        accounts[index - 1] -= sum

      if account2 == index:
        accounts[index - 1] += sum

# withdraw
  def withdraw(accounts, account1, sum):
    account1 = int(account1)
    sum = int(sum)

    checkAccountExists(accounts, account1, account2=0)

    for index, value in enumerate(accounts, 1):
      if account1 == index:
        accounts[index - 1] -= sum

        checkNegativeBalance(accounts, account1)

# deposit
  def deposit(accounts, account1, sum):
    account1 = int(account1)
    sum = int(sum)

    checkAccountExists(accounts, account1, account2=0)

    for index, value in enumerate(accounts, 1):
      if account1 == index:
        accounts[index - 1] += sum

# errors
  def checkAccountExists(accounts, account1, account2=None):
    if int(account1) > len(accounts):
      return [(r + 1)*-1]
    elif account2 is not None and int(account2) > len(accounts):
      return [(r + 1)*-1]

  def checkNegativeBalance(accounts, account1):
    if accounts[int(account1) - 1] < 0:
      # print "account has negative balance"
      return [(r + 1)*-1]


# Controller
  for r in range(0, len(requests)):
    requests[r] = requests[r].split()

    if requests[r][0] == 'deposit':
      if checkAccountExists(accounts, requests[r][1]) is not None:
        return checkAccountExists(accounts, requests[r][1])

      deposit(accounts, requests[r][1], requests[r][2])

      if checkNegativeBalance(accounts, requests[r][1]) != None:
        return checkNegativeBalance(accounts, requests[r][1])

    elif requests[r][0] == 'transfer':
      # check if account exists
      if checkAccountExists(accounts, requests[r][1], requests[r][2]) is not None:
        return checkAccountExists(accounts, requests[r][1], requests[r][2])
      # transfer funds
      transfer(accounts, requests[r][1], requests[r][2], requests[r][3])
      # see if transfer resulted in negative balance
      if checkNegativeBalance(accounts, requests[r][1]) is not None:
        return checkNegativeBalance(accounts, requests[r][1])

    elif requests[r][0] == 'withdraw':
      if checkAccountExists(accounts, requests[r][1]) is not None:
        return checkAccountExists(accounts, requests[r][1])

      withdraw(accounts, requests[r][1], requests[r][2])

      if checkNegativeBalance(accounts, requests[r][1]) != None:
        return checkNegativeBalance(accounts, requests[r][1])

  return accounts


