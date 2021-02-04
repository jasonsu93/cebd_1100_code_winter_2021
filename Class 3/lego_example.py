MIN_AGE = 8
MAX_AGE = 99

Customer_age_ok = False

age = int(input("What is the age of the customer?"))

if age >= MIN_AGE and age <= MAX_AGE:
    customer_age_ok = True

if customer_age_ok:
    print("This customer is able to use this product")