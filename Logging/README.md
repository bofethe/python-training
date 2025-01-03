# Logging in python

Python’s built-in `logging` module can be used to track events that happen while your code runs. It’s essential for debugging, monitoring, and understanding your application’s behavior. When building an application, `print()` statements can be used to quickly reveal insight on what's going on behind the scenes; however, when you're scheduling jobs such as in cron or Windows Task Scheduler, this information is lost and can make debugging or even noticing that something wrong is going on challenging. Logs can capture detailed info about what’s happening at different stages of your app and can be stored in files and displayed on the console. For more details, visit the reference documentation found [here](https://docs.python.org/3/library/logging.html). This repository gives a quick tutorial on how to get started using loggers.

There are different levels of logging, and only logs at or above the designated level will logged. Below are the 5 levels and their use cases.

| **Level**    | **Description**                             |
|--------------|-------------------------------------        |
| **DEBUG**    | Debugging info, low-level technical details |
| **INFO**     | General app information                     |
| **WARNING**  | Something to keep an eye on, *default*      |
| **ERROR**    | Recoverable errors                          |
| **CRITICAL** | Fatal errors, app crash imminent            |

In general, to get started logging you create the base logger object, create a handler to "handle" how the logs will be written, add the handler to the logger, and start logging similar to where you would add a `print()` statement. You can have many loggers, handlers, and output files depending on your project's needs. For example: a small scheduled process that only needs to log a few items periodically would be fine with a single log and handler, but a process that runs frequently and needs to log many DEBUG lines, it might be easier to have a critical-only log to quickly see if anything needs attention. Examples of both a single logger, and multiple loggers is provided in this repository.