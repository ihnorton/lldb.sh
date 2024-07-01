# lldb.sh

Make your LLDB experience 26% better* with one weird trick: pipe the output of lldb commands to any normal shell command.
(x-ref [this stackoverflow question](https://stackoverflow.com/a/59003895)).

```
(lldb) command script import /path/to/lldbsh.py

(lldb) sh image list | wc -c
    3898

(lldb) sh env | grep SDKROOT
  SDKROOT=/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk
```

Pagers are also supported! (but, as yet, the subprocess is not killable):

```
(lldb) sh image list | less
...
```

\* does not improve symbolication speed :(
