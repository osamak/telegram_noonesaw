import aiopg
import asyncio
import secrets

dsn = 'dbname={} user={} password={} host=127.0.0.1'.format(secrets.DB_NAME,
                                                            secrets.DB_USERNAME,
                                                            secrets.DB_PASSWORD)

_lock = asyncio.Lock()
_db_pool = False

async def _acquire_pool():
    global _db_pool

    if _db_pool:
        return _db_pool

    async with _lock:
        if not _db_pool:
            _db_pool = await aiopg.create_pool(dsn)

    return _db_pool
