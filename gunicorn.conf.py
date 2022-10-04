import multiprocessing

bind = "127.0.0.1:8000"
workers = 2
worker_class="gthread"
#threads=multiprocessing.cpu_count() * 2 + 1
threads=2
print_config=True


def worker_exit(server, worker):
    from djmin.connection import worker_exit as we
    we(server, worker)
