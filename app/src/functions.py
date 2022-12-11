# def say_hello(user_name, user_age):
#     print("Hello", user_name, "how r u?")
#     print("you are", user_age, "years old")

# say_hello('hyuk', 28)
# say_hello('sun', 28)

def tax_calc(salary, tax_rate=0.35):
    return salary * tax_rate

def pay_tax(tax):
    print('thank you for paying', tax)

to_pay = tax_calc(150000000)
pay_tax(to_pay)