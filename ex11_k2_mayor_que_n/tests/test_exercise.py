
import builtins
from importlib import import_module, reload
def run_io(inputs):
    it = iter(inputs.splitlines()); orig = builtins.input; builtins.input = lambda: next(it)
    try: mod = import_module("src.exercise"); reload(mod); mod.main()
    finally: builtins.input = orig
def test_30(capsys):
    run_io("30\n"); assert capsys.readouterr().out.strip() == "6"
def test_0(capsys):
    run_io("0\n"); assert capsys.readouterr().out.strip() == "1"
def test_24(capsys):
    run_io("24\n"); assert capsys.readouterr().out.strip() == "5"
