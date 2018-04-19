#Database
pid='P.ID.,,'
lname='League Name,,'
name='Full Name,,'
age = 'age,,'
sal='SALARY,,'
position='Position\n'
table = []
index = None
def createDatabase() :
    #checking if file exists or not
    import os.path
    if not os.path.isfile('pythonDB.txt') :
        #if file doesn't exist then creating a new file
        fo = open('pythonDB.txt','w')
        fo.close()
    else :
        print('Database is already created')


#making my own error to use while inserting the data
#for not null constraint
class NotNull(Exception) :
    pass
#for limiting the size of the input
class OverFlow(Exception) :
    pass
class UnderFlow(Exception) :
    pass
class UniqueConstraint(Exception) :
    pass


#craeting a function to write in file
def writeFile(row) :
    try :
        #checking if file exist or not
        import os.path
        #if file doesn't exist  then raising an error
        if not os.path.isfile('pythonDB.txt') :
            raise FileNotFoundError
        #if file exists then wrting the value in tuple iti the file
        else :
            fa = open('pythonDB.txt','a')
            for i in row :
                fa.write(i)
            fa.close()
    except FileNotFoundError :
        print('database does not exist !! create a new database')

def readFile() :
    try :
        with open('pythonDB.txt','r') as fr :
            l = [tuple(map(str, i.split(',,'))) for i in fr]
        return l
    except FileNotFoundError :
        print('database does not exist')

#creating a function to insert values into the table
def insertTable(pid,name,age,lname,sal,position) :#pid,name,age,lname,sal,position) :
    try :
        #global pid,name,age,lname,sal,position
        flag = 0
        #inserting pid
        # pid = input('enter value of P.ID.\t')
        pid = pid.strip()
        pid = pid.upper()
        z = readFile()
        for i in range(len(z)) :
            if pid == z[i][0] :
                flag = 1
                break
            else :
                flag = 0
        if flag == 1 :
            raise UniqueConstraint('')
        #checking for not null constraint
        elif len(pid) == 0 :
            n = 'P.ID.'
            raise NotNull('')
        #checking for length of size
        elif len(pid) > 5 :
            n = 5
            raise OverFlow('')
        else :
            #added ',,' at last so that while reading from file i can seperate out the values
            pid = pid.upper()+',,'
        #HAVE TO  ADD UNIQUNESS CONSTRAINT HERE

        #inserting full name
        # name = input('enter the full name\t')
        if len(name) == 0 :
            n = 'First Name'
            raise NotNull('')
        elif len(name) > 30 :
            n = 30
            raise OverFlow('')

        else :
            name = name.capitalize()+',,'
        #inserting age
        # age=input('insert player age')
        age = age + ',,'


        #inserting league name
        # lname = input('enter the league name\t')
        if len(lname) == 0 :
            n = 'Last Name'
            raise NotNull('')
        elif len(lname) > 30 :
            n = 30
            raise OverFlow('')

        else :
            lname = lname.capitalize()+',,'

        #inserting player salary
        # sal = input('enter the player salary\t')
        if len(sal) == 0 :
            n = 'SALARY'
            raise NotNull('')
        elif not sal.isdigit() :
            n = 'numbers'
            raise ValueError

        else :
            sal = sal+',,'



        #inserting position
        # position = input('enter player position\t')

        #here checking that only position contains alphabets and blankspace
        if not(position.isalpha() or any(i == ' ' for i in position)) :
            n = '"alphabets" or " "'
            raise ValueError('')
        else :
            position = position.title()+',,'

        # pic = input('enter the image name')
        pic = pic+'\n'

        #inserting all the values in tuple
        t=(pid,name,age,lname,sal,position,pic)
        #calling the write in  file function to insert all the entries scanned from user
        writeFile(t)
        print(t)
        return t



    except NotNull :
        print(n,'cannot be null')
        return("input cannot be null")
    except OverFlow :
        print('word limit is',n)
        return "word limit is 30"
    except ValueError :
        print('input should contain only',n)
        return"enter value correctly"
    except UnderFlow :
        print('length of input should not be less than',n)
    except UniqueConstraint :

        print('P.ID. should be unique')
        return"pid cannot be null"





def printTable() :
    try :
        '''fr = open('pythonDB.txt','r')
        l = [tuple(map(str, i.split(',,'))) for i in fr]
        l.sort()'''
        l = readFile()
        l.sort()
        global pid,name,age,lname,sal,position
        pid='P.ID.'
        lname='League Name'
        name='First Name'
        age='age'
        sal='SALARY'
        position='Position\n'
        t=(pid,name,age,lname,sal,position)
        l.insert(0,t)
        for i in l :
            print(i)
        '''for i in l :
            for j in i :
                print(j+'\t',end=' ')
            print()'''
        return l

    except FileNotFoundError :
        print('database does not exist create a new database!!')



