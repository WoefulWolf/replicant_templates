import os, sys, re, zstandard, traceback

archive_name = sys.argv[1].split("\\")[1].split(".")[0]

print("Reading input file...")
in_file = open(sys.argv[1], "rb")
data = in_file.read()
in_file.close()

print("Finding file segments...")
zsdt_sig_pattern = rb"\x28\xB5\x2F\xFD"
pat_regex = re.compile(zsdt_sig_pattern)

offsets = []
for match_obj in pat_regex.finditer(data):
    offset = match_obj.start()
    offsets.append(offset)

subdir = "./" + "uncompressed_" + archive_name

if not os.path.exists(subdir):
    os.mkdir(subdir)

dctx = zstandard.ZstdDecompressor()
errors = []
for i in range(len(offsets)):
    start_offset = offsets[i]

    if (i+1 > len(offsets)-1):   
        end_offset = len(data)
    else:
        end_offset = offsets[i+1]

    print("Decompressing segment", start_offset, "-", end_offset)
    data_segment = data[start_offset:end_offset]
    try:
        decompressed = dctx.decompress(data_segment)
    except:
        errors.append(["[!] ERROR: COULD NOT DECROMPRESS SEGEMENT " + str(start_offset) + " - " + str(end_offset), traceback.format_exc()])
        continue

    out_file_name = str(i) + "_uncompressed_" + sys.argv[1].split("\\")[1]
    out_file = open(subdir + "/" + out_file_name, "wb")
    out_file.write(decompressed)
    out_file.close()

for err in errors:
    print(err[0])
    print(err[1])