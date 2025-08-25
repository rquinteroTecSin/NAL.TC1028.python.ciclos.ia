
import builtins
from importlib import import_module, reload
def run_io(inputs):
    it = iter(inputs.splitlines()); orig = builtins.input; builtins.input = lambda: next(it)
    try: mod = import_module("src.exercise"); reload(mod); mod.main()
    finally: builtins.input = orig
def test_b_zero(capsys):
    run_io("3\n0\n"); assert capsys.readouterr().out.strip() == "0"
def test_a_zero(capsys):
    run_io("0\n4\n"); out = capsys.readouterr().out.strip().splitlines()
    assert out == ["0 4","0 2","0 1","0"]
def test_37_12(capsys):
    run_io("37\n12\n"); out = capsys.readouterr().out.strip().splitlines()
    assert out == ["37 12","74 6","148 3","296 1","444"]
def test_12_37(capsys):
    run_io("12\n37\n"); out = capsys.readouterr().out.strip().splitlines()
    assert out == ["12 37","24 18","48 9","96 4","192 2","384 1","444"]
