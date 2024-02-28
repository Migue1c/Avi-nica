import math

gamma_b = 008.8717

gg = math.floor(gamma_b)
v = (gamma_b - gg) * 60 
mm = math.floor(v)
mm_f = math.modf(v)
print(mm_f)
ss = int( mm_f[0] * 60 )
print(gg,'º',mm,'`',ss,'``')









