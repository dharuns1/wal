f = open('sample.txt','r')
data = f.readlines()
for i in data:
    row = i.strip().split(',')
    w = row[0].split('(')
    t = row[1].strip()
    n = row[2].strip().split(')')
    if t == 'DoubleType' or t == ' DoubleType' :
        t = "double"
    with open('output_file.txt', 'a') as output_file:
        print('{}:{},{}:"{}",{}:{},{}:{}'.format('{"name"', w[1], '"type"', t, '"nullable"', n[0], '"metadata"', '{}}'), file=output_file)
    output_file.close()
