
import builtins
from importlib import import_module, reload
def run_io(inputs):
    it = iter(inputs.splitlines()); orig = builtins.input; builtins.input = lambda: next(it)
    try: mod = import_module("src.exercise"); reload(mod); mod.main()
    finally: builtins.input = orig
def test_ok(capsys):
    run_io("1000\n10\n"); assert capsys.readouterr().out.strip() == "1104.71"
def test_error(capsys):
    run_io("1000\n-10\n"); assert capsys.readouterr().out.strip() == "Error en los datos"
