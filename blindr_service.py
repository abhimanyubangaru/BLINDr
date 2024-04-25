import asyncio
from asyncio_mqtt import Client, MqttError
import json
from bleak import BleakClient

# MQTT and device configuration
MQTT_BROKER_HOST = "localhost"
MQTT_TOPIC_SUBSCRIBE = "blinds/set_percentage"
MQTT_TOPIC_PUBLISH = "blinds/tilt_changed"
MAC_ADDRESS = "E8:72:19:71:DD:55"
CHARACTERISTIC_UUID = "CBA20002-224D-11E6-9FB8-0002A5D5C51B"

client = "blind_service"

def percentage_to_hex(percentage):
    if not 0 <= percentage <= 100:
        raise ValueError("Percentage must be between 0 and 100.")
    return f"570f450105ff{format(int(percentage), '02x')}"

async def send_command(client, command_hex, percentage, max_retries=10):
    for attempt in range(max_retries):
        try:
            await client.connect()
            if client.is_connected:
                await client.write_gatt_char(CHARACTERISTIC_UUID, bytes.fromhex(command_hex))
                print(f"Command sent: {command_hex}")
                return True
        except Exception as e:
            print(f"Failed to send command on attempt {attempt+1}: {str(e)}")
        finally:
            await client.disconnect()
        await asyncio.sleep(1)
    return False

async def main():
    async with Client(hostname=MQTT_BROKER_HOST) as mqtt_client:
        await mqtt_client.subscribe(MQTT_TOPIC_SUBSCRIBE)
        async with mqtt_client.unfiltered_messages() as messages:
            async for message in messages:
                try:
                    data = json.loads(message.payload.decode())
                    if 'percentage' in data:
                        percentage = data['percentage']
                        command_hex = percentage_to_hex(percentage)
                        bleak_client = BleakClient(MAC_ADDRESS)
                        if await send_command(bleak_client, command_hex, percentage):
                            # Successfully sent the command, now publish the change
                            await mqtt_client.publish(MQTT_TOPIC_PUBLISH, json.dumps({"percentage": percentage, "client" : client}))
                            print(f"Published new tilt percentage: {percentage}")
                except json.JSONDecodeError:
                    print("Received non-JSON message.")
                except KeyError:
                    print("Received JSON does not contain 'percentage' key.")
                except ValueError as e:
                    print(f"Error processing message: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())
