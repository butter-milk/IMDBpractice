import pandas as pd
import argparse

#input: csv file
#tables: list of table names
#columns: list of attribute names and types corresponding to each table
def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--table", nargs='+', default=[] ,required=True)
    return parser.parse_args()


def main():
    print("Give all table names and the data: --input <csv> --table <name1>...<name420>")
    args = parse()
    data = pd.read_csv(args.input)
    f = open("table.sql", "w")

    for i in range(len(args.table)):
        title = args.table[i]
        print("Give all columns and types of this table")
        lst = [ ]
        n = int(input("Enter number of columns: "))
        for _ in range(0, n):
            print("Give column name and type in seperate strings:")
            ele = [input(), input()]
            lst.append(ele)

        f.write("Create table "+title[i]+" (\n")
        for j in range(len(lst)-1):
            f.write( lst[j][0]+" "+lst[j][1]+",\n")
        f.write(lst[len(lst)-1][0]+" "+lst[len(lst)-1][1])
        f.write(");\n")
        elements = data[[x[0] for x in lst]].values.tolist()

        for j in range(len(elements)):
            f.write("Insert into "+title+" values (")
            for k in range(len(elements[j])-1):
                if 'text' in lst[k][1].lower():
                    f.write("\'")
                f.write(str(elements[j][k]))
                if 'text' in lst[k][1].lower():
                    f.write("\',")
                else:
                    f.write(",")
            if 'text' in lst[len(elements[j])-1][1].lower():
                    f.write("\'")
            f.write(str(elements[j][len(elements[j])-1]))
            if 'text' in lst[len(elements[j])-1][1].lower():
                f.write("\'")
            f.write(");\n")
    




if __name__ == "__main__":
    main()