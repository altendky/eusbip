import logging
import time

import click

import eusbip


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
        'sudo',
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
                eusbip.utils.run(
                    command=[
                        'sudo',
                        'usbip',
                        'bind',
                        '--busid', device,
                    ],
                    check=True,
                )
            time.sleep(2)
    except KeyboardInterrupt:
        click.echo('Autobind termination requested, exiting')
        pass
