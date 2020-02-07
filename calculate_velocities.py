# Calculate Galactocentric velocities for a list of stars
# by Guilherme Limberg

import numpy as np
import astropy.coordinates as coord
import astropy.units as u

# Reading data as a table and doing necessary convertions/operations

data = np.loadtxt("yourdata.txt", skiprows=1)

# A table with these parameters (below) must be provided
# The format MUST be in the sequence: radial velocities (RV), parallaxes, right ascensions (RA), declinations (DEC), RA proper motion and DEC proper motion  
# Feel free to improve upon that, I was too lazy

rv = data[:,0]
parallax = data[:,1]
ra = data[:,2]
dec = data[:,3]
pmra = data[:,4]
pmdec = data[:,5]

# Making velocity calculations from data presented above

#Important: your RA/DEC must be in deg. If they are not, convert them first (I have another program for it on my GitHub, it is pretty simple.)

vel = coord.ICRS(ra=ra*u.degree, dec=dec*u.degree,
                distance=(parallax*u.mas).to(u.pc, u.parallax()),
                pm_ra_cosdec=pmra*u.mas/u.yr,
                pm_dec=pmdec*u.mas/u.yr,
                radial_velocity=rv*u.km/u.s)

# Setting the Galactocentric velocity of the Sun AGAINST the V_LSR (Schonrich et al., 2019)

v_sun = coord.CartesianDifferential([11.1, 12.24, 7.25]*u.km/u.s)

gc_frame = coord.Galactocentric(galcen_v_sun=v_sun)

vel_gal = vel.transform_to(gc_frame)

# Writing vector with the V component of the calculated total velocities (in the U,V,W system)

v_y = []	
v_x = []
v_z = []

for i in range ( len (vel_gal.v_y) ):
	v_y.append ( float(vel_gal.v_y[i] * u.s / u.km) )
	v_x.append ( float(vel_gal.v_x[i] * u.s / u.km) )
	v_z.append ( float(vel_gal.v_z[i] * u.s / u.km) )

### Save velocity componenets to different variables (v_x, v_y and v_z) and keep them in the same array (Vtotal)

Vtotal = np.zeros((len(v_x), 3))

for i in range (len(v_x)):
	Vtotal[i][0] = v_x[i] 

for i in range (len(v_x)):
	Vtotal[i][1] = v_y[i]
 
for i in range (len(v_x)):
	Vtotal[i][2] = v_z[i] 

# Write results to an output document ( .txt in this case )

np.savetxt("full_vel.csv", Vtotal, fmt="%s")























