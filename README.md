# TGALib (Telegram Api Library)

# Usage

```python
from TGALib import TGA, emoji
import asyncio

app = TGA()

token = "6205861862:AAHi5kTdHELv2aVlNb2clFN-80AszYsCc60"
chat_id = 5041194621

for i in range(5):
    asyncio.run(app.send_message(token, chat_id, "hello", response=False))

asyncio.run(app.send_message(token, chat_id, f"Hello {emoji.ACCORDION}"))
asyncio.run(app.send_message(token, chat_id, f"Hello {emoji.ARTIST_PALETTE}"))
)

