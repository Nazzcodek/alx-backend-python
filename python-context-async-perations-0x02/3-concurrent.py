import asyncio
import aiosqlite

async def async_fetch_users():
    """Asynchronously fetch all users from the database"""
    async with aiosqlite.connect('users.db') as db:
        cursor = await db.execute("SELECT * FROM users")
        results = await cursor.fetchall()
        return results

async def async_fetch_older_users():
    """Asynchronously fetch users older than 40 from the database"""
    async with aiosqlite.connect('users.db') as db:
        cursor = await db.execute("SELECT * FROM users WHERE age > ?", (40,))
        results = await cursor.fetchall()
        return results

async def fetch_concurrently():
    """Execute both queries concurrently using asyncio.gather"""
    # Run both queries concurrently
    all_users, older_users = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )
    
    print("All Users:")
    for user in all_users:
        print(user)
    
    print("\nUsers older than 40:")
    for user in older_users:
        print(user)

# Run the concurrent fetch
asyncio.run(fetch_concurrently())