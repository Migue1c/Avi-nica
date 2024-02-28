import math

gamma_b = 45.01284
gg = math.floor(gamma_b)
v = (gamma_b - gg) * 60 
mm = math.floor(v)
mm_f = math.modf(v)
ss = int( mm_f * 60 )
print(gg,'º',mm,'`',ss,'``')









