import logging
import subprocess
import time

import click

import eusbip.utils


logger = logging.getLogger(__name__)


@click.group()
def main():
    pass


@main.command(
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
    add_help_option=False,
)
@click.pass_context
def daemon(context):
    command = [
        'usbipd',
    ]

    command += context.args

    return eusbip.utils.run(command)


@main.command()
@click.option('--device', 'devices', multiple=True)
def autobind(devices):
    try:
        while True:
            for device in devices:
                try:
                    eusbip.utils.run(
                        args=[
                            'usbip',
                            'bind',
                            '--busid', device,
                        ],
                        check=True,
                    )
                except subprocess.CalledProcessError:
                    pass
            time.sleep(2)
    except KeyboardInterrupt:
        click.echo('eusbip autobind termination requested, exiting')
        pass


@main.command()
@click.option('--remote')
@click.option('--device', 'devices', multiple=True)
def autoattach(remote, devices):
    try:
        while True:
            for device in devices:
                try:
                    eusbip.utils.run(
                        args=[
                            'usbip',
                            'attach',
                            '--remote', remote,
                            '--busid', device,
                        ],
                        check=True,
                    )
                except subprocess.CalledProcessError:
                    pass
            time.sleep(2)
    except KeyboardInterrupt:
        click.echo('eusbip autoattach termination requested, exiting')
        pass
