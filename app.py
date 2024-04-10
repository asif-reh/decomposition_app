from flask import Flask, request, render_template

app = Flask(__name__)

def Decomposition_Powers_Three(n):
    # ... (same code as before)
    decomposition = []  # Initialize an empty list to store the decomposition

    def decompose_helper(num, power):
        if num == 0:
            return
        elif num % 3 == 0:
            # If divisible by 3, add the positive power of 3 to the decomposition
            decomposition.append(f"{3 ** power}")
            decompose_helper(num // 3, power + 1)
        elif num % 3 == 1:
            # If remainder is 1, add the positive power of 3 and subtract 1
            decomposition.append(f"{3 ** power} - 1")
            decompose_helper((num - 1) // 3, power + 1)
        else:
            # If remainder is 2, add the negative power of 3 and add 1
            decomposition.append(f"-{3 ** power} + 1")
            decompose_helper((num + 1) // 3, power + 1)

    # Start the decomposition
    decompose_helper(n, 0)
    
    return decomposition

result = Decomposition_Powers_Three(42)
print("Decomposition of 42 using powers of 3:")
print(" + ".join(result))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num = int(request.form['number'])
        decomposition = Decomposition_Powers_Three(num)
        return render_template('result.html', num=num, decomposition=decomposition)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
