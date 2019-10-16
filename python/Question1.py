# modify this function, and create other functions below as you wish
def question01(initialLevelOfDebt, interestPercentage, repaymentPercentage):
    # modify and then return the variable below
    debt=initialLevelOfDebt
    fixedRepay=debt*repaymentPercentage/100
    if fixedRepay<50:
        fixedRepay=50
    amt=0.1*debt
    count=0
    while debt>fixedRepay:
        debt+=debt*interestPercentage/100
        debt-=fixedRepay
        amt+=fixedRepay
        count+=1
    if debt!=0:
        amt+=debt
    #print(count)        
    answer = amt
    return answer
        
