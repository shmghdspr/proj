class schema :
    list_of_rows = []
    with open ("schema.txt" , "r" ) as schema:
        for row in schema :
            field = row.split()

            list_of_rows.append(field)


    
    table_counter = 1
    for i in range(len(list_of_rows)) :
        if list_of_rows[i] == [] :
            table_counter += 1


    database = []                #creat database
    for i in range(table_counter) :
       database.append([])
    

    j = 0                                   
    for i in list_of_rows :
        if i != [] :
           database[j].append(i)
        
        else :

           j+=1
           continue

    #print(database)
    dict_name = {}
    for table in database :  

        
        
        
        if table != [] :                          #creat file for tables
   
            table_file  = str(table[0][0])
            file_of_table = open(table_file + ".txt" , "w")
            
            
            

        for field in range(1, len(table)) :        #write header in table file
            
        
            
            field_tobe_written = str(table[field][0])
            file_of_table.write(field_tobe_written + " " )
        
        file_of_table.write("\n")
        
          
        for field in table:
            
            dict_name[field[0]] = list(field[1:])
        #print(dict_name)
    file_of_table.close()