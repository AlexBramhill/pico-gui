import uasyncio as uasyncio
from machine import Pin
from interaction import CoroutineCreator


button_a = Pin(12, Pin.IN, Pin.PULL_UP)
button_b = Pin(13, Pin.IN, Pin.PULL_UP)
button_c = Pin(14, Pin.IN, Pin.PULL_UP)


def is_button_a_pressed(): return not button_a.value()
def is_button_b_pressed(): return not button_b.value()
def is_button_c_pressed(): return not button_c.value()


async def log_coroutine():
    try:
        while True:
            print('Async loop running')
            await uasyncio.sleep(2)
    except uasyncio.CancelledError:
        print('log_test cancelled')


def a_button_action(): print('a_button_pressed')


a_button_coroutine = CoroutineCreator.debouncedCoroutine(
    is_button_a_pressed, a_button_action, 1, 0.2
)


def create_b_button_action(a_button_task: uasyncio.Task):
    def b_button_action():
        nonlocal a_button_task
        print('b_button_pressed')
        if not a_button_task.done():
            a_button_task.cancel()
        else:
            print('log trying to start')
            loop = uasyncio.get_event_loop()
            a_button_task = loop.create_task(a_button_coroutine())
    return b_button_action


def create_b_button_coroutine(a_button_task):
    return CoroutineCreator.debouncedCoroutine(
        is_button_b_pressed, create_b_button_action(a_button_task), 1, 0.2)


def create_c_button_action(log_task: uasyncio.Task):
    def c_button_action():
        nonlocal log_task
        print('c_button_pressed')
        if not log_task.done():
            log_task.cancel()
        else:
            print('log trying to start')
            loop = uasyncio.get_event_loop()
            log_task = loop.create_task(log_coroutine())
    return c_button_action


def create_c_button_coroutine(log_task):
    return CoroutineCreator.debouncedCoroutine(
        is_button_c_pressed, create_c_button_action(log_task), 1, 0.2
    )


async def main():
    loop = uasyncio.get_event_loop()
    log_task = loop.create_task(log_coroutine())
    a_button_task = loop.create_task(a_button_coroutine())
    b_button_task = loop.create_task(
        create_b_button_coroutine(a_button_task)())
    c_button_task = loop.create_task(
        create_c_button_coroutine(log_task)())

    try:
        loop.run_forever()
    except Exception as e:
        print(f'Exception: {e}')
        loop.stop()
    # log_task = uasyncio.run(log_coroutine())
    # a_button_task = uasyncio.run(a_button_coroutine())
try:
    # uasyncio.run(main()) is used to start the main coroutine and handle the event loop.
    # This ensures that the main coroutine runs until completion or until an exception occurs.
    uasyncio.run(main())
except uasyncio.CancelledError:
    print('CancelledError123')
except KeyboardInterrupt:
    print('KeyboardInterrupt')
finally:
    loop = uasyncio.get_event_loop()
    loop.stop()
    loop.close()
