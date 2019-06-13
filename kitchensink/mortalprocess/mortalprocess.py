__author__ = 'Dean M. Sands, III (deanmsands3@gmail.com)'
import multiprocessing
import threading


class TidyTP(object):
    def __init__(self, *args, **kwargs):
        pass

    def setup(self):
        pass

    def loop(self):
        pass

    def clean_up(self):
        pass

    def finish(self):
        pass


class TidyProcess(multiprocessing.Process, TidyTP):
    def __init__(self, group=None, name=None, args=(), kwargs=None):
        super(TidyProcess, self).__init__(group=group, name=name, args=args, kwargs=kwargs)
        pass

    def run(self):
        self.setup()
        self.loop()
        self.clean_up()


class TidyThread(threading.Thread, TidyTP):
    def __init__(self, group=None, name=None, args=(), kwargs=None):
        super(TidyThread, self).__init__(group=group, name=name, args=args, kwargs=kwargs)
        pass

    def run(self):
        self.setup()
        self.loop()
        self.clean_up()


class MortalProcess(TidyProcess):
    """
    MortalProcess is a Process that runs a side thread designed to kill it.
    """
    def __init__(self, group=None, name=None, args=(), kwargs=None):
        super(MortalProcess, self).__init__(group=group, name=name, args=args, kwargs=kwargs)
        self._lethal_thread = MortalProcess.LethalThread(kwargs={"parent": self})
        self._blocker = multiprocessing.Queue()

    def run(self):
        self._pre_setup()
        self.setup()
        self._post_setup()
        self.loop()
        self._pre_clean_up()
        self.clean_up()
        self._post_clean_up()

    def _pre_setup(self):
        self._lethal_thread.start()

    def _post_setup(self):
        self._blocker.put("Feed the Queue.")

    def _pre_clean_up(self):
        self._lethal_thread.join()

    def _post_clean_up(self):
        pass

    def wait_til_ready(self):
        _dummy = self._blocker.get()

    def stop(self):
        pass

    def finish(self):
        self._lethal_thread.give_kill_order()

    class LethalThread(TidyThread):
        """
        LethalThread is a private class inside MortalProcess.
        Do NOT "correct" the indentation.
        """

        def __init__(self, group=None, name=None, args=(), kwargs=None):    # kwargs should not be None.
            assert(                                                         # Observe.
                (isinstance(kwargs, dict)) and
                ('parent' in kwargs)
            )
            super(MortalProcess.LethalThread, self).__init__(group=group, name=name, args=args, kwargs=kwargs)
            self._kill_order = multiprocessing.Queue()
            self.parent = kwargs['parent']

        def loop(self):
            _dummy = self._kill_order.get(block=True)

        def clean_up(self):
            self.parent.stop()
        
        def give_kill_order(self):
            self._kill_order.put("You're always welcome at our house.")  # https://www.youtube.com/watch?v=wH2x4KuRQVQ


# I'll get to this one later
class MortalProcessWrapper(object):
    def __init__(self, *args, **kwargs):
        pass
