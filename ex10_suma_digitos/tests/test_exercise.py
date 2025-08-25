
import builtins
from importlib import import_module, reload
def run_io(inputs):
    it = iter(inputs.splitlines()); orig = builtins.input; builtins.input = lambda: next(it)
    try: mod = import_module("src.exercise"); reload(mod); mod.main()
    finally: builtins.input = orig
def test_2975(capsys):
    run_io("2975\n"); assert capsys.readouterr().out.strip() == "23"
def test_neg_517(capsys):
    run_io("-517\n"); assert capsys.readouterr().out.strip() == "13"
def test_zero(capsys):
    run_io("0\n"); assert capsys.readouterr().out.strip() == "0"
