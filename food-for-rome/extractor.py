import sys
from subprocess import check_output
from shlex import split


if __name__ == "__main__":
    tables = check_output(split("mdb-tables -1 {0}".format(sys.argv[1]))).split("\n")
    for table in tables:
        if table == '':
            continue
        with open("{0}.csv".format(table.replace(" ", "_").replace("/", "-")), 'w') as f:
            f.write(check_output(split("mdb-export {0} '{1}'".format(sys.argv[1], table))))
