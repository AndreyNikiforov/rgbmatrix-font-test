# RGB Matrix Font test

Goal is to showcase different fonts on rgb matrix display

# Install


## pipkin
```shell
pip install pipkin
```

## libs
```shell
pipkin -d lib install adafruit-circuitpython-display-text  adafruit-circuitpython-bitmap-font
```

## fonts

- download font release from TBD
- extract
- copy contents of the lib folder into lib folder of project (only some will fit)

## copy to the board

on the host:

```shell
cp -r -v ./src/* /Volumes/CIRCUITPY && cp -r -v -n ./lib/* /Volumes/CIRCUITPY/lib
```






