# blindr
The blinds of the future.

Publish:
mosquitto_pub -h localhost -t blinds/set_percentage -m '{"percentage": 100, "client": "wawa"}' -p 1883

Subscribe:
mosquitto_sub -t "blinds/tilt_changed" -v
