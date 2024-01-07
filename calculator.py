name=str(input("Adınızı qeyd edin: "))
print(f"Salam {name} Calculator proqramına xoş gəldiniz!!!")
 
while True:
 	number1=int(input("Please type your first number: "))
 	number2=int(input("Please type your second number: "))
 	operation=str(input("Select your opreration (You can select *,/,+,- ):"))
 	def operation_func(x):
 		if x=="*":
 			print(f"{number1}*{number2}=",number1*number2)
 		elif x=="/":
 			print(f"{number1}/{number2}=",number1/number2)
 		elif x=="+":
 			print(f"{number1}+{number2}=",number1+number2)
 		elif x=="-":
 			print(f"{number1}-{number2}=",number1-number2)
 		else:
 			print("You must select valid operators!!! (You can select *,/,+,- ) ")
 	operation_func(operation)
 			

