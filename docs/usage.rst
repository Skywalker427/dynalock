=====
Usage
=====

To use dynalock in a project::

    from dynalock import DynaLock

    distributed_lock = DynaLock(
        table_name='my_table',
        region_name='us-west-2',
        lock_id='api_lock',
    )

    with distributed_lock:
        # do something that requires a lock


=================


