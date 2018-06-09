import signal
import sys
import time
import yaml

import click
import serial

from . import toggl

SERIAL_CONNECT_RETRIES = 4


@click.command()
@click.argument('cfg', envvar='POMIDOR_CFG', type=click.File('r'))
def toggl_poll(cfg):

    config = yaml.load(cfg)
    print(config)

    for i in range(SERIAL_CONNECT_RETRIES):
        try:
            ser = serial.Serial(config['device'], config['baud'], timeout=0.1)
        except serial.serialutil.SerialException:
            print(f'Serial connection error, attempt: {i}')
            time.sleep(1)

    def stop(signum, frame):
        print(f'received signal {signum}...')
        ser.close()
        sys.exit(0)

    signal.signal(signal.SIGINT, stop)
    signal.signal(signal.SIGTERM, stop)

    while True:

        try:
            entry = toggl.get_current_time_entry(config['toggl_api_token'])

            if entry:
                comm = b'up'
            else:
                comm = b'down'

            ser.write(comm + b'\n')
            ser.flush()
            print(ser.readlines())
        except Exception as e:
            print(f'Got Exception {e}')
            break
        else:
            time.sleep(7)

    ser.close()
    print('end.')
    return 0
