
import builtins
from importlib import import_module, reload
def run_io(inputs):
    it = iter(inputs.splitlines()); orig = builtins.input; builtins.input = lambda: next(it)
    try: mod = import_module("src.exercise"); reload(mod); mod.main()
    finally: builtins.input = orig
def test_6(capsys):
    run_io("6\n"); assert capsys.readouterr().out.strip() == "21"
def test_1(capsys):
    run_io("1\n"); assert capsys.readouterr().out.strip() == "1"
def test_10(capsys):
    run_io("10\n"); assert capsys.readouterr().out.strip() == "55"
