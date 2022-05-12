# Sanzan

![PyPi](https://github.com/kokseen1/Sanzan/actions/workflows/release.yml/badge.svg)
![PyPI](https://img.shields.io/pypi/v/sanzan)

Quick and simple video obfuscation

## Demo

Encrypted Video:

![Encrypted](https://raw.githubusercontent.com/kokseen1/Sanzan/main/img/enc.gif?raw=True)

Decrypted Video:

![Decrypted](https://raw.githubusercontent.com/kokseen1/Sanzan/main/img/dec.gif?raw=True)

<!-- <p align="center">
 <p align="center">Obfuscated Video:<p align="center">
  <img src="https://raw.githubusercontent.com/kokseen1/Sanzan/main/img/obfuscated.png?raw=True" width="70%" alt="Obfuscated Video"/>
</p>

<p align="center">
 <p align="center">Deobfuscated Video:<p align="center">
  <img src="https://raw.githubusercontent.com/kokseen1/Sanzan/main/img/deobfuscated.png?raw=True" width="70%" alt="Deobfuscated Video"/>
</p> -->
 
## Installation

```shell
pip install sanzan
```

## Usage

### Encryption

```shell
sz -e original.mp4 -o encrypted.mp4
```


### Decryption

```shell
sz -d encrypted.mp4 -o decrypted.mp4 -k <keyfile>
```

## More Usage

When encrypting, use the optional `-k` flag to specify the path of the generated keyfile.

```shell
sz -e original.mp4 -o encrypted.mp4 -k <generated keyfile>
```

Use the optional `-p` flag to view a real time preview of the output. This flag can be used alone or along with the `-o` argument.

```shell
sz -d encrypted.mp4 -o decrypted.mp4 -k <keyfile> -p
```

Use the optional `-s` flag to hide the progress bar. Might improve performance.


## Note

- `cv2.waitKey` is unable to maintain a consistent playback framerate for `cv2.imshow`.

<!-- - `vidgear` is used for streaming, but will fall back to `YDL` if streaming is unavailable. -->

- Audio is not yet supported.
