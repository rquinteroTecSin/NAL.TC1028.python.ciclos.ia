
import builtins
from importlib import import_module, reload
def run_io(inputs):
    it = iter(inputs.splitlines()); orig = builtins.input; builtins.input = lambda: next(it)
    try: mod = import_module("src.exercise"); reload(mod); mod.main()
    finally: builtins.input = orig
def test_gcd_48_18(capsys):
    run_io("48\n18\n"); assert capsys.readouterr().out.strip() == "6"
def test_gcd_270_192(capsys):
    run_io("270\n192\n"); assert capsys.readouterr().out.strip() == "6"
def test_gcd_7_5(capsys):
    run_io("7\n5\n"); assert capsys.readouterr().out.strip() == "1"
def test_invalid_zero(capsys):
    run_io("7\n0\n"); assert capsys.readouterr().out.strip() == "Invalid input"
def test_invalid_negative(capsys):
    run_io("-8\n12\n"); assert capsys.readouterr().out.strip() == "Invalid input"
