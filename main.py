class studentiki:
    id = 0
    fio = ''
    if_project = ''
    clas = ''
    score = 0
studens = []
f = open('students.csv')
j = 0
skip = f.readline()
for i in f:
    s=i.split(',')
    if int(s[3][:-1]) == 10:
        studens.append(studentiki())
        studens[j].id = s[0]
        studens[j].fio = s[1]
        studens[j].score = int (s[4])
        j += 1

for i in range(len(studens)-1):
    j = i
    t = studens[i]
    st = studens[i].score
    sid=studens[i].id
    while j>0 and studens[j-1].score>st and studens[j-1].id>sid:
        studens[j] = studens[j-1]
        j -= 1
    studens[j] = t

print(studens[0].fio,studens[0].id,studens[0].score)
print(studens[1].fio,studens[1].id,studens[1].score)
print(studens[2].fio,studens[2].id,studens[2].score)
