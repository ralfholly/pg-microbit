# PG MicroBit
A Playground for BBC micro:bit [MicroPython](http://microbit-micropython.readthedocs.io/en/latest) projects.


## Description
This playground lets you try out BBC micro:bit/MicroPython features and programming ideas. You can easily setup a safe try-out area in which you develop and unit test your app. It is based on the idea described in [this blog post](https://www.approxion.com/?p=2784).


## Usage
Enter the directory of the cloned repository and start a new topic:
```
cd ~/pg-microbit
. pg-setup step_counter
```
This will create a directory named `step_counter` that is equipped with a Makefile and a Python source code file named `script.py`. If you have defined the `EDITOR` environment variable, `script.py` will be opened in your favorite editor. Type `make install` to download your app to the BBC micro:bit device.


## Unit Testing
Unit tests are expected to be in the tests/ subfolder of an app. Execute your tests by executing `make test` or just `make`.
Within your app folder, you can find a Python module called `microbit.py` which contains predefined mocks for the API offered by MicroPython. On the real device the module `microbit` is part of the runtime; `microbit.py` is only used for host-based mocking/unit testing.


## Flashing
In order to download your script to your device, run `make install`, which calls the [uflash](https://github.com/ntoll/uflash) utility to get the job done.

## Dependencies

See `requirements.txt`. Install dependencies like so:

```
pip3 install --user -r requirements.txt
```
