
import builtins
from importlib import import_module, reload
def run_io(inputs):
    it = iter(inputs.splitlines()); orig = builtins.input; builtins.input = lambda: next(it)
    try: mod = import_module("src.exercise"); reload(mod); mod.main()
    finally: builtins.input = orig
def test_8(capsys):
    run_io("8\n"); assert capsys.readouterr().out.strip() == "8 4 2 1"
def test_3(capsys):
    run_io("3\n"); assert capsys.readouterr().out.strip() == "3 10 5 16 8 4 2 1"
def test_invalid(capsys):
    run_io("0\n"); assert capsys.readouterr().out.strip() == "Invalid input"
