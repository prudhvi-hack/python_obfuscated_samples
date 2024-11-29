def main ():#line:1
    try :#line:3
        OO0OO0O0O0O00OOO0 =input ('Enter value of x: ')#line:4
        OO0O000OO0OOO0OOO =input ('Enter value of y: ')#line:5
        O0000O000000OO0OO =OO0OO0O0O0O00OOO0 #line:8
        OO0OO0O0O0O00OOO0 =OO0O000OO0OOO0OOO #line:9
        OO0O000OO0OOO0OOO =O0000O000000OO0OO #line:10
        print ('The value of x after swapping: {}'.format (OO0OO0O0O0O00OOO0 ))#line:13
        print ('The value of y after swapping: {}'.format (OO0O000OO0OOO0OOO ))#line:14
    except ValueError :#line:16
        print ("Invalid input! Please enter numeric values.")#line:17
if __name__ =="__main__":#line:19
    main ()