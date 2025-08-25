
import builtins
from importlib import import_module, reload
def run_io(inputs):
    it = iter(inputs.splitlines()); orig = builtins.input; builtins.input = lambda: next(it)
    try: mod = import_module("src.exercise"); reload(mod); mod.main()
    finally: builtins.input = orig
def test_pos(capsys):
    run_io("4\n"); assert capsys.readouterr().out.strip() == "24"
def test_neg(capsys):
    run_io("-2\n"); assert capsys.readouterr().out.strip() == "Factorial no definido para negativos"
def test_zero(capsys):
    run_io("0\n"); assert capsys.readouterr().out.strip() == "1"
