import asyncio
import telepot
import telepot.aio
from telepot.aio.loop import MessageLoop
from telepot.aio.delegate import per_chat_id, create_open, pave_event_space
import core
import secrets


class Handler(telepot.aio.helper.ChatHandler):
    async def on_chat_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)

        if chat_type != 'supergroup':
            return

        message_date = msg['date']
        message_id = msg['message_id']

        query = "INSERT INTO messages (message_id, message_date, content_type, chat_id, is_deleted) VALUES (%s, %s, %s, %s, FALSE);"
        pool = await core._acquire_pool()
        async with pool.acquire() as aconnection:
            async with aconnection.cursor() as cursor:
                print("Inserted message id #{}".format(message_id))
                await cursor.execute(query, (message_id, message_date, content_type, chat_id))



bot = telepot.aio.DelegatorBot(secrets.TELEGRAM_TOKEN, [
    pave_event_space()(
        per_chat_id(), create_open, Handler, timeout=10),
])

loop = asyncio.get_event_loop()
loop.create_task(MessageLoop(bot).run_forever())
print('Listening ...')

loop.run_forever()
