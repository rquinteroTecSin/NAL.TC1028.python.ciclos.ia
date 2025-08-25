
import builtins
from importlib import import_module, reload
def run_io(inputs):
    it = iter(inputs.splitlines()); orig = builtins.input; builtins.input = lambda: next(it)
    try: mod = import_module("src.exercise"); reload(mod); mod.main()
    finally: builtins.input = orig
def test_basic(capsys):
    run_io("1\n"); assert capsys.readouterr().out.strip() == "False"
    run_io("-3\n"); assert capsys.readouterr().out.strip() == "False"
    run_io("5\n"); assert capsys.readouterr().out.strip() == "True"
    run_io("2\n"); assert capsys.readouterr().out.strip() == "True"
    run_io("9\n"); assert capsys.readouterr().out.strip() == "False"
