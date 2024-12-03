from flask import Flask, request, render_template_string

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html>
<head><title>Проверка времени сна</title></head>
<body>
  <h2>Введите время сна в формате ЧЧ-ММ:</h2>
  <form method="POST">
    <input type="text" name="time_sleep" placeholder="Например: 07-30">
    <input type="submit" value="Отправить">
  </form>
  <p>{{ message }}</p>
</body>
</html>
"""

def convertHoversToMinuts(timeSleep):
    h, m = map(int, timeSleep.split('-'))
    totalMin = h * 60 + m
    return totalMin

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        timeSleep = request.form.get("time_sleep")
        try:
            timeSleep = convertHoversToMinuts(timeSleep)
            if timeSleep < 360:
                message = "У вас недосып, старайтесь спать больше шести часов."
            elif 360 < timeSleep < 480:
                message = "Вы выполнили норму по продолжительности сна!"
            else:
                message = "Вы слишком долго спали, это плохо! Я вам завидую."
        except Exception:
            message = "Ошибка ввода! Пожалуйста, используйте формат ЧЧ-ММ."
    return render_template_string(html_template, message=message)

if __name__ == "__main__":
    app.run(debug=True)
