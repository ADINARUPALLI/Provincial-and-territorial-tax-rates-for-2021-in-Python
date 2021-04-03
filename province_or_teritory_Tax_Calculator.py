def province_or_teritory_name():

    Province_territory=''

    while Province_territory not in ['Newfoundland and Labrador','Prince Edward Island','Nova Scotia','New Brunswick','Quebec','Ontario','Manitoba','Saskatchewan','Alberta','British Columbia','Yukon','Northwest Territories','Nunavut']:
        Province_territory = input("Please pick a province or teritory  from: 'Newfoundland and Labrador','Prince Edward Island','Nova Scotia','New Brunswick','Quebec','Ontario','Manitoba','Saskatchewan','Alberta','British Columbia','Yukon','Northwest Territories' or 'Nunavut'")
    return(Province_territory)
	
def tax_check():
    Annual_income = ''
    
    while type(Annual_income) != float:
        Annual_income = float(input("Please enter your annual income in numbers:"))
    return(Annual_income)

def province_tax():
    Annual_income = tax_check()
    b1= province_or_teritory_name()
    if b1 == 'Newfoundland and Labrador' and type(Annual_income) == float :
        if Annual_income <= 38081:
            return((8.7/100)*Annual_income)
        elif Annual_income >= 38081 and Annual_income <= 76161:
            T1 = Annual_income - 38081
            return((8.7/100)*38081 + (14.5/100)(T1))                  
        elif Annual_income >= 76161   and Annual_income <=  135973:
            T2= Annual_income - 76161
            return((8.7/100)*38081+(14.5/100)*76161+(15.8)*(T2))                   
        elif Annual_income >= 135973  and Annual_income <=  190363:
            T3= Annual_income - 135973
            return((8.7/100)*38081+(14.5/100)*76161+(15.8/100)*135973+(17.3/100)*T3)                   
        elif Annual_income >= 190363:
            T4= Annual_income - 190363 
            return((8.7/100)*38081+(14.5/100)*76161+(15.8/100)*135973+(17.3/100)*190363+(18.3/100)*T4)
        
    elif b1 == 'Prince Edward Island' and type(Annual_income) == float :
        if Annual_income <= 31984:
            return((9.8/100)*Annual_income)
        elif Annual_income >= 31984 and Annual_income <= 63939:
            T1 = Annual_income - 31984
            return((9.8/100)*31984 + (14.5/100)*(T1))                                     
        elif Annual_income >= 63969:
            T2 = Annual_income - 63969 
            return((9.8/100)*31984+(14.5/100)*63939+(16.7/100)*T2)
    
    elif b1 == 'Nova Scotia' and type(Annual_income) == float :
        if Annual_income <= 29590:
            return((8.79/100)*Annual_income)
        elif Annual_income >= 29590 and Annual_income <= 59180:
            T1 = Annual_income - 29590
            return((8.79/100)*29590 + (14.95/100)(T1))                  
        elif Annual_income >= 59180   and Annual_income <=  93000:
            T2= Annual_income - 59180
            return((8.79/100)*29590+(14.95/100)*59180+(16.5)*(T2))                   
        elif Annual_income >= 93000  and Annual_income <=  150000:
            T3= Annual_income - 93000
            return((8.79/100)*29590+(14.95/100)*59180+(16.5/100)*93000+(17.5/100)*T3)                   
        elif Annual_income >= 150000:
            T4= Annual_income - 150000 
            return((8.79/100)*29590+(14.95/100)*59180+(16.5/100)*93000+(17.5/100)*150000+(21.0/100)*T4)
        
    elif b1 == 'New Brunswick' and type(Annual_income) == float :
        if Annual_income <= 43835:
            return((8.79/100)*Annual_income)
        elif Annual_income >= 43835 and Annual_income <= 87671:
            T1 = Annual_income - 43835
            return((8.79/100)*43835 + (14.95/100)(T1))                  
        elif Annual_income >= 87671   and Annual_income <=  142534:
            T2= Annual_income - 87671
            return((8.79/100)*43835+(14.95/100)*87671+(16.5)*(T2))                   
        elif Annual_income >= 142534  and Annual_income <=  162383:
            T3= Annual_income - 142534
            return((8.79/100)*43835+(14.95/100)*87671+(16.5/100)*142534+(17.5/100)*T3)                   
        elif Annual_income >= 162383:
            T4= Annual_income - 162383 
            return((8.79/100)*43835+(14.95/100)*87671+(16.5/100)*142534+(17.5/100)*162383+(21.0/100)*T4)
        
    elif b1 == 'Quebec' and type(Annual_income) == float :
        if Annual_income <= 44545:
            return((15/100)*Annual_income)
        elif Annual_income >= 44545 and Annual_income <= 89080:
            T1 = Annual_income - 44545
            return((15/100)*44545 + (20/100)(T1))                  
        elif Annual_income >= 89080   and Annual_income <=  108390:
            T2= Annual_income - 89080
            return((15/100)*43835+(20/100)*89080+(24)*(T2))                   
        elif Annual_income >= 108390  :
            T3= Annual_income - 108390
            return((15/100)*43835+(20/100)*89080+(24/100)*142534+(25.75/100)*T3)
    
    elif b1 == 'Ontario' and type(Annual_income) == float :
        if Annual_income <= 45142:
            return((5.05/100)*Annual_income)
        elif Annual_income >= 45142 and Annual_income <= 90287:
            T1 = Annual_income - 45142
            return((5.05/100)*45142 + (9.15/100)(T1))                  
        elif Annual_income >= 90287   and Annual_income <=  150000:
            T2= Annual_income - 90287
            return((5.05/100)*45142+(9.15/100)*90287+(11.16)*(T2))                   
        elif Annual_income >= 142534  and Annual_income <=  220000:
            T3= Annual_income - 142534
            return((5.05/100)*45142+(9.15/100)*90287+(11.16/100)*142534+(12.16/100)*T3)                   
        elif Annual_income >= 220000:
            T4= Annual_income - 220000 
            return((5.05/100)*45142+(9.15/100)*90287+(11.16/100)*142534+(12.16/100)*220000+(13.16/100)*T4)
    
    elif b1 == 'Manitoba' and type(Annual_income) == float :
        if Annual_income <= 33723:
            return((10.8/100)*Annual_income)
        elif Annual_income >= 33723 and Annual_income <= 72885:
            T1 = Annual_income - 33723
            return((10.8/100)*33723 + (12.75/100)*(T1))                                     
        elif Annual_income >= 72885:
            T2 = Annual_income - 72885 
            return((10.8/100)*33723+(12.75/100)*72885+(17.4/100)*T2)
    
    elif b1 == 'Saskatchewan' and type(Annual_income) == float :
        if Annual_income <= 45667:
            return((10.8/100)*Annual_income)
        elif Annual_income >= 45667 and Annual_income <= 130506:
            T1 = Annual_income - 45667
            return((10.8/100)*45667 + (12.5/100)*(T1))                                     
        elif Annual_income >= 130506:
            T2 = Annual_income - 130506
            return((10.8/100)*45667+(12.5/100)*130506+(14.5/100)*T2)
        
    elif b1 == 'Alberta' and type(Annual_income) == float :
        if Annual_income <= 131220:
            return((10/100)*Annual_income)
        elif Annual_income >= 131220 and Annual_income <= 157464:
            T1 = Annual_income - 131220
            return((10/100)*131220 + (12/100)(T1))                  
        elif Annual_income >= 157464   and Annual_income <=  209952:
            T2= Annual_income - 157464
            return((10/100)*131220+(12/100)*157464+(13)*(T2))                   
        elif Annual_income >= 209952  and Annual_income <=  314928:
            T3= Annual_income - 209952
            return((10/100)*131220+(12/100)*157464+(13/100)*209952+(14/100)*T3)                   
        elif Annual_income >= 314928:
            T4= Annual_income - 314928 
            return((10/100)*45142+(12/100)*90287+(13/100)*142534+(14/100)*314928+(15/100)*T4)
        
    elif b1 == 'British Columbia' and type(Annual_income) == float :
        if Annual_income <= 42184:
            return((5.06/100)*Annual_income)
        elif Annual_income >= 42184 and Annual_income <= 84369:
            T1 = Annual_income - 42184
            return((5.06/100)*42184 + (7.7/100)(T1))                  
        elif Annual_income >= 84369   and Annual_income <=  96886:
            T2= Annual_income - 84369
            return((5.06/100)*42184+(7.7/100)*84369+(10.5)*(T2))                   
        elif Annual_income >= 96886  and Annual_income <=  117623:
            T3= Annual_income - 96886
            return((5.06/100)*42184+(7.7/100)*84369+(10.5/100)*96886+(12.29/100)*T3)                   
        elif Annual_income >= 117623 and Annual_income <=  159483:
            T4= Annual_income - 117623 
            return((5.06/100)*42184+(7.7/100)*84369+(10.5/100)*96886+(12.29/100)*117623+(14.7/100)*T4)                              
        elif Annual_income >= 159483 and Annual_income <=  222420:
            T5= Annual_income - 159483 
            return((5.06/100)*42184+(7.7/100)*84369+(10.5/100)*96886+(12.29/100)*117623+(14.7/100)*159483+(16.8/100)*T5)                       
        elif Annual_income >= 222420:
            T6= Annual_income - 222420 
            return((5.06/100)*42184+(7.7/100)*84369+(10.5/100)*96886+(12.29/100)*117623+(14.7/100)*159483+(16.8/100)*222420+(20.5)*(T6))
    
    elif b1 == 'Yukon' and type(Annual_income) == float :
        if Annual_income <= 49020:
            return((6.4/100)*Annual_income)
        elif Annual_income >= 49020 and Annual_income <= 98040:
            T1 = Annual_income - 49020
            return((6.4/100)*49020 + (9/100)(T1))                  
        elif Annual_income >= 98040   and Annual_income <=  151978:
            T2= Annual_income - 98040
            return((6.4/100)*49020+(9/100)*98040+(10.9)*(T2))                   
        elif Annual_income >= 151978  and Annual_income <=  500000:
            T3= Annual_income - 151978
            return((6.4/100)*49020+(9/100)*98040+(10.9/100)*151978+(12.8/100)*T3)                   
        elif Annual_income >= 500000:
            T4= Annual_income - 500000 
            return((6.4/100)*49020+(9/100)*98040+(10.9/100)*151978+(12.8/100)*500000+(15/100)*T4)  
        
    elif b1 == 'Northwest Territories' and type(Annual_income) == float :
        if Annual_income <= 44396:
            return((5.9/100)*Annual_income)
        elif Annual_income >= 44396 and Annual_income <= 88976:
            T1 = Annual_income - 44396
            return((5.9/100)*44396 + (8.6/100)(T1))                  
        elif Annual_income >= 88976   and Annual_income <=  144362:
            T2= Annual_income - 88976
            return((5.9/100)*44396+(8.6/100)*98040+(12.2)*(T2))                   
        elif Annual_income >= 144362 : 
            T3= Annual_income - 144362
            return((5.9/100)*44396+(8.6/100)*98040+(12.2/100)*144362+(14.5/100)*T3)  
        
    elif b1 == 'Nunavut' and type(Annual_income) == float :
        if Annual_income <= 46740:
            return((4/100)*Annual_income)
        elif Annual_income >= 46740 and Annual_income <= 93480:
            T1 = Annual_income - 46740
            return((4/100)*46740 + (7/100)(T1))                  
        elif Annual_income >= 93480   and Annual_income <=  144362:
            T2= Annual_income - 93480
            return((4/100)*46740+(7/100)*93480+(9)*(T2))                   
        elif Annual_income >= 144362 : 
            T3= Annual_income - 144362
            return((4/100)*46740+(7/100)*93480+(9/100)*144362+(11.5/100)*T3)