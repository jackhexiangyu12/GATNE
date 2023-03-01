
if __name__ == '__main__':
    fn = 'train.txt'
    with open(fn,'r') as f:
        edges = ""
        for line in f.readlines():
            print(line)
            print(line.split())
            _,src,dst = line.split()
            edges+= src+" "+dst+"\n"
    output_fn = 'edgelists.txt'
    with open(output_fn,'w') as g:
        g.write(edges)
