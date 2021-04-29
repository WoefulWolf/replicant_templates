# NieR:Replicant ver.1.22474487139 Tools

## Archive (.arc) Files
* Hex Signature: `28 B5 2F FD`
* Can contain one or multiple compressed files.
* Files are compressed using [zstd](https://facebook.github.io/zstd/) (version >= 0.8.0)
* Usually contain PACK files (which store more files) or BXON files.

## PACK Files
* Hex Signature: `50 41 43 4B`.
* Can contain one or multiple BXON files.
* Organizes contained files by header structures, and then all asset data at end.
* TODO

## BXON Files
| Type | Description | Offset | Size | Comments |
| --- | --- | --- | --- | --- |
| char[4] | id | 0x0 | 0x4 | `BXON` |
| uint32 | version | 0x4 | 0x4 | Replicant uses `3` |
| n/a | projectID | 0x8 | 0x4 | Format Unknown |
| uint32 | offsetToAssetTypeName | 0xC | 0x4 | AssetTypeNames have variable length |
| uint32 | offsetToAssetTypeData | 0x10 | 0x4 |  |

* Hex Signature: `42 58 4F 4E`
* Contains game asset headers.
* Some common labels include:
	* tpXonAssetHeader
	* tpGxMeshHead
	* tpGxTexHead
* TODO

## tpGxMeshHead
* Contains all things mesh geometry!
* A lot more that is too much to put here, check out the binary template.
<br>

# Scripts

## decompress_archive.py

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