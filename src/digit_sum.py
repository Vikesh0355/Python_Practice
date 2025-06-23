def sum_digit(var):
    sum = 0;
    while var!=0:  
        sum = sum + var%10;
        var = var//10;
    print(sum);
    
sum_digit(123);