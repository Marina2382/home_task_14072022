
while True:
    customer_code =str(input('Customer code: ')).upper()
    
    if customer_code == 'Q':
        break
    else:
        
        n_days =int(input('Number of days: '))
        start =int(input('Odometer reading at the start: '))
        end =int(input('Odometer reading at the end: '))
    
    
        
        
        def my_miles_calc (start, end): 
            if end >= start:
                miles = (end- start)/10
            else:
                miles = (end+1000000- start)/10
            return   miles  
        
        if customer_code=='D':
            miles = my_miles_calc(start, end)
            if miles/n_days <= 100:
                amount = 60 * n_days
            else:
                amount = 60 * n_days + miles/n_days*0.25
            print(f'Classification code: {customer_code}')
            print(f'Rental period (days): {n_days}')
            print(f'Odometer reading at the start: {start}')
            print(f'Odometer reading at the end: {end}')
            print(f'Number of miles driven: {miles}')
            print(f'Amount due $: {amount}')
    

    
        elif customer_code=='B':
                miles = my_miles_calc(start, end)
                amount = 40 * n_days + miles*0.25
                print(f'Classification code: {customer_code}')
                print(f'Rental period (days): {n_days}')
                print(f'Odometer reading at the start: {start}')
                print(f'Odometer reading at the end: {end}')
                print(f'Number of miles driven: {miles}')
                print(f'Amount due $: {amount}')
    
        elif customer_code=='W':
            if n_days <= 7:
                n_weeks = 1
            else:
                n_weeks = (n_days // 7) + 1
            miles = my_miles_calc(start, end)
            avg_miles = miles / n_weeks
            if avg_miles <= 900:
                amount = 190 * n_weeks 
            elif avg_miles > 900 and avg_miles < 1500:
                amount = 190 * n_weeks + 100 * n_weeks
            else:
                amount = 190 * n_weeks + 200 * n_weeks + (avg_miles-1500) * 0.25 * n_weeks
            print(f'Classification code: {customer_code}')
            print(f'Rental period (days): {n_days}')
            print(f'Odometer reading at the start: {start}')
            print(f'Odometer reading at the end: {end}')
            print(f'Number of miles driven: {miles}')
            print(f'Amount due $: {amount}')    
