import click.testing

import eusbip.cli


def test_explore():
    runner = click.testing.CliRunner()
    runner.invoke(
        eusbip.cli.main,
        catch_exceptions=False,
    )

