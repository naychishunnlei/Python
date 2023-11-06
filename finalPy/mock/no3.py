def count_operands_in_expr(expr):
    if type(expr) != tuple:
        return 1
    else:
        return count_operands_in_expr(expr[0]) + count_operands_in_expr(expr[2])
    
print(count_operands_in_expr((3, '**', 4)))