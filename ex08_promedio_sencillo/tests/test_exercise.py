
import builtins
from importlib import import_module, reload
def run_io(inputs):
    it = iter(inputs.splitlines()); orig = builtins.input; builtins.input = lambda: next(it)
    try: mod = import_module("src.exercise"); reload(mod); mod.main()
    finally: builtins.input = orig
def read_float(out):
    return float(out.strip().splitlines()[-1])
def test_sample(capsys):
    run_io("3\n2.5\n3.8\n4.6\n"); val = read_float(capsys.readouterr().out)
    assert abs(val - 3.633333333333333) < 1e-9
def test_single(capsys):
    run_io("1\n10\n"); val = read_float(capsys.readouterr().out)
    assert abs(val - 10.0) < 1e-9
def test_two(capsys):
    run_io("2\n-1.0\n3.0\n"); val = read_float(capsys.readouterr().out)
    assert abs(val - 1.0) < 1e-9
