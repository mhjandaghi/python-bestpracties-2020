def years_save():
    year_user = int(input("enter your years: "))
    return year_user

def bank_pos(cash_user, rate):
    pos_money = cash_user * rate
    
    for _ in range(0,years_save()):
        cash_user += pos_money # cashuser *= (1 - rate) 
    return cash_user

user_rate = float(input("enter your rate: "))
user_current_money = int(input("enter your money: "))
print(int(bank_pos(user_current_money, user_rate)))