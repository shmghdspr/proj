from ast import alias
from datetime import datetime
from time import time
import database

class READFILE() :
    def read_file(file_name) :
        with open(file_name + ".txt" , "r") as f :     
            lines = f.readlines()
            lines_strip =[]
            for line in lines :
                line = line.strip().split(" ")
                lines_strip.append(line)
            return(lines_strip)


class app(READFILE) :

    def show_info(self , d):             # d ye dicte ke key hash field ha v value hash value haye motanazere useran

        lines_strip = READFILE.read_file("hesab")         
        headers =  lines_strip[0]
        for line in lines_strip :
            
            if str(line[2]) == d["national_code"] and str(line[3]) == d["password"]:                            #2=index nationalcode to headeraye hesab, 3=password
                   line_of_userinfo = line                             #pas ma hesab ro ba codemeli , password peyda mikonim
                   z = zip(headers, line_of_userinfo)
                   dictt = dict(z)
        print("""
        what dou you want to show?
        1.account_type
        2.Mojodi
        3.liste trakonesh ha                                        # chra select nmikhad?://///
        """)
        cho = int(input("iinput number(1-3)"))
        if cho == 1 :
            print(dictt["account_type"])
        elif cho == 2 :
            print(dictt["Mojodi"])
        elif cho == 3:
            listt =[]
            alia = dictt["alias"]
            lines_strip = READFILE.read_file("trakonesh_list")         
            headers =  lines_strip[0]
            for line in lines_strip :
                if str(line[1]) == alia or str(line[2]) == alia :  
                    listt.append(line)
            print(listt)
        else :
            print("error")

    
    def create_account (self, d):
        alias = input("input an alias for your account:")
        password = input("input an password for your account:")
        query  = "INSERT INTO hesab VALUES {alias} {password} {national_code} customer 0;".format( alias=alias, password=password, national_code=d["national_code"] )
        b = database.INSERT()
        b.insert(query)

    def management(self, d ) :
        print("""
        what do you want to do?
        1. sakhte hesabe jadid
        2. moshahede etelate hesab
        3. sakht alias baraye hesab
        """)
        choicee = int(input("input a number (1-3)"))
        if choicee == 1 :
            app.create_account (self, d)
        elif choicee == 2 :
            app.show_info(self, d)
        elif choicee == 3 :
            passw = input("input the password of an account wanto to define an alias for it : ")
            aliass = input("input the alias of an account : ")
            s = STARTAPP()
            lines_strip = s.read_file("hesab")         
            headers =  lines_strip[0]
            for line in lines_strip :
            
                if str(line[1]) == passw :                            #index of passw in list of headers of table files : 1
                   line_of_userinfo = line
                   z = zip(headers, line_of_userinfo)
                   dictt = dict(z)
                   dictt["alias"] = aliass                        #update bayad beshe
                   break

    def enteghal_vajh(self , d) :    # d inja dige bayad male hesab bashe na user
        alia = input("input password of your account :")
        passw = input("input password of your account :")

        national_code = d["national_code"]
        with open ("hesab.txt" , "r") as f :
            r = READFILE.read_file(f)
            headers =  r[0] 
            for line in r:
            
                if str(line[2]) == national_code :                            
                   line_of_userinfo = line
                   z = zip(headers, line_of_userinfo)
                   dictt2 = dict(z)
            if dictt2["hesab_password"] == passw :
                pass 
            else :
                print("password is wrong")
           
        mablagh = int(input("input mablaghe enteghal: "))
        
        print("""
        1.input hesabe maghsad
        2.entekhab az list useful account
        """)
        
        cho = int(input("input number (1-2)"))
        if cho == 1:
            hesabe_maghsad = input("input alias hesabe maghad: ") 
        else :
            with open ("usefull_account.txt" , "r") as f:
                list_of_usefull_account = READFILE.read_file(f)
                print(list_of_usefull_account)
                th = int(input("input shomare satri ke hesab mord nazaret dr oone"))
                hesabe_maghsad = list_of_usefull_account[th][0]   #0:index alias

        
        t = datetime.now().time()                 #trakonesh_list
        with open("trakonesh_list.txt" , "a") as f:
            query = "INSERT INTO trakonesh_list VALUES enteghale_vajh {alia} {hesabe_maghsad} {mablagh} {time};".format(alia=alia, hesabe_maghsad=hesabe_maghsad, mablagh=mablagh, time=t)
            i = database.INSERT()
            i.insert(query)

        with open ("hesab.txt" , "r") as f :      #MAGHSAD
            r = READFILE.read_file(f)
            headers =  r[0] 
            for line in r:
            
                if str(line[0]) == hesabe_maghsad :                            
                   line_of_userinfo = line
                   z = zip(headers, line_of_userinfo)
                   dictt = dict(z)
                   
                   mojodi = int(dictt["Mojodi"]) + mablagh
                   query =  "UPDATE hesab WHERE alias=={hesabe_maghsad} OR 1==1 VALUES {alias} {hesab_password} {national_code} {account_type} {Mojodi} {account_id};".format( hesabe_maghsad=hesabe_maghsad, alias=dictt["alias"], hesab_password=dictt["hesab_password"], national_code=dictt["national_code"], account_type=dictt["account_type"], Mojodi=mojodi, account_id=dictt["account_id"]  )    
                   u = database.UPDATE 
                   u.update(query)

        with open ("hesab.txt" , "r") as f :      #MABDA
            r = READFILE.read_file(f)
            headers =  r[0] 
            for line in r:
            
                if str(line[0]) == alia :                            
                   line_of_userinfo = line
                   z = zip(headers, line_of_userinfo)
                   dictt = dict(z)
                   
                   mojodi = int(dictt["Mojodi"]) - mablagh
                   query =  "UPDATE hesab WHERE alias=={alia} OR 1==1 VALUES {alias} {hesab_password} {national_code} {account_type} {Mojodi} {account_id};".format(alia=alia,  alias=dictt["alias"],  hesab_password=dictt["hesab_password"], national_code=dictt["national_code"], account_type=dictt["account_type"], Mojodi=mojodi, account_id=dictt["account_id"]  )     
                   u = database.UPDATE 
                   u.update(query)
    
    def pardakhte_ghabz(self , d):
        #id_ghabz = input("input shenase ghabz:")
        #id_pardakht = input("input shenase pardakht: ")
        mablagh_ghabz = int(input("input mablagh ghabz: "))
        national_code = d["national_code"]
        alias = d["alias"]
        with open ("hesab.txt" , "r") as f :          #hesab
            r = READFILE.read_file(f)
            headers =  r[0] 
            for line in r:
            
                if str(line[2]) == national_code :                            
                   line_of_userinfo = line
                   z = zip(headers, line_of_userinfo)
                   dictt3 = dict(z)
            
            alia = dictt3["alias"]
            mojodi = int(dictt3["Mojodi"]) - mablagh_ghabz
            query =  "UPDATE hesab WHERE alias=={alia} OR 1==1 VALUES {alias} {hesab_password} {national_code} {account_type} {Mojodi} {account_id};".format( alia=alia ,alias=dictt3["alias"], hesab_password=dictt3["hesab_password"], national_code=dictt3["national_code"], account_type=dictt3["account_type"], Mojodi=mojodi, account_id=dictt3["account_id"]  )     
            u = database.UPDATE ()
            u.update(query)

        t = datetime.now().time()                 #trakonesh_list
        with open("trakonesh_list.txt" , "a") as f:
            query = "INSERT INTO trakonesh_list VALUES ghabz {alia} - {mablagh} {time};".format(alia=alia, mablagh=mablagh_ghabz, time=t)
            i = database.INSERT()
            i.insert(query)

        with open("ghabz.txt" , "a") as f:
            query = "INSERT INTO ghabz VALUES ghabz {alias} {mablagh_ghabze} {time};".format(alias=alias, mablagh_ghabz=mablagh_ghabz, time=t)
            i = database.INSERT()
            i.insert(query)
    
    def darkhaste_vam(self, d) :
        mablagh = int(input("mablaghe vam mored nazar ra vared konid :"))
        dore_pardakht = 12
        ghest = mablagh/dore_pardakht
        national_code = d["national_code"]
        with open ("hesab.txt" , "r") as f :          #find mojodi
            r = READFILE.read_file(f)
            headers =  r[0] 
            for line in r:
            
                if str(line[2]) == national_code :                            
                   line_of_userinfo = line
                   z = zip(headers, line_of_userinfo)
                   dictt4 = dict(z)
            mojodi = int(dictt4["Mojodi"])
            mojodi += mablagh
            query =  "UPDATE hesab WHERE alias=={alia} OR 1==1 VALUES {alias} {hesab_password} {national_code} {account_type} {Mojodi} {account_id};".format( alia=dictt4["alias"] ,alias=dictt4["alias"], hesab_password=dictt4["hesab_password"], national_code=dictt4["national_code"], account_type=dictt4["account_type"], Mojodi=mojodi, account_id=dictt4["account_id"]  )     
            u = database.UPDATE ()
            u.update(query)
      
            
            while dore_pardakht!=0 :
                time.sleep(20)
                dore_pardakht -= 1
                mojodi = mojodi - ghest 
                query =  "UPDATE hesab WHERE alias=={alia} OR 1==1 VALUES {alias} {hesab_password} {national_code} {account_type} {Mojodi} {account_id};".format( alia=dictt4["alias"] ,alias=dictt4["alias"], hesab_password=dictt4["hesab_password"], national_code=dictt4["national_code"], account_type=dictt4["account_type"], Mojodi=mojodi, account_id=dictt4["account_id"]  )     
                u = database.UPDATE ()
                u.update(query)

    def bastane_hesab(self, d) :
        nationalcode = d["national_code"]
        query = "DELETE FROM hesab WHERE national_code=={nationalcode} or 1==1;".format(nationalcode=nationalcode)
        d = database.DELETE() 
        d.delete(query)


