[no-cd]
python-lint year day part:
    ruff format {{ year }}/day_{{ day }}/part_{{ part }}.py &
    ruff check --fix {{ year }}/day_{{ day }}/part_{{ part }}.py &
    mypy {{ year }}/day_{{ day }}/part_{{ part }}.py

python-run year day part:
    uv run {{ year }}/day_{{ day }}/part_{{ part }}.py

ocaml-lint year day part:
    ocamlformat -i {{ year }}/day_{{ day }}/part_{{ part }}.ml

ocaml-run year day part:
    dune exec {{ year }}/day_{{ day }}/part_{{ part }}.exe
