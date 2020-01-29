question:stone paper scissor
program:
print("a wish")
a=input()
print("b wish")
b=input()
if ((a=="stone") and (b=="paper")):
  print("b wins")
elif((a=="paper") and (b=="stone")):
  print("a wins")
elif ((a=="scissor") and (b=="paper")):
  print("a wins")
elif ((a=="paper") and (b=="scissor")):
  print("b wins")
elif ((a=="stone") and (b=="scirror")):
  print("a wins")
elif ((a=="scissor") and (b=="stone")):
  print("b wins")
elif ((a=="paper") and (b=="scissor")):
  print("b wins")
else:
  print("try agaimn")
