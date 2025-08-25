
import builtins
from importlib import import_module, reload
def run_io(inputs):
    it = iter(inputs.splitlines()); orig = builtins.input; builtins.input = lambda: next(it)
    try: mod = import_module("src.exercise"); reload(mod); mod.main()
    finally: builtins.input = orig
def test_1(capsys):
    run_io("1\n2\n0\n"); assert capsys.readouterr().out.strip() == "3"
def test_2(capsys):
    run_io("100\n200\n0\n"); assert capsys.readouterr().out.strip() == "300"
def test_3(capsys):
    run_io("1\n-1\n0\n"); assert capsys.readouterr().out.strip() == "0"
