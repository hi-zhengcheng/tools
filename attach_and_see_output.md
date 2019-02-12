Sometimes, one process was started from a terminal and printed out some log info. But the terminal suddenly crashed. When a new terminal was started, how to get the output of that process ?

Linux has a command `strace` to attach one process and get the output:

```bash
sudo strace -e trace=write -s 200 -f -p ${pid}
```

Args:

* -e trace=write: only trace write system call.
* -s 200: maximum string size to print.
* -f: include forked child processes.
* -p ${pid}: target process id.
    
