import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')

    t1=1/power
    for i in range(5):
        await asyncio.sleep
        print(f'Силач {name} поднял {i+1} шар.')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task1=asyncio.create_task(start_strongman(name='Александр', power=5))
    task2=asyncio.create_task(start_strongman(name='Валерий', power=3))
    task3=asyncio.create_task(start_strongman(name='Вадим', power=4))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())