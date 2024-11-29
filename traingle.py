def main ():#line:1
    try :#line:2
        O0OOO00O0O00O0OO0 =float (input ('Enter first side: '))#line:3
        OO00OOO0OO0O0OO0O =float (input ('Enter second side: '))#line:4
        OO0000O000000O00O =float (input ('Enter third side: '))#line:5
        O0OOO0O00OO0O0OOO =(O0OOO00O0O00O0OO0 +OO00OOO0OO0O0OO0O +OO0000O000000O00O )/2 #line:8
        OOO00OO0000OOOO00 =(O0OOO0O00OO0O0OOO *(O0OOO0O00OO0O0OOO -O0OOO00O0O00O0OO0 )*(O0OOO0O00OO0O0OOO -OO00OOO0OO0O0OO0O )*(O0OOO0O00OO0O0OOO -OO0000O000000O00O ))**0.5 #line:11
        print ('The area of the triangle is %0.2f'%OOO00OO0000OOOO00 )#line:12
    except ValueError :#line:14
        print ("Invalid input! Please enter numeric values.")#line:15
if __name__ =="__main__":#line:17
    main ()