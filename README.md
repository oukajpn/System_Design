# System Design

## Requirement
* RPi.GPIO
* spidev

## Install
```bash
pip install rpi.gpio
git clone git://github.com/doceme/py-spidev
cd py-spidev
sudo python setup.py install

```
## Activate SPI driver
```bash
/boot/config.txt
# Uncomment some or all of these to enable the optional hardware interfaces
#dtparam=i2c_arm=on
#dtparam=i2s=on
#dtparam=spi=on
dtparam=spi=on
```
Delete \# at "\#dtparam=spi=on" or add "dtparam=spi=on".  
After you have to reboot.
```bash
sudo reboot
```

## Usage
```bash
DustBox.py
```

## References
* [Raspberry PiのGPIO端子のスイッチ入力](https://qiita.com/rockhopper-penguin/items/fd3fe09cdbd04b2a5f86)
* [Raspberry Piで圧力センサーを使う](https://iinpht.jeez.jp/raspberrypi/raspberry-piで圧力センサーを使う)
* [Raspberry Pi はじめてのラズパイ：ステッピングモータをA4988ドライバで制御する](https://stemship.com/raspberry-pi-beginner-stepmotor/)
