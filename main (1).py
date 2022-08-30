import random 

def main ():
    """Kuiz jadual unsur berkala"""

    print ("Teka nama unsur")
  
    Unsur =["hidrogen", "nitrogen", "oksigen", "fluorin", "klorin", "iodin,magnesium","platinum", "silikon", "zink"] 

    player_name =str (input ("Masukkan Nama anda : ")) 
    x = random.choice (Unsur) 
  
    
    answer = None
    
    while x != answer: 
        if x == "hidrogen":
            print ('Hint 1:Mewakili simbol H dalam jadual berkala')
            print ('Hint 2:Mewakili nombor 1 dalam jadual berkala')
            answer = str (input ('Apakah jawapan anda? ')) 
            if answer!='hidrogen':
                print ('HAHAHAH Try again')
            else:
                print ('NICE') 
    
        elif x == "nitrogen":
            print ('Hint 1:Mewakili simbol N dalam jadual berkala')
            print ('Hint 2:Mewakili nombor 7 dalam jadual berkala')
            answer = str (input ('Apakah jawapan anda? ')) 
            if answer!='nitrogen':
                print ('HAHAHAH Try again')
            else:
                print ('NICE')
	    
        elif x == "oksigen":
            print ('Hint 1:Mewakili Simbol O dalam jadual berkala')
            print ('Hint 2:Mewakili nombor 8 dalam jadual berkala')
            answer = str (input ('Apakah jawapan anda? ')) 
            if answer!= 'oksigen':
                print ('HAHAHAH Try again')
            else:
                print ('NICE')
	        
        elif x == "fluorin":
            print ('Hint 1:Mewakili simbol F dalam jadual berkala')
            print ('Hint 2:Mewakili nombor 9 dalam jadual berkala')
            answer = str (input ('Apakah jawapan anda? ')) 
            if answer!= 'fluorin':
                print ('HAHAHAH Try again')
            else:
                print ('NICE') 
		
        elif x == "klorin":
            print ('Hint 1:Mewakili simbol CL dalam jadual berkala')
            print ('Hint 2:Mewakili nombor 17 dalam jadual berkala')
            answer = str (input ('Apakah jawapan anda? ')) 
            if answer!= 'klorin':
                print ('HAHAHAH Try again')
            else :
                print ('NICE') 
	   
        elif x == "iodin":
            print ('Hint 1:Mewakili simbol I dalam jadual berkala')
            print('Hint 2:Mewakili nombor 23 dalam jadual berkala')
            answer = str (input ('Apakah jawapan anda? ')) 
            if answer!= 'iodin':
                print ('HAHAHAH Try again')
            else:
                print ('NICE') 
		
        elif x == "magnesium":
            print('Hint 1:Mewakili simbol Mg dalam jadual berkala')
            print('Hint 2:Mewakili nombor 12 dalam jadual berkala')
            answer = str (input ('Apakah jawapan anda? ')) 
            if answer!= 'magnesium':
                print ('HAHAHAH Try again')
            else:
                print ('NICE') 
	    
        elif x == "platinum":
            print('Hint 1:Mewakili simbol Pt dalam jadual berkala')
            print('Hint 2:Mewakili nombor 78 dalam jadual berkala')
            answer = str (input ('Apakah jawapan anda? ')) 
            if answer!= 'platinum':
                print ('HAHAHAH Try again')
            else:
                print ('NICE') 
	    
        elif x == "silikon":
            print('Hint 1:Mewakili simbol Si dalam jadual berkala')
            print('Hint 2:Mewakili nombor 14 dalam jadual berkala')
            answer = str (input ('Apakah jawapan anda? ')) 
            if answer!= 'silikon':
                print ('HAHAHAH Try again')
            else:
                print ('NICE')
				    
        elif x == "zink":
            print('Hint 1:Mewakili simbol Zn dalam jadual berkala')
            print('Hint 2:Mewakili nombor 7 dalam jadual berkala')
            answer = str (input ('Apakah jawapan anda? '))
            if answer!= 'zink':
                print ('HAHAHAH Try again')
            else:
                print ('NICE')
    
    print("Terima kasih kerana telah menjawab soalan yang diberikan")
main()