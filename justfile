[no-cd]
lint file:
    ruff format {{ file }} &
    ruff check --fix {{ file }} &
    mypy {{ file }}
