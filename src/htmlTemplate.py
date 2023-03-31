class HtmlTemplate:
    def __init__(self, data):
        self.header = '''<!DOCTYPE html>
<html>
<head>
<style>
table {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

table td, table th {
  border: 1px solid #ddd;
  padding: 8px;
}

table tr:nth-child(even){background-color: #f2f2f2;}

table tr:hover {background-color: #ddd;}

table th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #04AA6D;
  color: white;
}
</style>
</head>
<body>'''

        self.footer = '''</body>
                            </html>'''

        self.data = data

    def get_html(self):
        html = self.header
        html += self.data
        html += self.footer
        return html