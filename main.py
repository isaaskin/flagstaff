from flagstaff import run, Command


run([
    Command(
        name="show",
        target=lambda frequency, duty: print('show', frequency),
        options={
            '--frequency': {
                'required': True,
                'type': int,
                'nargs': 2
            },
            '--duty': {
                'required': True,
                'type': int,
            }
        }
    ),
    Command(
        name="list",
        target=Command(
            name="up",
            target=lambda: print('up')
        )
    )
])
