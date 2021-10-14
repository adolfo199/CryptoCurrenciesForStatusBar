# Crypto Currencies price tracker for status bars

## Dependencies

-   python(v>=3.0)

## Instalation

1. Clone this repository and copy their folder to /usr/share/
2. Make a folder named CryptoBarModule on ~/.config
3. Copy the example.config.json file from this repository to ~ / .config / CryptoBarModule and rename it to config.json
4. execute with python 3

```console
user@bar:~$ git clone https://github.com/adolfo199/CryptoCurrenciesForBar.git
user@bar:~$ cp -r CryptoCurrenciesForBar/ /usr/share/
user@bar:~$ mkdir ~/.config/CryptoBarModule
user@bar:~$ cp CryptoCurrenciesForBar/example.config.json ~/.config/CryptoBarModule/config.json
user@bar:~$ python3 /usr/share/CryptoCurrenciesForBar/main.py
BTC $57362.07 1.88% 0 | 1INCH $2.96 2.11% 28.06 | O3 $2.16 89.54 | T:$117.60

```

### Polybar

1. Put this module on your polybar config file

```console
[module/crypto]
type = custom/script
interval = 5
format-prefix = " "
format-prefix-foreground = #ffd200
format = <label>
exec = python3 ~/.config/CryptoCurrenciesForBar/main.py
format-underline = #858585
```

2. and call it with

```console
modules-center = crypto
```

### DwmBlocks

1. Put this element in your
   constant blocks from your config.h file

```c
static const Block blocks[] = {
//   Icon    Command                          Update Interval     Update Signal
    ....
    {"",    "python3 ~/.config/CryptoCurrenciesForBar/main.py" ,60,               0}
    ....
};
```

2. Recompile your Dwm

```console
user@bar:~$ cd path/to/dwm/source/directory
user@bar:~$ sudo make clean install
```
