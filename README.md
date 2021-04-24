# NieR:Replicant ver.1.22474487139 Tools

## Archive (.arc) Files
* Can contain one or multiple compressed files.
* Files are compressed using [zstd](https://facebook.github.io/zstd/) (version >= 0.8.0)
* Usually contain PACK files (which store more files) or BXON files.

## PACK Files
* Can contain one or multiple BXON files.
* Organizes contained files in a directory structure with filenames.
* TODO

## BXON Files
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