import math

#A(38º04'35''N, 037º48'17''E, 7200m) 
h=7200
a=6378137
e= 0.0818

phi_a = 38
phi_b = 4
phi_c = 35
gamma_a = 37
gamma_b = 48
gamma_c = 17

def ang_geo(phi_a, phi_b, phi_c, gamma_a, gamma_b, gamma_c): #passar geodetico para decimal

    lat = phi_a + (phi_b / 60) + (phi_c/3600)
    #lat = round(lat, 6)
    
    long = gamma_a + (gamma_b / 60) + (gamma_c/3600)
    #long = round(long, 6)

    return lat, long

lat, long = ang_geo(phi_a, phi_b, phi_c, gamma_a, gamma_b, gamma_c)

lat = math.radians(lat)
long = math.radians(long)

n = a / math.sqrt( 1 - ((e**2)*(math.sin(lat)**2)) )
print("n=",n)

x = (h + n) * math.cos(lat) * math.cos(long)
y = (h + n) * math.cos(lat) * math.sin(long)
z = (h + n - ((e**2)*n)) * math.sin(lat)
print("X=",x,"Y=",y,"Z=",z)