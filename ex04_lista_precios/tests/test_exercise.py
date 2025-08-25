
import builtins
from importlib import import_module, reload
def run_io(inputs):
    it = iter(inputs.splitlines()); orig = builtins.input; builtins.input = lambda: next(it)
    try: mod = import_module("src.exercise"); reload(mod); mod.main()
    finally: builtins.input = orig
def test_b_a_x(capsys):
    run_io("B\nA\nX\n"); out = capsys.readouterr().out.strip().splitlines()
    assert out == ["250","120","370"]
def test_c_x(capsys):
    run_io("C\nX\n"); out = capsys.readouterr().out.strip().splitlines()
    assert out == ["360","360"]
def test_a_b_c_x(capsys):
    run_io("A\nB\nC\nX\n"); out = capsys.readouterr().out.strip().splitlines()
    assert out == ["120","250","360","730"]
