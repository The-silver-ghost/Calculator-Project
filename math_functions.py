def regular_calc(question_string):
    answer = eval(question_string)
    return answer

def quadratic_calc(number_list):
    a = float(number_list[0])
    b = float(number_list[1])
    c = float(number_list[2])

    x_1 = ((-b)-(((b**2)-4*a*c)**0.5))/(2*a)
    x_1 = "{:.3f}".format(x_1)
    x_2 = ((-b)+(((b**2)-4*a*c)**0.5))/(2*a)
    x_2 = "{:.3f}".format(x_2)
    answer = f"x₁ = {x_1}, x₂ = {x_2}"
    return answer