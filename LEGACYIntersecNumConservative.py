from array import array

from beautifultable import BeautifulTable

n = int(input("Order: "))

# First subtable
table2 = BeautifulTable()
table2.set_style(BeautifulTable.STYLE_COMPACT)

# Second subtable
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

def fillChart (n, n2, a22_2, a22_3, a24_2):
    if n2 >= a22_3 + a22_2:  # Since a24(3) = n2-a22(3)-a22(2) >= 0
        a24_3 = n2 - a22_3 - a22_2

        if n4 - a24_2 - a24_3 >= 0:
            a22_4 = int(n2 / n4) * (n2 - a22_2 - a22_3)  # assign a22(4)
            a23_4 = int(n2 / n4) * (n2 - 2 * a22_2 - 1)  # assign a23(4)
            a24_4 = n2 - a23_4 - a22_4

            if n4 - 2 * a24_4 - 1 >= 0:
                table.column_headers = [f"Order: {n}"]

                table2[1][1] = a22_2  # a22(2)
                table2[2][1] = a22_3  # a22(3)
                table2[3][1] = a22_4  # a22(4)

                table2[0][3] = n2  # a23(1)
                table2[1][3] = a23_2  # a23(2)
                table2[2][3] = a23_2  # a23(3)
                table2[3][3] = a23_4  # a23(4)

                table2[1][5] = a24_2  # a24(2)
                table2[2][5] = a24_3  # a24(3)
                table2[3][5] = a24_4  # a24(4)

                table3[1][1] = a22_3  # a33(2)
                table3[2][1] = a22_2  # a33(3)
                table3[3][1] = a22_4  # a33(4)

                table3[1][3] = a24_2  # a34(2)
                table3[2][3] = a24_3  # a34(3)
                table3[3][3] = a24_4  # a34(4)

                table3[0][5] = n4  # a44(1)
                table3[1][5] = n4 - a24_2 - a24_3  # a44(2)
                table3[2][5] = n4 - a24_2 - a24_3  # a44(3)
                table3[3][5] = n4 - 2 * a24_4 - 1  # a44(4)

                print(table)








##############################################



for n2 in range(0, int(n / 2) + 1):
    n4 = n - 2 * n2 - 1

    for a22_2 in range(0, n2 - 1 + 1):
        a23_2 = a22_2
        a24_2 = n2 - a23_2 - a22_2 - 1
        a23_3 = a23_2

        if a24_2 >= 0:
            for a22_3 in range(0, n2 - a23_3 + 1):
                if n2 >= a22_3 + a22_2:                 # Since a24(3) = n2-a22(3)-a22(2) >= 0
                    a24_3 = n2 - a22_3 - a22_2

                    if n4 - a24_2 - a24_3 >= 0:
                        a22_4 = int(n2 / n4)*(n2-a22_2-a22_3)       # assign a22(4)
                        a23_4 = int(n2 / n4)*(n2 - 2*a22_2 - 1)     # assign a23(4)
                        a24_4 = n2 - a23_4 - a22_4

                        if n4 - 2 * a24_4 - 1 >= 0:
                            table.column_headers = [f"Order: {n}"]

                            table2[1][1] = a22_2    # a22(2)
                            table2[2][1] = a22_3    # a22(3)
                            table2[3][1] = a22_4    # a22(4)

                            table2[0][3] = n2       # a23(1)
                            table2[1][3] = a23_2    # a23(2)
                            table2[2][3] = a23_2    # a23(3)
                            table2[3][3] = a23_4    # a23(4)

                            table2[1][5] = a24_2    # a24(2)
                            table2[2][5] = a24_3    # a24(3)
                            table2[3][5] = a24_4    # a24(4)

                            table3[1][1] = a22_3    # a33(2)
                            table3[2][1] = a22_2    # a33(3)
                            table3[3][1] = a22_4    # a33(4)

                            table3[1][3] = a24_2    # a34(2)
                            table3[2][3] = a24_3    # a34(3)
                            table3[3][3] = a24_4    # a34(4)

                            table3[0][5] = n4                   # a44(1)
                            table3[1][5] = n4 - a24_2 - a24_3   # a44(2)
                            table3[2][5] = n4 - a24_2 - a24_3   # a44(3)
                            table3[3][5] = n4 - 2 * a24_4 - 1   # a44(4)

                            print(table)