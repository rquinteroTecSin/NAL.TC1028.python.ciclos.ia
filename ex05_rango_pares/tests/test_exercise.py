
import builtins
from importlib import import_module, reload
def run_io(inputs):
    it = iter(inputs.splitlines()); orig = builtins.input; builtins.input = lambda: next(it)
    try: mod = import_module("src.exercise"); reload(mod); mod.main()
    finally: builtins.input = orig
def test_3_12(capsys):
    run_io("3\n12\n"); out = capsys.readouterr().out.strip().splitlines()
    assert out == ["4","6","8","10","12"]
def test_0_5(capsys):
    run_io("0\n5\n"); out = capsys.readouterr().out.strip().splitlines()
    assert out == ["0","2","4"]
def test_4_4(capsys):
    run_io("4\n4\n"); assert capsys.readouterr().out.strip() == "4"
