
# # n = int(input(""))

# # for i in range(n):
# #     for col in range(n-i-1):
# #         print(" ",end='')
# #     for col in range(i+1):
# #         print("*",end=' ')
# #     print()

n = int(input(""))

for i in range(n):
    # สร้างช่องว่างด้านซ้าย
    for col in range(i):
        print(" ", end='')
    
    # พิมพ์เครื่องหมายดอกจัน
    for col in range(n - i):
        print("*", end=' ')
    
    # ขึ้นบรรทัดใหม่
    print()




# name = input("")

# for i in range(len(name)):
#     for col in range(len(name) - i - 1):
#         print(" ", end='')

#     for col in range(i + 1):
#         print(name[col], end=' ')
#     print()



# name = "FITM"

# for i in range(len(name)):
#     for col in range(len(name) - i - 1):
#         print(" ",end='')
#     for col in range(i+1):
#         print(name[col],end= ' ')
#     print()




# name = "FITM"

# for i in range(len(name)):
#     for col in range(len(name)-i):
#         print(" ",end='')
#     for col in range(i+1):
#         print(name[col],end=' ')
#     print()




















'''
* * * * * 
 * * * * 
  * * * 
   * * 
    * 

'''