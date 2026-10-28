

import numpy as np
import 

initial_biomass = 0.1       
maximum_growth_rate = 0.5   
saturation_constant = 0.5   
substrate_initial = 20.0   
yield_coefficient = 0.5     


pH = 7.0
optimum_pH = 7.0


time = np.linspace(0, 24, 200)
dt = time[1] - 
biomass = np.zeros(len(time))
substrate = np.zeros(len(time))

biomass[0] = initial_biomass
substrate[0] = substrate_initial


pH_factor = max(0, 1 - ((pH - optimum_pH)

for i in range(1, len(time)):

    
    growth_rate = (
        maximum_growth_rate
        * substrate[i - 1]
        / (saturation_constant + substrate[i - 1])
        * pH_factor
    

    
    biomass_growth = growth_rate * biomass[i - 1]

    
    substrate_consumption = biomass_growth / 
    biomass[i] = biomass[i - 1] + biomass_growth * dt

    substrate[i] = max(
        0,
        substrate[i - 1] - substrate_consumption 

print("CHEMICAL BIOENGINEERING SIMULATION")
print("----------------------------------")
print(f"Initial Biomass: {biomass[0]:.3f} g/L")
print(f"Final Biomass: {biomass[-1]:.3f} g/L")
print(f"Initial Substrate: {substrate[0]:.3f} g/L")
print(f"Final Substrate: {substrate[-1]:.3f} g/L")
print(f"Operating pH: 

plt.figure(figsize=(10, 6))

plt.plot(
    time,
    biomass,
    label="Biomass Concentration",
    linewidth=2
)

plt.plot(
    time,
    substrate,
    label="Substrate Concentration",
    linewidth=2
)

plt.xlabel("Time (hours)")
plt.ylabel("Concentration (g/L)")
plt.title("Bioreactor Biomass Growth Simulation")
plt.legend()
plt.grid(True)

plt.show()
