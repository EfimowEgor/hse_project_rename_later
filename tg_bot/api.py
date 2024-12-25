from aiohttp import ClientSession, ClientConnectorError


async def get_data_from_api(url):
    try:
        async with ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                
    except ClientConnectorError:
        pass
    
    return None
