real_income, temp, tax = 0, 0, 0

def cal_tax(income):
    print("소득: {} ".format(income), end="")
    print("(만)원")

    global real_income    #tax 대신
    global temp   #income의 변화
    global tax

    real_income = income

    if income > 15000:
        temp = (income-15000)
        tax += temp*0.38
        income -= temp
 
    if income >8800 and income <= 15000:
        temp = (income-8800)
        tax += temp*0.35
        income -= temp

    if income > 4600 and income <= 8800:
        temp = (income-4600)
        tax += temp*0.24
        income -= temp
 
    if income > 1200 and income <=4600:
        temp = (income-1200)
        tax += temp*0.15
        income -= temp
 
    if income <= 1200:
        tax += (income*0.06)

cal_tax(income = float(input("소득을 입력해주세요 (만)원: ")))
print("세금:", tax, end="")
print("(만)원")
print("순수소득:", real_income-tax, end="")
print("(만)원")