# This is a systemd service daemon

## Install
Install this script by executing
```
pip3 install .
```
In order to create the systemd service, you can modify the `example-systemd.service` file and place on the systemd services path.
Run `systemctl daemon-reload` and enable it with `systemd enable example-systemd`.

## Debug
The program will log on the `stdout` .

## Tests
Run the tests executing
```
python3 -m unittest discover
```

## File structure
```
src/ - Program files
test/ - Test files
config/__init__.py - Default configuration settings
myservice - Main executable
```

## Running
Execute this program by `./myservice`.

### Environment
The default environment variables are

| Variable  | Environment var | Type   |
|-----------|-----------------|--------|
| name      | APP_NAME        | String |
| log_level | LOG_LEVEL       | String |