class STARTAPP(READFILE) :
    while True :
        print("""
        welcom to your mobile Bank
        what do you want to do?
        1.login
        2.signin
        """)
        n1 = int(input("input a number (1-2)"))
        
        if n1 == 1:          #login
            print("""
            if you want to login as a
            1. customer
            
            2. admin
            """)
            n2 = int(input("input a number (1-2)"))
           
            if n2 == 1 :                #customer
                national_code = input("please input your national code :")       #call UNIQUE checker
                password = input("please input your password : ")

                lines_strip = READFILE.read_file("user")         
                headers =  lines_strip[0]
                
                for line in lines_strip :
            
                    if (str(line[1]) == national_code) and (line[2] == password)  :                            #index of natinal code in list of headers of table files : 1
                        print("Login completed successfully")
                        line_of_userinfo = line
                        z = zip(headers, line_of_userinfo)
                        dictt = dict(z)

                        print("""
                        what do you want to do?
                        1. moshahede eteleate hesab
                        2. eftetah hesab
                        3. modiriate hesab
                        4. enteghale vajh
                        5. pardakht ghbz
                        6. darkhaste vam
                        7. bastan hesab
                        """)

                        menou_choice = int(input("input a number (1-6)"))
                        app = app()
                        if menou_choice==1 :
                            atrr = app.show_info( dictt )
                        elif menou_choice==2 :
                            atrr = app.create_account( dictt )
                        elif menou_choice==3 :
                            atrr = app.management( dictt )
                        elif menou_choice==4 :
                            atrr = app.enteghal_vajh( dictt )
                        elif menou_choice==5 :
                            atrr = app.pardakhte_ghabz( dictt )
                        elif menou_choice==6 :
                            atrr = app.darkhaste_vam( dictt )
                        elif menou_choice==7 :
                            atrr = app.bastane_hesab( dictt )
        

            elif n2 == 2 :              #admin
               pass

        elif n1 == 2 :                 #signin
            name = input("please enter your name :")
            national_code = input("please enter your national code :")
            password = input("please enter your password : ")
            phone_number = input("please enter your phone number :")
            email = input("please enter your email :")

            query  = "INSERT INTO user VALUES {name} {national_code} {password} {phone_number} {email};".format( name=name, national_code=national_code, password=password, phone_number=phone_number, email=email)
            b = database.INSERT()
            b.insert(query)

            print("""
            account shoma sakhte shod
            what do you want to do?
            1. khoroj az brname
            2. login to your account
            """)
            n3 = int(input("input a number (1-2)"))
            if n3 == 1:
                break
            elif n3 == 2 :
                pass

