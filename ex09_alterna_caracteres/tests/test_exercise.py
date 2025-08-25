
import builtins
from importlib import import_module, reload
def run_io(inputs):
    it = iter(inputs.splitlines()); orig = builtins.input; builtins.input = lambda: next(it)
    try: mod = import_module("src.exercise"); reload(mod); mod.main()
    finally: builtins.input = orig
def test_one(capsys):
    run_io("1\n"); assert capsys.readouterr().out.strip() == "1-#"
def test_four(capsys):
    run_io("4\n"); out = capsys.readouterr().out.strip().splitlines()
    assert out == ["1-#","2-%","3-#","4-%"]
def test_seven(capsys):
    run_io("7\n"); out = capsys.readouterr().out.strip().splitlines()
    assert out == ["1-#","2-%","3-#","4-%","5-#","6-%","7-#"]
