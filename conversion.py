def main ():#line:1
    try :#line:3
        OO0OOO00O00O00O00 =float (input ("Enter value in kilometers: "))#line:5
        OO0000OO00OO0OO0O =0.621371 #line:8
        OOOOO00O000O00O00 =OO0OOO00O00O00O00 *OO0000OO00OO0OO0O #line:11
        print ('%0.2f kilometers is equal to %0.2f miles'%(OO0OOO00O00O00O00 ,OOOOO00O000O00O00 ))#line:14
    except ValueError :#line:16
        print ("Invalid input! Please enter numeric values.")#line:17
if __name__ =="__main__":#line:19
    main ()