import lldb
import subprocess

def sh(debugger, command, result, dict):
  commands = command.split("|")
  lldb_cmd = commands[0]

  interpreter = debugger.GetCommandInterpreter()
  res = lldb.SBCommandReturnObject()
  interpreter.HandleCommand(lldb_cmd, res)

  if not res.Succeeded():
      raise Exception("failed to execute lldb command!")
  if not res.GetOutput():
      return

  if len(commands) == 1:
    # `sh command` is equivalent to `command`
    print(res.GetOutput())
    return
  elif len(commands) == 2:
    # TODO support chaining?
    shell_cmd = commands[1]

  # TODO: Not sure what the underlying buffer is for HandleCommand, but
  # ideally do some check/optim for really large output.
  output = res.GetOutput().encode('UTF-8')
  proc = subprocess.Popen(shell_cmd, shell=True, stdin=subprocess.PIPE)

  # TODO?
  # Not using a timer here allows piping to a pager. However,
  # it also means that the shell-out process may not be killable.
  try:
      out, errs = proc.communicate(output)
  except:
      print("Unexpected exit, killing subprocess")
      proc.kill()
      outs, errs = proc.communicate()

def __lldb_init_module (debugger, dict):
  res = lldb.SBCommandReturnObject()
  interpreter = debugger.GetCommandInterpreter()
  interpreter.HandleCommand('command script delete sh', res)
  debugger.HandleCommand('command script add -f lldbsh.sh sh ')
