from p3.classwork.day13clean_data import CleanData
def process_data(filename):
    f_w=open("day16cleandata.txt","w",encoding="utf-8")
    op=CleanData("dict.txt")
    with open(filename,"r",encoding="utf-8") as f:
        for line in f:
            line=line.strip("\n")
            newline=op.get_result(line)
            f_w.write(newline+"\n")
    f_w.close()
if __name__ == "__main__":
    process_data("../day15/text15.text")