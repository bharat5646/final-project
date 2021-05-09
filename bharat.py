helpline_no=["0866-2410978","9436055743","6913347770","104","8558893911","0471-2552056","020-26127394","3852411668","108","102","7005539653","9439994859","0141-2225624","044-29510500","0381-2315879","18001805145","1800313444222","03323412600","03192-232102","9779558282","011-22307145","01912520982"," 0194-2440283","01982256462"]
print("****************Check any phone no. authenticity pretending to be a covid helpline no.*******************")
suspicious_no=input("Enter the suspicious phone no.(please include all symbols like -,space etc which are ther in the no.):")
flag=0
for i in range(len(helpline_no)):
    if suspicious_no==helpline_no[i]:
        flag=1
        break
if flag==1:
    print("The no. seems valid")
else:
    print("Alert! The no. seems fraud. please talk wisely")