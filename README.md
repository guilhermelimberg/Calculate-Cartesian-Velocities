# Calculate-Cartesian-Velocities

by Guilherme Limberg

This Python3 code allows you to calculate Cartesian velocities in a Galactocentric frame. 

For this, you need Astropy and Numpy packages installed. 

Necessary inputs: Radial velocity (km/s), parallax (mas), RA + DEC (in deg) and pmRA + pmDEC (in mas/yr) in this order. I was too lazy to improve upon this. Feel free to do so. 

Important: the Galactocentric velocity of the Sun against the Local Standard of Rest (v_LSR) is set to the values of Schonrich et al., 2019. 

If you need to convert RA/DEC from hh:mm:ss to degree, I also have a script for that. Check out github.com/guilhermelimberg/Convert-RA-DEC. 

