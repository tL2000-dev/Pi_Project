from mavsdk import System

async def connect_drone(address: str) -> System:
    drone = System()
    await drone.connect(system_address=address)
    return drone