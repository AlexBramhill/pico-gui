import uasyncio


class CoroutineCreator():
    @staticmethod
    def debouncedCoroutine(is_triggered, button_event, debounce_time, loop_time):
        async def debounced_coroutine():
            while True:
                if is_triggered():
                    button_event()
                    await uasyncio.sleep(debounce_time)
                await uasyncio.sleep(loop_time)
        return debounced_coroutine
