# methods of dictionary
marks = {
    "dhananjay":100,
    "shubham":56,
    "rishab":37
}
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"dhananjay":99})
print(marks)
print(marks.get("dhananjay"))
print(marks.get("dhananjay2"))#same ans but different (prints none) 
# print(marks["dhananjay2"])  #(returns an error)