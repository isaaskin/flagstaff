import unittest

import click

from flagstaff import Command, generate_command, generate_node_from_command


class TestFlagstaff(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_generate_command(self):
        command = generate_command(Command("test", lambda: print("text")))
        self.assertTrue(isinstance(command, click.Command))
        self.assertEqual(command.name, "test")

    def test_generate_node_from_class_command(self):
        self.assertTrue(isinstance(generate_node_from_command(Command(
            name="show",
            target=lambda: print('show'),
            options={
                '--frequency': {
                    'required': True,
                    'type': int,
                    'nargs': 2
                },
                '--duty': {

                }
            }
        )), click.Command))

    def test_generate_node_from_class_group(self):
        self.assertTrue(isinstance(generate_node_from_command(Command(
            name="list",
            target=Command(
                name="up",
                target=lambda: print('up')
            )
        )), click.Group))
