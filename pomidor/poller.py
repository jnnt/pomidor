import click
import serial
import requests


@click.command()
@click.argument('cfg', envvar='POMIDOR_CFG', type=click.File('r'))
def toggl_poll(cfg):
    pass
