# NieR:Replicant ver.1.22474487139 Tools

## Importing Game Models/Materials/Textures to Blender
https://github.com/WoefulWolf/Replicant2Blender

## Unpacking Game Archives & Textures
https://github.com/yretenai/kaine/

# Files

## Archive (.arc) Files
* Magic: `28 B5 2F FD`
* Can contain one or multiple compressed files.
* Files are compressed using [zstd](https://facebook.github.io/zstd/) (version >= 0.8.0)
* Usually contain PACK files (which store more files) or BXON files.

## All Other Files
* Just check the 010 Editor Binary Templates found in this repo.
* Running the `PACK.bt` template will automatically run the corresponding binary templates as well for the files found inside the PACK.

# Scripts

## decompress_archive.py (Pointless)

#### Note:
* Not really recommended at the moment, ignores structure and just tries to decompress anything it can.
* Recommended instead: https://github.com/yretenai/kaine

#### Requires:
* [Python 3](https://www.python.org/)
* [zstandard](https://pypi.org/project/zstandard/) 

#### Usage: 
`python ./archive_extractor.py <Archive Path>`

#### Description:
Attempts to decompress and separate the archive files into their uncompressed state. <br>
Uncompressed files will be placed in sub-directories adjacent to the Python script.

### If you wish to contribute or learn more, please check out the [NieR:Modding Discord Server.](https://discord.gg/7F76ZVv)
