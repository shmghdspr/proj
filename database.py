
class TOKENIZE :

    def tokenize(self, query) :

        self.token = []                                          #tokenize query
        self.word =""
        query = query[:len(query)-1]
        for i in query :
            if i == " " :
                self.token.append(self.word)
                self.word = "" 
            else:
                self.word += i
        self.token.append(self.word)
        #print(self.token)
        return(self.token)


class indexing_headers :
    def indexing (self, file_of_tables = "user.txt") :
            with open(file_of_tables  , "r") as f :
                headers= f.readline()
                headers = headers.strip().split(" ")
            f.close()
            return(headers)
               


                                                                         
class INSERT(TOKENIZE) :                                        #INSERT
    
                                                                #query form : INSERT INTO <table_name> VALUES (<field1_name>,<field2_name>);
    def insert (self, query) :

        token = TOKENIZE.tokenize(self,query)

        self.table_name = token[2]
        with open( self.table_name + ".txt" , "a" ) as f :
            
            
            for i in token[4:] :
               
                f.write( i + " ")
            f.write("\n")
        


class DELETE(TOKENIZE) :                                         #query form : DELETE FROM <table_name> WHERE <field_name>==<field_value> OR <field_name>==<field_value>                   
    
    def delete(self, query) :

         token = TOKENIZE.tokenize(self,query)
        
         self.table_name = token[2]
         del1 = token[4].split("==")
         del2 = token[6].split("==")

         h = indexing_headers.indexing(self.table_name + ".txt")
         for i in range(len(h)) :
            if h[i] == del1[0] :
                 insdex_of_field_of_value_tobe_delete1 = i
            elif h[i] == del2[0] :
                 insdex_of_field_of_value_tobe_delete2 = i
            else :
                pass

         
         
         with open( self.table_name + ".txt" , "r" ) as f :                  #delete  line of file
            lines = f.readlines()
            
            lines_strip =[]
            for line in lines :
                line = line.strip().split(" ")
                lines_strip.append(line)

        


           # print(lines_strip)
            for line in lines_strip :
                
               # print(line)
                if (line[insdex_of_field_of_value_tobe_delete1] == del1[1])  or (line[insdex_of_field_of_value_tobe_delete2] == del2[1]) :
                    
                    inde= lines_strip.index(line)
                    #print(inde)
                    del lines_strip[inde]
                   # print(lines_strip)
            
         
         new_file = open(self.table_name + ".txt" , "w" )                    #update file after delete
         
         for line in lines_strip :                                           #change list to string for input to write
             stri = ""
             for i in line :
                 stri += i
                 stri += " "

             new_file.write(stri)
             new_file.write("\n")
         new_file.close()
             
class SELECT(TOKENIZE) :
    def select (self, query) :
        token = TOKENIZE.tokenize(self,query)
        self.table_name = token[2]
        selc1 = token[4].split("==")
        selc2 = token[6].split("==")

        
        h = indexing_headers.indexing(self.table_name + ".txt")
        for i in range(len(h)) :
            if h[i] == selc1[0] :
                 insdex_of_field_of_value_tobe_select1 = i
            elif h[i] == selc2[0] :
                 insdex_of_field_of_value_tobe_select2 = i
            else :
                pass
        
        with open( self.table_name + ".txt" , "r" ) as f :                  #select  line of file
            lines = f.readlines()
            print(lines)
            
            lines_strip =[]
            for line in lines :
                line = line.strip().split(" ")
                lines_strip.append(line)


            for line in lines_strip :
                if token[5] == "OR" :
               
                    if (line[insdex_of_field_of_value_tobe_select1] == selc1[1])  or (line[insdex_of_field_of_value_tobe_select2] == selc2[1]) :
                    
                        inde= lines_strip.index(line)
                        print( lines_strip[inde] )
                
                elif token[5] == "AND" :
                    if (line[insdex_of_field_of_value_tobe_select1] == selc1[1])  and (line[insdex_of_field_of_value_tobe_select2] == selc2[1]) :
                    
                        inde= lines_strip.index(line)
                        print( lines_strip[inde] )
                else:
                    pass

class UPDATE(TOKENIZE) :
            def update(self, query) :
                token = TOKENIZE.tokenize(self,query)
                self.table_name = token[1]
                ex1 = token[3].split("==")
                ex2 = token[5].split("==")

                h = indexing_headers.indexing(self.table_name + ".txt")
                for i in range(len(h)) :
                     if h[i] == ex1[0] :
                         insdex_of_field_of_value_tobe_update1 = i
                     elif h[i] == ex2[0] :
                         insdex_of_field_of_value_tobe_update2 = i
                     else :
                         pass

                with open( self.table_name + ".txt" , "r" ) as f :                  #update  line of file
                    lines = f.readlines()
                    #print(lines)
            
                    lines_strip =[]
                    for line in lines :
                        line = line.strip().split(" ")
                        lines_strip.append(line)
                    
                    for line in lines_strip :
                        if (line[insdex_of_field_of_value_tobe_update1] == ex1[1])  or (line[insdex_of_field_of_value_tobe_update2] == ex2[1]) :
                    
                            inde= lines_strip.index(line)
                            del lines_strip[inde]
                            #print( lines_strip[inde] )

                
                            new_line = token[7:]
                            lines_strip.append(new_line)
               
                            #print(new_line)      
                
                new_file = open(self.table_name + ".txt" , "w" )                    #update file after delete
         
                for line in lines_strip :                                           #change list to string for input to write
                    stri = ""
                    for i in line :
                        stri += i
                        stri += " "

                    new_file.write(stri)
                    new_file.write("\n")
                new_file.close()
