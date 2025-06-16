from flask import Flask, render_template_string

app = Flask(__name__)

ipl_winners = [
    {'year': 2025, 'winner': 'Royal Challengers Bengaluru'},
    {'year': 2024, 'winner': 'Kolkata Knight Riders'},
    {'year': 2023, 'winner': 'Chennai Super Kings'},
    {'year': 2022, 'winner': 'Gujarat Titans'},
    {'year': 2021, 'winner': 'Chennai Super Kings'},
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Last 5 Years IPL Winners</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        :root {
            --matte-bg: #232946;
            --matte-card: #121629;
            --accent: #eebbc3;
            --text: #f4f4f6;
            --header: #b8c1ec;
            --row-alt: #393e60;
            --shadow: rgba(20, 20, 30, 0.25);
        }
        body {
            background: var(--matte-bg);
            color: var(--text);
            font-family: 'Segoe UI', 'Roboto', Arial, sans-serif;
            margin: 0;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        .container {
            background: var(--matte-card);
            border-radius: 18px;
            box-shadow: 0 6px 32px var(--shadow);
            padding: 2.5rem 2rem;
            margin-top: 2rem;
            max-width: 420px;
            width: 100%;
        }
        h2 {
            color: var(--header);
            text-align: center;
            margin-bottom: 1.5rem;
            letter-spacing: 1px;
            font-weight: 700;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            background: transparent;
        }
        th, td {
            padding: 0.85rem 0.5rem;
            text-align: center;
        }
        th {
            background: var(--matte-bg);
            color: var(--accent);
            font-size: 1.1rem;
            letter-spacing: 1px;
            border-bottom: 2px solid var(--accent);
        }
        tr {
            transition: background 0.2s;
        }
        tr:nth-child(even) td {
            background: var(--row-alt);
        }
        tr:hover td {
            background: var(--accent);
            color: var(--matte-card);
        }
        td {
            font-size: 1rem;
            border-bottom: 1px solid #32365a;
        }
        @media (max-width: 600px) {
            .container {
                padding: 1rem 0.2rem;
                max-width: 98vw;
            }
            th, td {
                padding: 0.6rem 0.2rem;
                font-size: 0.95rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Last 5 Years IPL Winners (2021–2025)</h2>
        <table>
            <tr>
                <th>Year</th>
                <th>Winner</th>
            </tr>
            {% for item in winners %}
            <tr>
                <td>{{ item.year }}</td>
                <td>{{ item.winner }}</td>
            </tr>
            {% endfor %}
        </table>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, winners=ipl_winners)

if __name__ == '__main__':
    app.run(debug=True)
