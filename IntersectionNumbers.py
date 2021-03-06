from array import array
import math

from beautifultable import BeautifulTable



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

def eigenvalue_checks (n, k, a, c):
    d = (a - c) ** 2 + 4 * (k - c)

    # Must have real eigenvalues
    if d < 0:
        return False

    theta = (a - c + math.sqrt(d)) / 2
    tau = (a - c - math.sqrt(d)) / 2

    m_theta = -1 * ((n - 1) * tau + k) / (theta - tau)
    m_tau = ((n - 1) * theta + k) / (theta - tau)

    # Multiplicities must be integral
    if not m_theta.is_integer() or not m_tau.is_integer():
        return False

    # See wikipedia page on SRGs, Godsil Lemma 10.3.2 and pg 222
    if 2 * k + (n - 1) * (a - c) != 0:
        if not theta.is_integer() or not tau.is_integer() or m_theta == m_tau:
            return False
    elif m_theta != m_tau or k != (n - 1) / 2 or a != (n - 5) / 4 or c != (n - 1) / 4:
        return False

    # Godsil Lemma 10.3.1
    if m_theta * m_tau != (n * k * (n - k - 1)) / (theta - tau) ** 2:
        return False

    # Super Krein Bounds
    if (m_theta ** 2 / n) * (1 + theta ** 3 / k ** 2 - (theta + 1) ** 3 / (n - k - 1) ** 2) < 0 or \
            (m_tau ** 2 / n) * (1 + tau ** 3 / k ** 2 - (tau + 1) ** 3 / (n - k - 1) ** 2) < 0:
        return False
    elif (m_theta ** 2 / n) * (1 + theta ** 3 / k ** 2 - (theta + 1) ** 3 / (n - k - 1) ** 2) == 0:
        if n > .5 * m_theta * (m_theta + 3):
            print("New test fail 1\n=====\n====\n====\n====\n====\n====\n====\n")
            return False
    elif (m_theta ** 2 / n) * (1 + theta ** 3 / k ** 2 - (theta + 1) ** 3 / (n - k - 1) ** 2) > 0:
        if n > .5 * m_theta * (m_theta + 1):
            print("New test fail 2\n")
            return False


    # Regular Krein Bounds (possibly redundant)
    if theta * (tau ** 2) - 2 * (theta ** 2) * tau - theta ** 2 - k * theta + k * (tau ** 2) + 2 * k * tau < 0 or \
            (theta ** 2) * tau - 2 * theta * (tau ** 2) - tau ** 2 - k * tau + k * (theta ** 2) + 2 * k * theta < 0:
        return False
    elif theta * (tau ** 2) - 2 * (theta ** 2) * tau - theta ** 2 - k * theta + k * (tau ** 2) + 2 * k * tau == 0:
        if k < m_theta:
            return False
    elif (theta ** 2) * tau - 2 * theta * (tau ** 2) - tau ** 2 - k * tau + k * (theta ** 2) + 2 * k * theta == 0:
        if k < m_tau:
            return False

    return True

def fillChart (n, n2, a22_2, a22_3, a24_2):

    # Since a24(3) = n2-a22(3)-a22(2) >= 0
    if (n2 >= a22_3 + a22_2):
        a24_3 = n2 - a22_3 - a22_2

        a22_4 = (n2 / n4) * (n2 - a22_2 - a22_3)  # assign a22(4)
        a23_4 = (n2 / n4) * (n2 - 2 * a22_2 - 1)  # assign a23(4)
        a24_4 = n2 - a23_4 - a22_4
        a44_2 = n - 4 * n2 + 3 * a22_2 + a22_3
        a44_4 = n4 - 2 * a24_4 - 1

        if a24_3 > 0 and a22_4 > 0 and a23_4 > 0 and a24_4 > 0 and a44_2 > 0 and a44_4 > 0 and a22_4.is_integer() and a23_4.is_integer()\
                and a22_3 * a22_3 + a22_4 * a24_3 == n2 + a22_2 * a22_2 + a23_4 * a24_2 and eigenvalue_checks(n, n4, a44_4, a44_2):
            table.column_headers = [f"n: {n}, n2: {n2}, a22(2): {a22_2}, a22_3: {a22_3}"]

            table2[1][1] = a22_2  # a22(2)
            table2[2][1] = a22_3  # a22(3)
            table2[3][1] = a22_4  # a22(4)

            table2[0][3] = n2     # a23(1)
            table2[1][3] = a22_2  # a23(2)
            table2[2][3] = a22_2  # a23(3)
            table2[3][3] = a23_4  # a23(4)

            table2[1][5] = a24_2  # a24(2)
            table2[2][5] = a24_3  # a24(3)
            table2[3][5] = a24_4  # a24(4)

            table3[1][1] = a22_3  # a33(2)
            table3[2][1] = a22_2  # a33(3)
            table3[3][1] = a22_4  # a33(4)

            table3[1][3] = a24_3  # a34(2)
            table3[2][3] = a24_2  # a34(3)
            table3[3][3] = a24_4  # a34(4)

            table3[0][5] = n4  # a44(1)
            table3[1][5] = a44_2  # a44(2)
            table3[2][5] = a44_2  # a44(3)
            table3[3][5] = a44_4  # a44(4)

            print(table)



########################

# n = int(input("Order: "))

for n in range(1,501):
    for n2 in range(1, int((n - 1) / 2) + 1):             # n=n4+2n2+1 -> 2n2<=n-1
        n4 = n - 2 * n2 - 1

        if n4 > 0:
            for a22_2 in range(1, n2 - 1 + 1):
                a24_2 = n2 - (2 * a22_2) - 1
                if a24_2 > 0:
                    for a22_3 in range(1, n2 - a22_2 + 1):
                        fillChart(n, n2, a22_2, a22_3, a24_2)
