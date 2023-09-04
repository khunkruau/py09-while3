#การเขียนโปรแกรมแบบทำซ้ำโดยการถามตอบและมีลูปซ้อนใน
yesno = "y"
while (yesno =="y") :
    myfname = input("โปรดป้อนชื่อของท่าน ? ")
    myage = int(input("โปรดอายุของท่าน ? "))
    for i in range(myage):
        print("สวัสดีคุณ "+myfname)
        print("คุณเกิดปี พ.ศ. "+str(2566-myage))
    yesno = input("คำนวณต่อหรือไม่ ? [y/n]")
    