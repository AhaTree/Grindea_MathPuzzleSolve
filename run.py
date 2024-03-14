
####### modify "nums", "ops" and "target" here:#########
nums = [8,7,6,3,4] # <- change here 
ops = ["+","+","*","+"] # <- change here 
target = 160 # <- change here


########### Don't touch the rest, just run##############


nums = [str(x) for x in nums]
num_flag = [0] * len(nums)
op_flag = [0] * len(ops)

equation = ""

def make_str(equation, num_flag, op_flag):
    if not 0 in num_flag:
        if eval(equation) == target:
            print(equation)
            exit()
        else:
            return
    elif len(equation) == 0:
        for i in range(len(nums)):
            equation += nums[i]
            num_flag[i] = 1
            make_str(equation, num_flag, op_flag)
            equation = ""
            num_flag[i] = 0


    else:
        for i in range(len(ops)):
            if op_flag[i] == 1:
                continue
            else:
                for j in range(len(nums)):
                    if num_flag[j] ==1:
                        continue
                    else:
                        equation += ops[i]
                        op_flag[i] = 1
                        equation += nums[j]
                        num_flag[j] = 1
                        equation = "(" + equation
                        equation += ")"
                        make_str(equation, num_flag, op_flag)
                        equation = equation[1:-3]
                        num_flag[j] = 0
                op_flag[i] = 0


def make_str2(equation, rest_num, rest_op):
    if len(rest_num) == 0:
        if eval(equation) == target:
            print(equation)
            exit()
        else:
            return
    elif len(equation) == 0:
        for num in rest_num.copy():
            equation += num
            rest_num.remove(num)
            make_str2(equation, rest_num, rest_op)
            equation = ""
            rest_num.append(num)
    else:
        for op in rest_op.copy():
            for num in rest_num.copy():
                equation += op
                rest_op.remove(op)
                equation += num
                rest_num.remove(num)
                equation = "(" + equation
                equation += ")"
                make_str2(equation, rest_num, rest_op)
                equation = equation[1:-3]
                rest_num.append(num)
                rest_op.append(op)

make_str(equation, num_flag, op_flag)
# make_str2(equation, nums, ops)