def search() :
    try :
        p = input('enter the P.ID. you want to search\t')
        p = p.upper()
        '''with open('pythonDB.txt','r') as fr :
            l = [tuple(map(str, i.split(',,'))) for i in fr]
        l.sort()'''
        l = readFile()
        l.sort()
        flag = 0
        for i in range(len(l)) :
            if p == l[i][0] :
                flag = 1
                break
        if flag == 1 :
            print(l[i])
        else :
            print('no entry found')

    except FileNotFoundError :
        print('database does not exist create a new database!!')



def firstTuple() :
    try :
        l = readFile()
        l.sort()
        print(l[0])
        global index
        index = 0
        return(l[0])
    except FileNotFoundError :
        print('database does not exist create a new database!!')
    except  IndexError :
        print('database is empty')


def lastTuple() :
    try :
        l = readFile()
        l.sort()
        print(l[len(l)-1])
        global index
        index = len(l)-1
        return l[index]

    except FileNotFoundError :
        print('database does not exist create a new database!!')
    except  IndexError :
        print('database is empty')

def nextTuple() :
    try :
        l = readFile()
        l.sort()
        global index
        if index == len(l)-1 :
            print('table finished')
        elif index == None :
            print('select a row first')
        else :
            index += 1
            print(l[index])
            return(l[index])
    except FileNotFoundError :
        print('database does not exist')

def prevTuple() :
    try :
        l = readFile()
        l.sort()
        global index
        if index == 0 :
            print('table finished')
        elif index == None :
            print('select a row first')
        else :
            index -= 1
            print(l[index])
            return(l[index])
    except FileNotFoundError :
        print('database does not exist')


def delete() :
    try :
        l = readFile()
        p = input('enter the P.ID.')
        p = p.upper()
        for i in range(len(l)) :
            if  p == l[i][0] :
                flag = 1
                break
            else :
                flag = 0
        if flag == 1 :
            del(l[i])
            l1=[]
            for j in l :
                l1.append(',,'.join(j))
            with open('pythonDB.txt','w') as fw :
                fw.writelines(l1)
        else :
            print('no data found')
    except FileNotFoundError:
        print('database not found')

def update() :
    try :
        p = input('enter pid whose data you have to update')
        p = p.upper()
        l = readFile()
        for i in range(len(l)) :
            if p == l[i][0] :
                flag = 1
                print(l[i])
                break
            else :
                flag = 0

        if flag == 1 :
            with open('pythonDB.txt','r') as fr :
                l1 = fr.readlines()
            global pid, name, age, lname, sal, position
            #inserting first name
            name = input('enter the full name\t')
            if len(name) == 0 :
                n = 'First Name'
                raise NotNull('')
            elif len(name) > 30 :
                n = 30
                raise OverFlow('')
            #checking if first name contains only alphabets

            else :
                name = name.capitalize()+',,'
            #insering age
            age=input('insert player age')
            age = age + ',,'


        #inserting last name
            lname = input('enter the last name\t')
            if len(lname) == 0 :
                n = 'Last Name'
                raise NotNull('')
            elif len(lname) > 10 :
                n = 10
                raise OverFlow('')
            elif not lname.isalpha() :
                n = 'alphabets'
                raise ValueError('')
            else :
                lname = lname.capitalize()+',,'

            #inserting player salary
            sal = input('enter the player salary\t')
            if len(sal) == 0 :
                n = 'Salary'
                raise NotNull
            elif not sal.isdigit() :
                n = 'numbers'
                raise ValueError

            else :
                sal = sal+',,'



            #inserting position
            position = input('enter the player position\t')

            #here checking that only position contains alphabets and blankspace
            if not(position.isalpha() or any(i == ' ' for i in position)) :
                n = '"alphabets" or " "'
                raise ValueError
            else :
                position = position.title()+'\n'

            t = pid+name+lname+sal+position
            l1[i] = t
            with open('pythonDB.txt','w') as fw :
                fw.writelines(l1)
        else :
            print('data not found with pid',p)

    except NotNull :
        print(n,'cannot be null')
    except OverFlow :
        print('word limit is',n)
    except ValueError :
        print('input should contain only',n)
    except UnderFlow :
        print('length of input should not be less than',n)



import sys
'''
while(True) :
    try :
        a = int(input('\n1\tcreate table\n2\tinsert in table\n3\tprint table\n4\tprint first row of table\n5\tprint last row of table\n6\tsearch\n7\tprint next row\n8\tprint previous row\n9\tupdate\n10\tdelete\n11\texit\nenter\t'))
        if a == 1 :
            createDatabase()
        elif a == 2 :
            insertTable()
        elif a == 3 :
            printTable()
        elif a== 4 :
            firstTuple()
        elif a == 5 :
            lastTuple()
        elif a == 6 :
            search()
        elif a== 7 :
            nextTuple()
        elif a == 8 :
            prevTuple()
        elif a == 9 :
            update()
        elif a == 10 :
            delete()
        elif a== 11 :
            sys.exit()
        else :
            print("enter value from 1 to 11")
    except ValueError :
        print("enter value correctly")

'''