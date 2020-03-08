from beautifultable import BeautifulTable

Order = 10

# First subtable
table2 = BeautifulTable()
table2.set_style(BeautifulTable.STYLE_COMPACT)

#Second subtable
table3 = BeautifulTable()
table3.set_style(BeautifulTable.STYLE_COMPACT)

table2.append_row(['a22(1)', 0, 'a23(1)', 0, 'a24(1)', 0])
table2.append_row(['a22(2)', 0, 'a23(2)', 0, 'a24(2)', 0])
table2.append_row(['a22(3)', 0, 'a23(3)', 0, 'a24(3)', 0])
table2.append_row(['a22(4)', 0, 'a23(4)', 0, 'a24(4)', 0])

table3.append_row(['a33(1)', 0, 'a34(1)', 0, 'a44(1)', 0])
table3.append_row(['a33(2)', 0, 'a34(2)', 0, 'a44(2)', 0])
table3.append_row(['a33(3)', 0, 'a34(3)', 0, 'a44(3)', 0])
table3.append_row(['a33(4)', 0, 'a34(4)', 0, 'a44(4)', 0])

table = BeautifulTable()

table.append_row([table2])
table.append_row([table3])

#############################################################


# Restriction of a22(2)+a23(2)+a24(2)=n2
for n2 in range(0, int(Order/2)+1):
    n4 = Order-2*n2-1
    for a22_2 in range(0,n2-1+1):
        for a23_2 in range(0,n2-a22_2+1-1):
            a24_2 = n2-a23_2-a22_2-1
            a23_3=a23_2
            
            if a24_2>=0 and a23_2>=0:
                for a22_3 in range(0,n2-a23_3+1):
                    a24_3=n2-a22_3-a23_3
                    
                    if a24_3 >= 0 and n4-a24_2-a24_3 >= 0:
                        for a22_4 in range(0,n2+1):
                            for a23_4 in range(0,n2-a22_4+1):
                                a24_4=n2-a23_4-a22_4
                                if n4-2*a24_4-1 >= 0:
                                    table.column_headers = [f"Order: {Order}"]
                                    
                                    table2[1][1]=a22_2
                                    table2[2][1]=a22_3
                                    table2[3][1]=a22_4
                                    
                                    table2[0][3]=n2
                                    table2[1][3]=a23_2
                                    table2[2][3]=a23_2
                                    table2[3][3]=a23_4
                                    
                                    table2[1][5]=a24_2
                                    table2[2][5]=a24_3
                                    table2[3][5]=a24_4
                                    
                                    table3[1][1]=a22_3
                                    table3[2][1]=a22_2
                                    table3[3][1]=a22_4
                                    
                                    table3[1][3]=a24_2
                                    table3[2][3]=a24_3
                                    table3[3][3]=a24_4
                                    
                                    table3[0][5]=n4
                                    table3[1][5]=n4-a24_2-a24_3
                                    table3[2][5]=n4-a24_2-a24_3
                                    table3[3][5]=n4-2*a24_4-1
                                    
                                    print(table)
                        
            
            
# Restriction of a22(4)+a23(4)+a24(4)=n2
#for n2 in range(0, int(Order/2)+1):
#    for a22_4 in range(0,n2+1):
#        for a23_4 in range(0,n2-a22_4+1):
#            a24_4 = n2-a22_4-a23_4


#for a22_2 in range(0,10+1):
#    for a23_2 in range(0,10-a22_2+1):
#        a24_2 = 10-a22_2-a23_2
#        print(a22_2, a23_2, a24_2)





#print(table)