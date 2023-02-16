from flask import render_template, request
from keep_alive import keep_alive, app

@app.route("/health")
    print("App is alive")
    return render_template("udm.html")

@app.route("/")
def main():
    return render_template("calculator.html")


@app.route("/calculate", methods=["POST"])
def calculate():
    number_one = request.form["number_one"]
    number_two = request.form["number_two"]
    operation = request.form["operation"]
    if(check_if_digt(number_one) and check_if_digt(number_two))
        result = _math(operation, number_one, number_two)
        if result==0:
            return render_template("calculator.html", result=result)
        else:
            return render_template("calculator.html")
    else:
            return render_template("calculator.html")



@app.errorhandler(404)
def not_found(error):
    return render_template("404.html", error=error)


@app.errorhandler(500)
def server_error(error):
    return render_template("500.html", error=error)

@app.errorhandler(403)
def forbidden(error):
    return render_template("403.html", error=error)

def check_if_digt(value):
    return value.isnumeric()

def _math(operation, num1, num2):
    print("reached here")
    match operation {
        case "add":
            return  float(num1) + float(num2);
        case "subtract":
            result = float(num1) - float(num1);
            return result;
        case "multiply":
            result = float(num1) * float(num2)
            return result;
        casee "divide":
            result = float(num1) / float(num2);
            return result;
        case "logn":
            result = math.log(float(num1));
            return result;
        case _:
            return 0;
    }     

if __name__ == "__main__":
    keep_alive()
