from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Tuple
from simulation.epi_sim import Simulation
from fastapi import FileResponse
import matplotlib.pyplot as plt
import numpy as np
import io

app = FastAPI()

# Instancia global de la simulación
simulation = None
running = False
done = False

class SimulationParameters(BaseModel):
    simulation_days: int = 31
    grid_size: int = 10
    block_capacity: int = 100
    house_amount: int = 10
    house_capacity: int = 5
    hospital_amount: int = 4
    hospital_capacity: int = 50
    hospital_hours: tuple = (8, 20)
    recreational_amount: int = 4
    recreational_capacity: int = 20
    recreational_hours: tuple = (8, 20)
    works_amount: int = 4
    works_capacity: int = 10
    work_hours: tuple = (8, 20)
    amount_of_agents: int = 10

@app.post("/simulation/initialize")
async def initialize_simulation(params: SimulationParameters):
    global simulation
    global running
    if simulation is not None:
        raise HTTPException(status_code=400, detail="Delete current simulation to initialize another one")
    # simulation = Simulation(**params.dict())# Deprecated
    simulation = Simulation(**params.model_dump())
    simulation.initialize_simulation()
    return {"message": "Simulation initialized"}

@app.get("/simulation/delete")
async def delete_simulation():
    global simulation
    global running
    global done
    if simulation is None:
        raise HTTPException(status_code=400, detail="Theres no created simulation")
    if running:
        raise HTTPException(status_code=400, detail="Wait till the simulation stops running to delete it")
    simulation = None
    done = False
    return {"message": "Simulation deleted"}
    
@app.get("/simulation/reset")
async def reset_simulation():
    global simulation
    global running
    global done
    if simulation is None:
        raise HTTPException(status_code=400, detail="Initialize a simulation first")
    if running:
        raise HTTPException(status_code=400, detail="Wait till the simulation is done running")
    simulation.reset_sim()
    done = False
    return {"message": "Simulation reseted"}
    
@app.get("/simulate")
async def start_simulation():
    global simulation
    global running
    global done
    if simulation is None:
        raise HTTPException(status_code=400, detail="Define a simulation first")
    if running:
        raise HTTPException(status_code=400, detail="The simulation is already running")
    if done:
        raise HTTPException(status_code=400, detail="Reset the simulation before running it")
    running = True
    simulation.simulate()
    running = False
    done = True
    return {"message": "Simulation started"}

@app.get("/simulate/status")
async def get_simulation_status():
    global simulation
    global running
    if simulation is None:
        return {"status": "not initialized"}
    if done:
        return {"status": "done"}
    if not running:
        return {"status": "not running"}
    if running:
        return {"status": "running"}

@app.get("/statistics")
async def stats(stat: Optional[str] = None, range: Optional[Tuple] = None):
    global simulation
    global done
    if simulation is None:
        raise HTTPException(status_code=400, detail="Define a simulation first")
    if not done:
        raise HTTPException(status_code=400, detail="Run the simulation first")
    sim_stats = simulation.get_stats()
    if stat is None:
        return sim_stats
    else:
        return sim_stats[stat][start:end]


@app.get("/plots/test")
async def test_plot():
    # Generate some data for plotting
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # Create a plot
    plt.figure(figsize=(8, 6))
    plt.plot(x, y)
    plt.title("Test Plot")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    
    # Save the plot to a BytesIO object
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    # Return the plot as a FileResponse
    return FileResponse(buf, media_type="image/png")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)