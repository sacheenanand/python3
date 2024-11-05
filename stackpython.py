list = [3, 3, 10, 7, 4,3,0]
stack = []

for element in list:
    if element % 2 == 1:  # Check if element is odd
        stack.append(element)  # Push odd element to the stack
    else:
        if stack:  # Ensure stack is not empty before popping
            old_element = stack.pop()  # Pop the top element from the stack
            if old_element > element:
                stack.append(old_element)  # Push the popped element back if it's greater
print(stack)

'''
Q3. A
Q4. C i.e. 3
Q5. B, D, E
Q6. not sure
Q7. E
Q8. A, D
Q9. D
Q10. A, B, C, D
Q11. C




'''


