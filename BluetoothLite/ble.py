import asyncio
from bleak import BleakClient

address = "C4:E4:8F:C7:DA:59"

MODEL_NBR_UUID = "db450001-8e9a-4818-add7-6ed94a328aB4"
async def run(address, loop):
    async with BleakClient(address, loop=loop) as client:
        model_number = await client.read_gatt_char(MODEL_NBR_UUID)
        print("Model Number: {0}".format("".join(map(chr, model_number))))

loop = asyncio.get_event_loop()
loop.run_until_complete(run(address, loop))
