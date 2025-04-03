def euler_method(f, t0, y0, t_final, num_steps):
  h = (t_final - t0) / num_steps

  t = t0
  y = y0

  for _ in range(num_steps):
      slope = f(t, y)
      y = y + h * slope
      t = t + h

  return y

def runge_kutta(f, t0, y0, t_final, num_steps):
  h = (t_final - t0) / num_steps

  t = t0
  y = y0

  for _ in range(num_steps):
      k1 = f(t, y)
      k2 = f(t + h / 2, y + h * k1 / 2)
      k3 = f(t + h / 2, y + h * k2 / 2)
      k4 = f(t + h, y + h * k3)

      y = y + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
      t = t + h

  return y

def f(t, y):
  return t - y**2

def gaussian_elimination(A):
  n = len(A)

  for i in range(n):
      max_row = max(range(i, n), key=lambda r: abs(A[r][i]))
      A[i], A[max_row] = A[max_row], A[i]

      pivot = A[i][i]
      for j in range(i, n + 1):
          A[i][j] /= pivot

      for k in range(i + 1, n):
          factor = A[k][i]
          for j in range(i, n + 1):
              A[k][j] -= factor * A[i][j]

  x = [0] * n
  for i in range(n - 1, -1, -1):
      x[i] = A[i][n]
      for j in range(i + 1, n):
          x[i] -= A[i][j] * x[j]

  return x

def determinant(B):
  n = len(B)
  A = [row[:] for row in B]
  det = 1

  for i in range(n):
      max_row = max(range(i, n), key=lambda r: abs(A[r][i]))
      if i != max_row:
          A[i], A[max_row] = A[max_row], A[i]
          det *= -1

      pivot = A[i][i]
      if pivot == 0:
          return 0

      det *= pivot

      for j in range(i + 1, n):
          factor = A[j][i] / pivot
          for k in range(i, n):
              A[j][k] -= factor * A[i][k]

  return det

def lu_factorization(B):
  n = len(B)
  L = [[0] * n for _ in range(n)]
  U = [[0] * n for _ in range(n)]

  for i in range(n):
      L[i][i] = 1

      for j in range(i, n):
          U[i][j] = B[i][j] - sum(L[i][k] * U[k][j] for k in range(i))

      for j in range(i + 1, n):
          if U[i][i] == 0:
              raise ValueError("Zero pivot encountered, LU factorization fails without pivoting.")
          L[j][i] = (B[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]

  return L, U

def is_diagonally_dominant(C):
  n = len(C)

  for i in range(n):
      diagonal_element = abs(C[i][i])

      row_sum = sum(abs(C[i][j]) for j in range(n) if j != i)

      if diagonal_element < row_sum:
          return False, i  

  return True, None

def determinant_2x2(D):
  return D[0][0] * D[1][1] - D[0][1] * D[1][0]

def determinant_3x3(D):
  return (D[0][0] * (D[1][1] * D[2][2] - D[1][2] * D[2][1]) -
          D[0][1] * (D[1][0] * D[2][2] - D[1][2] * D[2][0]) +
          D[0][2] * (D[1][0] * D[2][1] - D[1][1] * D[2][0]))

def is_positive_definite(D):
  det1 = D[0][0]  
  det2 = determinant_2x2([[D[0][0], D[0][1]],
                           [D[1][0], D[1][1]]])  
  det3 = determinant_3x3(D)

  return det1 > 0 and det2 > 0 and det3 > 0