# NieR:Replicant ver.1.22474487139 Tools

## Archive (.arc) Files
* Hex Signature: `28 B5 2F FD`
* Can contain one or multiple compressed files.
* Files are compressed using [zstd](https://facebook.github.io/zstd/) (version >= 0.8.0)
* Usually contain PACK files (which store more files) or BXON files.

## PACK Files
* Hex Signature: `50 41 43 4B` (Same as Quake Archive File, but could just a coincidence be due to `PACK` text lol).
* Can contain one or multiple BXON files.
* Organizes contained files in a directory structure with filenames.
* TODO

## BXON Files
* Hex Signature: `42 58 4F 4E`
* Contains game assets.
* Some common labels include:
	* tpXonAssetHeader
	* tpGxMeshHead
	* tpGxTexHead
* TODO

<br>

# Scripts

## decompress_archive.py
#### Requires:
* [Python 3](https://www.python.org/)
* [zstandard](https://pypi.org/project/zstandard/) 

#### Usage: 
`python ./archive_extractor.py <Archive Path>`

#### Description:
Attempts to decompress and separate the archive files into their uncompressed state. <br>
Uncompressed files will be placed in sub-directories adjacent to the Python script.

### If you wish to contribute or learn more, please check out the [NieR:Modding Discord Server.](https://discord.gg/7F76ZVv)