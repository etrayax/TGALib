# TGALib (Telegram Api Library)

# Usage

```python
from TGALib import TGA, emoji
import asyncio

app = TGA()

token = ""
chat_id = 

for i in range(5):
    asyncio.run(app.send_message(token, chat_id, "hello", response=False))

asyncio.run(app.send_message(token, chat_id, f"Hello {emoji.ACCORDION}")) # Hello 🪗
asyncio.run(app.send_message(token, chat_id, f"Hello {emoji.ARTIST_PALETTE}")) # Hello 🎨
)

