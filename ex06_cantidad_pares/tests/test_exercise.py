
import builtins
from importlib import import_module, reload
def run_io(inputs):
    it = iter(inputs.splitlines()); orig = builtins.input; builtins.input = lambda: next(it)
    try: mod = import_module("src.exercise"); reload(mod); mod.main()
    finally: builtins.input = orig
def test_sample(capsys):
    run_io("4\n3\n11\n42\n0\n-2\n"); assert capsys.readouterr().out.strip() == "Total de pares=3"
def test_none_even(capsys):
    run_io("1\n3\n5\n7\n-1\n"); assert capsys.readouterr().out.strip() == "Total de pares=0"
def test_many_zeros(capsys):
    run_io("0\n0\n0\n-5\n"); assert capsys.readouterr().out.strip() == "Total de pares=3"
