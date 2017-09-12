import asyncio
import datetime
import telepot.aio
import core
import secrets


bot = telepot.aio.Bot(secrets.TELEGRAM_TOKEN)

async def delete_older_messages():
    pool = await core._acquire_pool()
    unix_seconds = int(datetime.datetime.now().strftime("%s"))
    unix_seconds = 0

    async with pool.acquire() as aconnection:
        async with aconnection.cursor() as cursor:
            await cursor.execute("SELECT chat_id, message_id FROM messages WHERE is_deleted=FALSE AND message_date >= %s;", (unix_seconds,))
            results = await cursor.fetchall()
            for chat_id, message_id in results:
                message_identifier = (chat_id, message_id)
                print("Delete", message_id)
                await bot.deleteMessage(message_identifier)
                await cursor.execute("UPDATE messages SET is_deleted=TRUE WHERE message_id=%s;", (message_id,))

loop = asyncio.get_event_loop()

loop.run_until_complete(delete_older_messages())
