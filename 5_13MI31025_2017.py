import numpy as np


def fuzzy(price):
    if price < 5.:
        return [1., 0., 0.]
    elif price >= 5. and price < 10.:
        return [2. - price / 5., price / 5. - 1, 0.]
    elif price >= 10. and price < 20.:
        return [0., 1., 0.]
    elif price >= 20. and price < 35.:
        return [0., -price / 15. + 35. / 15., price / 15. - 20. / 15.]
    else:
        return [0., 0., 1.]

price = []
for i in range(1, 4):
    price.append(int(raw_input("Enter car price of person {}: ".format(i))))

#### car price and income relationship ##############
c_i_rel = np.matrix([[0.6, 0.3, 0.3],
                     [0.3, 0.8, 0.3],
                     [0.1, 0.3, 0.7]])

#### income and mortgage relationship ##############

i_m_rel = np.matrix([[0., 0.3, 1.],
                     [0.2, 0.6, 0.5],
                     [0.8, 0.4, 0.4]])

ans = []
for j in range(3):
    price_rel = []
    for i in range(3):
        price_rel = np.vstack(fuzzy(price[j] / 1000))

    price_rel = np.vstack(price_rel)

    income = []
    for i in range(3):
        income.append(np.max(np.minimum(c_i_rel[:, i], price_rel)))

    income = np.vstack(income)

    mortgage = []
    for i in range(3):
        mortgage.append(np.max(np.minimum(i_m_rel[:, i], income)))

    mortgage = np.vstack(mortgage)
    ans.append(mortgage)

pp = []
for i in range(3):
    pp.append(ans[i][0])

ans  = np.argmax(pp)

print "Person {} will pay mortgage in shortest time so he is perfect for the girl.".format(ans+1)