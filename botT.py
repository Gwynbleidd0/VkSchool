import requests
import xlrd
import fille
import os
def get_timetable():
    import fille
    dirfile = 'https://s11028.edu35.ru/attachments/article/224/'
    file_name_list = fille.get_name_file()
    count_var=len(file_name_list)
    t1=False
    g=0
    while g<count_var:
        fille0 = file_name_list[g]
        r = requests.get(dirfile+fille0)
        if r.ok==True:
            with open('base.xls', "wb") as code:
                code.write(r.content)
                t1=True
                break
        g=g+1
    if t1==False:
        data = ''
        return(t1,data)
    if t1==True:
        data = fille.get_date()
        return(t1,data)
def get_timetable2():
    import parcer
    import fille
    t1=False
    res=parcer.get_url()
    r = requests.get(res[-1])
    if r.ok==True:
         with open('base.xls', "wb") as code:
             code.write(r.content)
             t1=True
    if t1==False:
        data = ''
        return(t1,data)
    if t1==True:
        data = fille.get_date()
        return(t1,data)
def get_book(class_number):
    rb =xlrd.open_workbook('base.xls')
    sheet = rb.sheet_by_index(0)
    #val = sheet.row_values(6)[85]
    print(sheet.ncols)
    print(sheet.nrows)

    i=0
    while i<sheet.ncols:
        if sheet.row_values(2)[i] == class_number:
            rownum = i

            break
        i=i+1
    print(rownum)
    f=3
    result=[]

    while f<sheet.nrows:
        result.append(sheet.row_values(f)[rownum])
        f=f+2
    print(result)
#    while 
    lessons=len(result)
    print(lessons)
    result_string=''
    s=0
    while s<lessons:
        if result[s]=='':
            result[s]='---------'
        result_string=result_string+result[s]+'\n'
        s=s+1
    return(result_string)
#print(get_timetable()[0])
#print(os.listdir(path="."))
def get_lastfille():
    files = [f for f in os.listdir('.') if f.endswith('.xls')]
    fille=files[0]
    return(fille)
#def check_updates():

#print(get_timetable2())    
"""
print(os.path.getmtime(files[0]))
i=0
while i<len(files):    
    os.path.getmtime(files[i])
    i=i+1"""
"""  
    while f<sheet.nrows:
        if sheet.row_values(f)[rownum]!='':
            result.append(sheet.row_values(f)[rownum])
        elif sheet.row_values(f+1)[rownum]!='':
            break;
        f=f+2
""" 


