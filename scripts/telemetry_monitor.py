import asyncio
from src.drone.config import MAVLINK_ADDRESS
from src.drone.mavlink.connection import connect_drone

async def main():
    drone = await connect_drone(MAVLINK_ADDRESS)

    print("Waiting for connection...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print("Connected to drone")
            break

    async for position in drone.telemetry.position():
        print(position)
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())