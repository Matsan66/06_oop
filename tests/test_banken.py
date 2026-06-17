from myapp.banken import Bank
import pytest

"""
Funktionella krav:
User-Stories

Som användare vill jag kunna skapa ett konto så att jag kan hantera mina tillgångar
Som användare vill jag kunna sätta in pengar så att jag kan öka mina tillgångar
Som användare vill jag kunna ta ut pengar så att jag kan använda mina tillgångar
Som användare vill jag kunna se mitt saldo så att jag vet vilka tillgångar jag har
Som användare vill jag kunna räkna ut ränta så att jag ser hur mycket extra pengar jag får
Som användare vill jag kunna ange en summa att betala så att jag ser om jag har råd

Icke Funktionella krav:
- Om man inte anger ett saldo då kontot skapas ska det sättas till 0 krav
- Om ett negativt värde anges då kontot skapas ska ett fel genereras
- Om en positiv summa anges då kontot skapas ska denna utgöra kontots saldo
- Om man väljer att sätta in en godkänds summa ska kontots saldo öka med denna
- Om ett negativt värde anges vid insättning skall ett fel genereras
- Om en godkänd summa anges vid uttag skall kontots saldo minskas med denna
- Om summan vid uttag överstiger saldot på kontot ska ett fel genereras
- Om ett negativt värde anges vid uttag skall ett fel genereras
- Om användaren väljer att visa kontots saldo skall detta returnera
- Om man anger en räntesats 1 - 100 skall kontots saldo ökas med denna 
- Om man anger en felaktig räntesats skall ett fel genereras
- Om man anger en summa att betala skall programmet returnera om det finns täckning (True eller False)
- Om man anger en negativ summa att betala skall ett fel genereras
"""

# BANK ACCOUNT CREATION
#-----------------------

@pytest.mark.parametrize(
    "start_balance, expected_balance",
    [
        (0, 0.0),       # Test 0 kr as start balance
        (100, 100)      # Test 100 kr as start balance
    ]
)

def test_create_balance_account(start_balance, expected_balance):
    """
    Test create an account with starting balance. Also tests check_balance()
    """

    bank_account = Bank(start_balance)
    assert bank_account.check_balance() == expected_balance

# -------------------------------------------------------------

def test_create_zero_balance_account():
    """
    Test create an account with no starting balance gives 0 kr in balance
    """

    bank_account = Bank()
    assert bank_account.check_balance() == 0

# -------------------------------------------------------------

def test_create_negative_balance_account():
    """
    Test create an account with negative starting balance triggers ValueError
    """

    with pytest.raises(ValueError):
        bank_account = Bank(-100)

# -------------------------------------------------------------


# BANK ACCOUNT DEPOSITION
#-------------------------

@pytest.mark.parametrize(
    "deposit_amount, expected_balance",
    [
        (1, 1),       # Test deposit 0 kr
        (500, 500)      # Test deposit 500 kr
    ]
)

def test_deposit_account(deposit_amount, expected_balance):
    """
    Test deposit a sum greater than 0 kr to account
    """

    bank_account = Bank()
    bank_account.deposit_money(deposit_amount)
    assert bank_account.check_balance() == expected_balance

# -------------------------------------------------------------

@pytest.mark.parametrize(
    "deposit_amount",
    [
    0,          # Test deposit 0 kr
    -1          # Test deposit -1 kr
    ]
)

def test_deposit_negative_amount_account(deposit_amount):
    """
    Test deposit a sum lower than 1 kr to account triggers ValueError
    """

    bank_account = Bank()
    with pytest.raises(ValueError):
        bank_account.deposit_money(deposit_amount)

# -------------------------------------------------------------


# BANK ACCOUNT WITHDRAW
#-----------------------

@pytest.mark.parametrize(
    "withdraw_amount, expected_balance",
    [
        (0, 1000.0),        # Test withdraw 0 kr
        (500, 500)          # Test withdraw 500 kr
    ]
)

def test_withdraw_account(withdraw_amount, expected_balance):
    """
    test withdraw a sum from account
    """

    bank_account = Bank(1000)
    bank_account.withdraw_money(withdraw_amount)
    assert bank_account.check_balance() == expected_balance

# -------------------------------------------------------------

def test_withdraw_negative_amount_account():
    """
    Test withdraw a negative sum from account triggers ValueError
    """

    bank_account = Bank(1000)
    with pytest.raises(ValueError):
        bank_account.withdraw_money(-100)

# -------------------------------------------------------------

def test_withdraw_no_coverage_amount_account():
    """
    Test withdraw a sum greater than balance triggers ValueError
    """

    bank_account = Bank(1000)
    with pytest.raises(ValueError):
        bank_account.withdraw_money(2000)

# -------------------------------------------------------------


# BANK ACCOUNT APPLY INTEREST
#-----------------------------

@pytest.mark.parametrize(
    "interest, expected_balance",
    [
        (0, 1000.0),       # Test add 0 % interest
        (10, 1100),        # Test add 10 % interest
        (100, 2000)        # Test add 100 % interest
    ]
)

def test_add_interest_account(interest, expected_balance):
    """
        Test add a percentual interest sum to account
    """
    bank_account = Bank(1000)
    bank_account.apply_interest(interest)
    assert bank_account.check_balance() == expected_balance

# -------------------------------------------------------------

@pytest.mark.parametrize(
    "interest",
    [
        -1,           # Test add -1 % interest
        101           # Test add 101 % interest
    ]
)

def test_add_invalid_interest_account(interest):
    """
        Test add an invalid percentage trigger ValueError
    """
    bank_account = Bank(1000)
    with pytest.raises(ValueError):
        bank_account.apply_interest(interest)

# -------------------------------------------------------------


# BANK ACCOUNT SUFFICIENT BALANCE
#----------------------------------

@pytest.mark.parametrize(
    "bill_amount, balance, expected_result",
    [
        (1000, 1000, True),      # Test bill amount 1000 kr with balance 1000 (sufficient)
        (1100, 1000,False)       # Test bill amount 1100 kr with balance 1000 (insufficient)
    ]
)

def test_sufficient_funds_account(bill_amount, balance, expected_result):
    """
        Test if balance is sufficient for bill
    """
    bank_account = Bank(balance)
    assert bank_account.check_sufficient_funds(bill_amount) == expected_result