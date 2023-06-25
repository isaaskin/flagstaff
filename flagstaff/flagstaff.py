import typing

import click

from .command import Command, Flagstaff


def generate_command(command: Command) -> click.Command:
    if not callable(command.target):
        raise ValueError('Target must be a callable')
    if command.options:
        for option in command.options:
            click.option(option, **command.options[option])(command.target)

    return click.command(name=command.name)(command.target)


def generate_node_from_command(command: Command) -> typing.Union[click.Command, click.Group]:
    if callable(command.target):
        return generate_command(command)
    elif isinstance(command.target, list) or isinstance(command.target, Command):
        def _g(): return None
        group = click.group(name=command.name)(_g)

        if isinstance(command.target, Command):
            nodes = [command.target]
        else:
            nodes = command.target
        for node in nodes:
            group.add_command(generate_node_from_command(node))
        return group
    else:
        raise ValueError("Unknown target")


def run(flagstaff: Flagstaff):
    def cli(): return None
    cli = click.group(cli)

    for node in flagstaff:
        cli.add_command(generate_node_from_command(node))

    # Run
    cli()