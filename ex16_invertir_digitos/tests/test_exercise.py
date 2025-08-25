
import builtins
from importlib import import_module, reload
def run_io(inputs):
    it = iter(inputs.splitlines()); orig = builtins.input; builtins.input = lambda: next(it)
    try: mod = import_module("src.exercise"); reload(mod); mod.main()
    finally: builtins.input = orig
def test_samples(capsys):
    run_io("123\n"); assert capsys.readouterr().out.strip() == "321"
    run_io("-8534\n"); assert capsys.readouterr().out.strip() == "-4358"
    run_io("12345678\n"); assert capsys.readouterr().out.strip() == "Too long"
    run_io("0\n"); assert capsys.readouterr().out.strip() == "0"
