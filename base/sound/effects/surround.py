from . import echo
from .. import formats
from ..filters import equalizer

def test1():
    echo.test()

def test2():
    formats.wavread.test()

def test3():
    equalizer.test()

def testAll():
    echo.test()
    equalizer.test()
    print(formats)
    # formats.wavread.test() # ? 出错