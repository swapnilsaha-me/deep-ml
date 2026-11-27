import numpy as np

def online_simple_regression(xs, ys):
    # return (N, 2) array of (w0, w1) after each point

    x0 = xs[0]
    y0 = ys[0]
    cnt = 0.0
    sum_xi = 0.0
    sum_xi_square = 0.0
    sum_yi = 0.0
    sum_xi_yi = 0.0

    ans = np.zeros((len(xs), 2))

    for i in range(len(xs)):
        dx = xs[i] - x0
        dy = ys[i] - y0

        cnt = cnt + 1
        sum_xi = sum_xi + dx
        sum_xi_square = sum_xi_square + (dx * dx)
        sum_yi = sum_yi + dy
        sum_xi_yi = sum_xi_yi + (dx * dy)

        sum_xi_avg = sum_xi / cnt
        sum_yi_avg = sum_yi / cnt

        cxx = (sum_xi_square - (2 * sum_xi * sum_xi_avg) + (cnt * sum_xi_avg * sum_xi_avg)) / cnt
        cxy = (sum_xi_yi - (sum_xi * sum_yi_avg) - (sum_xi_avg * sum_yi) + (cnt * sum_xi_avg * sum_yi_avg)) / cnt

        if cxx > 0.0:
            w1 = cxy / cxx
        else:
            w1 = 0.0
        w0 = (y0 + sum_yi_avg) - (w1 * (x0 + sum_xi_avg))
        ans[i][0] = w0
        ans[i][1] = w1

    return ans
