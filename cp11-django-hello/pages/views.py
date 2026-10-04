from django.http import HttpResponse

PAGE = """<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Моя фраза</title>
<style>
  :root { color-scheme: light dark; }
  body { margin: 0; min-height: 100vh; display: grid; place-content: center; gap: 12px; padding: 24px; text-align: center; background: light-dark(#f5f5f7, #000); color: light-dark(#1d1d1f, #f5f5f7); font: 17px/1.47 -apple-system, BlinkMacSystemFont, system-ui, sans-serif; }
  h1 { margin: 0; max-width: 820px; font-size: clamp(2.5rem, 5vw + 1rem, 4.5rem); line-height: 1.05; letter-spacing: -0.035em; }
  p { margin: 0; color: light-dark(#6e6e73, #a1a1a6); }
</style>
</head>
<body>
<p>Первое приложение Django</p>
<h1>Код пишут для людей, а исполняют машины.</h1>
<p>— Тигран Мхитарян</p>
</body>
</html>"""


def home_page_view(request):
    return HttpResponse(PAGE)
