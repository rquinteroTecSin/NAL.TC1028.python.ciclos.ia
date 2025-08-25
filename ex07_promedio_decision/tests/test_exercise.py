
import builtins
from importlib import import_module, reload
def run_io(inputs):
    it = iter(inputs.splitlines()); orig = builtins.input; builtins.input = lambda: next(it)
    try: mod = import_module("src.exercise"); reload(mod); mod.main()
    finally: builtins.input = orig
def read_float(out):
    return float(out.strip().splitlines()[-1])
def test_sample(capsys):
    run_io("2.5\n6.3\n4.7\n-2.1\n"); val = read_float(capsys.readouterr().out)
    assert abs(val - 4.5) < 1e-9
def test_with_zero(capsys):
    run_io("10\n0\n20\n-1\n"); val = read_float(capsys.readouterr().out)
    assert abs(val - (10+0+20)/3) < 1e-9
