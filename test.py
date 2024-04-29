from simulation.epi_sim import Simulation
from pydantic import BaseModel
import logging

logging.basicConfig(filename="simulation.log",
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

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
    amount_of_agents: int = 20

a = SimulationParameters()
simulation = Simulation(**a.model_dump())
simulation.initialize_simulation()
simulation.simulate()
pass