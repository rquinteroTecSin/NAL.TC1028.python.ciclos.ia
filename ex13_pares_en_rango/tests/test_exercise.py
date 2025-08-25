
import builtins
from importlib import import_module, reload
def run_io(inputs):
    it = iter(inputs.splitlines()); orig = builtins.input; builtins.input = lambda: next(it)
    try: mod = import_module("src.exercise"); reload(mod); mod.main()
    finally: builtins.input = orig
def test_4_9(capsys):
    run_io("4\n9\n"); assert capsys.readouterr().out.strip().splitlines() == ["4","6","8"]
def test_3_3(capsys):
    run_io("3\n3\n"); assert capsys.readouterr().out.strip() == "No hay pares"
def test_9_2(capsys):
    run_io("9\n2\n"); assert capsys.readouterr().out.strip().splitlines() == ["2","4","6","8"]
