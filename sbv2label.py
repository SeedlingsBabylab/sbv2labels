import sys

class SBVGroup:
    def __init__(self, start, end, content):
        self.start = start
        self.end = end
        self.content = content


def parse_sbv():
    time_line = ""
    content_line = ""

    count = 0
    groups = []
    with open(sbv_file, "rU") as input:

        for index, line in enumerate(input):
            if count == 0:
                time_line = line
            if count == 1:
                content_line = line
            if count == 2:
                group = parse_group(time_line, content_line)
                groups.append(group)
                time_line = ""
                content_line = ""
                count = 0
                continue
            count += 1

        return groups



def parse_group(time_line, content_line):

    time_split = time_line.split(",")
    onset_split = time_split[0].split(":")
    offset_split = time_split[1].split(":")

    onset_seconds = int(onset_split[0])*3600 + int(onset_split[1])*60 + float(onset_split[2])
    offset_seconds = int(offset_split[0])*3600 + int(offset_split[1])*60 + float(offset_split[2])

    group = SBVGroup(onset_seconds, offset_seconds, content_line)

    return group

def output_labels(groups):

    with open(label_out, "wb") as output:
        for group in groups:
            output.write("{:.6f} {:.6f} {}\n".format(group.start, group.end, group.content))

if __name__ == "__main__":

    sbv_file = sys.argv[1]
    label_out = sbv_file.replace(".sbv", ".labels")

    groups = parse_sbv()
    output_labels(groups)

    print groups