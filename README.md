# blindr
The blinds of the future.

Publish:
mosquitto_pub -p 50001 -t devices/e45f01ae3ae5/blinds/set_percentage -m '{"percentage": 100, "client": "wawa"}'

Subscribe:
mosquitto_sub -t "blinds/tilt_changed" -v
