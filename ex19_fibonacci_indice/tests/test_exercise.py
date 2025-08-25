
import builtins
from importlib import import_module, reload
def run_io(inputs):
    it = iter(inputs.splitlines()); orig = builtins.input; builtins.input = lambda: next(it)
    try: mod = import_module("src.exercise"); reload(mod); mod.main()
    finally: builtins.input = orig
def test_0(capsys):
    run_io("0\n"); assert capsys.readouterr().out.strip() == "0"
def test_3(capsys):
    run_io("3\n"); assert capsys.readouterr().out.strip() == "2"
def test_20(capsys):
    run_io("20\n"); assert capsys.readouterr().out.strip() == "6765"
